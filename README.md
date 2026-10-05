# UltraHaul — development prototype

A real R.E.P.O. BepInEx 5 mashup, using V1, weapon models/animations, coins and sounds from the player's installed ULTRAKILL copy.

Start with R.E.P.O.'s normal looting objective. Fragile valuables keep their native physics, damage, value and extraction rules. Draw a revolver or shotgun to protect the haul; holster to grab valuables again. Dash, slide and slam through rooms. Coin ricochets, shotgun projectile boosts and timed close-range parries reward style. Style refills dash energy and briefly improves damage and firing speed; it never adds money or shields loot.

## Requirements and current scope

Both R.E.P.O. and ULTRAKILL must be installed. R.E.P.O. is the running host game; ULTRAKILL supplies local assets and is never redistributed. Tested installations: R.E.P.O. v0.4.4.3 / Steam build 23363152, ULTRAKILL Steam build 22957324. Other versions are unverified. BepInEx 5.4.23.5 is the loader Melty can install automatically. No Python, toolkit, asset export or additional runtime is needed by players.

Solo and private co-op are intended in the first release. Native Steam/Photon lobbies support up to six players; every player needs both games and the same mod. TWO-CLIENT HOST/JOIN AND COMBAT ARE STILL UNVERIFIED. This is not a finished multiplayer release and has not been submitted or published on Melty. Do not infer co-op support from successful compilation.

## Controls

Defaults: G draw/holster, R switch weapons, left mouse fire, right mouse toss a revolver coin, F parry or boost a freshly fired shotgun shot. Dash uses the player's saved R.E.P.O. Sprint binding; slide/slam uses the saved Crouch binding. The HUD displays actual bindings. Custom mod actions are remappable in BepInEx/config/local.ultrahaul.cfg. Ammunition is unlimited.

Parries currently counter native enemy hits inside three metres while facing the attacker, within a 0.22-second window. Shotgun boosts turn a traveling pellet packet into an explosive shot. Native loot remains breakable, including from combat impacts.

## Development and verification

JSON sheets in Sheets are the source of truth. Build.ps1 runs a complete cell/reference preflight and generates one C# struct per row before compilation. Tools/self_check.py rejects missing cells, unresolved references and nonfinite values. Tools/runtime_check.py drives the actual installed game and checks real native movement, enemy damage and timed incoming-hit hooks; its development commands require ULTRAHAUL_DEV=1 and stay inactive during normal play. Source-only, untested and pending behaviors are tracked in MODLOG.md and test-results.json.

## Credits and publishing choices

Concept and gameplay choices: the project owner; public credit name pending confirmation.
ULTRAKILL assets: Arsi “Hakita” Patala, the ULTRAKILL team and New Blood Interactive, loaded only from the player's copy.
R.E.P.O.: semiwork; native worlds, enemies, physics, valuables, extraction and Steam/Photon networking.
BepInEx and Harmony: their respective open-source contributors, provided by the loader.
Development toolkit: rehan-remade/universal-modder. No paid asset generation used.

Content/source license and Melty remix permission have not been chosen by the owner. This development package is for local testing and is not an upload-ready release.
