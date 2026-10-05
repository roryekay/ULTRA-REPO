"""Check the loaded plugin in the actual game. Requires ULTRAHAUL_DEV=1.
Run in a fresh development save, never a player's existing run.
"""
import hashlib,json,os,re,sys,time
from pathlib import Path
from um.win import Drive,shot

root=Path(__file__).resolve().parents[1]
bridge=Path(os.environ['LOCALAPPDATA'])/'UltraHaul'/'dev'
log=Path(os.environ['USERPROFILE'])/'AppData/LocalLow/semiwork/REPO/Player.log'
def state():
    try:return json.loads((bridge/'state.json').read_text())
    except (OSError,json.JSONDecodeError):return {}
def wait(predicate,seconds=20):
    stop=time.monotonic()+seconds
    while time.monotonic()<stop:
        s=state()
        if predicate(s):return s
        time.sleep(.05)
    raise AssertionError('Runtime state did not reach condition: '+str(state()))
def command(text,delay=.15):
    path=bridge/'command.txt';tmp=bridge/'command.tmp';tmp.write_text(text);tmp.replace(path)
    stop=time.monotonic()+5
    while path.exists() and time.monotonic()<stop:time.sleep(.02)
    assert not path.exists(),'Game did not consume '+text
    time.sleep(delay)
def god(enabled):
    if state().get('godMode')!=enabled:command('native godmode');wait(lambda s:s.get('godMode')==enabled)

assert state().get('assets'),'Wait for native ULTRAKILL assets to load.'
if not state().get('playing'):
    command('run');wait(lambda s:s.get('playing'))
time.sleep(.5)
start=len(log.read_text());evidence={}
god(True)
command('movement point',.3)
command('measure')
d=Drive('REPO');d.focus();d.cmd('scanmode on');d.key('0x43');time.sleep(.6)
s=state();assert s.get('peakSpeed',0)>=20,s;evidence['dash']=s
command('movement point',.3);d.key('0x57','down');time.sleep(.2);d.cmd('hold 0xA0 400');d.key('0x57','up');time.sleep(.3)
assert 'ACTION native slide' in log.read_text()[start:],'Native slide did not start.'
command('movement point',.3);command('measure');d.key('0x20',pause=.02);time.sleep(.03);d.cmd('hold 0xA0 250');time.sleep(.6)
s=state();assert s.get('minVertical',0)<=-24,s;evidence['slam']=s
command('freeze enemies');command('near enemy',.2);command('aim enemy',.2);command('equip');command('fire',.5)
command('coin shot',.7);command('aim enemy',.2);command('boost shot',.7)
text=log.read_text()[start:]
for kind in ['revolver','coin','boost']:
    assert re.search(r'HIT .+ \d+ -> \d+ via '+kind,text),'No real enemy hit via '+kind
evidence['combat']=text
evidence['stateAfterCombat']=state()
god(False)
command('parry test',.9)
text=log.read_text()[start:]
timed=re.search(r'CHECK timed native incoming hit: health (\d+) -> (\d+) dash=([\d.]+)',text)
expired=re.search(r'CHECK expired window: health (\d+) -> (\d+)',text)
assert timed and timed[1]==timed[2] and float(timed[3])>0,text
assert expired and int(expired[2])<int(expired[1]),text
evidence['parry']=text
evidence['note']='Actual native game, enemies and loot. God mode isolates damage tests; disabled for timed native Hurt/parry check. Native incoming hit is scripted; AI attack timing is a separate playtest.'
evidence['pluginSha256']=hashlib.sha256((root/'bin/Release/netstandard2.1/UltraHaul.dll').read_bytes()).hexdigest()
evidence['cooperativeJoin']='pending two authenticated clients'
(root/'test-results.json').write_text(json.dumps(evidence,indent=2)+'\n')
print('PASS: real dash/slide/slam, enemy revolver/coin/boost damage, timed native parry and expired window. Co-op remains pending.')
