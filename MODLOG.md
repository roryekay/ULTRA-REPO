# UltraHaul development journal

User-approved concept: loot-first R.E.P.O. with V1, dash/slide/slam, revolver coin shots, shotgun projectile boosts, parries, and style that refills dash and briefly boosts combat. Solo and cooperative play are required in the first release. Fragile valuables retain native damage and value rules.

Primary game: C:/Program Files (x86)/Steam/steamapps/common/REPO, Steam build 23363152, Unity 2022.3.67f2 Mono/C#.
Secondary game: C:/Program Files (x86)/Steam/steamapps/common/ULTRAKILL, Steam build 22957324, Unity 2022.3.29f1 Mono/C#.
Melty: connected over Python HTTPS JSON-RPC; account has no mods. Both games support Melty automatic BepInEx 5.4.23.5. No ULTRAKILL/REPO mashup currently listed. Working example: ultrakill-risk-of-rain (reads assets from local ULTRAKILL).

Chosen route: BepInEx 5 plugin with Harmony hooks and Photon PUN host-authoritative combat. Keep R.E.P.O. existing relay/lobby transport. Read only targeted game types. Decompiled files stay in ../reference, outside this project. Game assets stay outside source and package; local importer reads the user's ULTRAKILL installation.

Tools acquired: universal-modder clone ../universal-modder; ILSpy 9.1.0.7988 in ../ilspy; UnityPy 1.25.4/PyYAML and dependencies in ../pydeps. Existing .NET 9 SDK and FFmpeg with gfxcapture available. No paid generation or fal key used.

Status: first plugin compiles cleanly (222 defined cells, 30 generated structs) and loads in native R.E.P.O. with global BepInEx defaults. Saved games and original loader files backed up before installation. Both Steam builds listed above verified. Native ULTRAKILL AssetBundle loading works across these two Unity 2022 versions; no importer/runtime or extracted game assets need redistribution.

Installed BepInEx 5.4.23.5 from official GitHub release into REPO, ILSpy 9.1.0.7988 locally, UnityPy 1.25.4 locally, and BtbN FFmpeg with real gfxcapture under LocalAppData/universal-modder. No paid services used.

Runtime evidence so far: clean native startup; V1/revolver/shotgun subassets loaded; saved bindings Sprint=C, Crouch=LeftShift; dash input C reduced charge and moved actual controller ~3.6m; custom F arms parry. Native tutorial and new solo Arctic run entered. Gun animation scale reset found with live renderer telemetry, correction under test. Native slide speed and host-broadcast coin/shell end events added; not yet verified in co-op. Enemy damage, coin ricochet, projectile boost, incoming parry, loot physics, slide and slam still need runtime checks. Never infer runtime success from preflight.

Current iteration: REPO PID 26036; dev bridge ULTRAHAUL_DEV=1 (local files in LocalAppData/UltraHaul/dev). Original saves are in tool-state/backups/repo-saves/20261005-183725.zip. Global HideManagerGameObject remains false; plugin sets its own manager hide flags so Melty defaults work.

Nothing uploaded or published. Listing title, credit name, license/remix choices remain unconfirmed. Solo and private co-op are both required; two-client host/join test required before saying co-op works. Native limit 6 with Steam/Photon relay, no invented server. Leave automatic connect out if joining is untested.

Latest verified findings: native collider health lives under EnemyParent, often beside the collider hierarchy rather than above it. One shared resolver fixes revolver, shotgun, ricochets and explosions. Native EnemyDirector attacker index is the correct parry target, not solo Photon ViewID (zero for several enemies). Timed native Hurt integration passed: 100→100 inside window, 100→95 after 0.35s, enemy counter damaged/killed and dash refilled 1.72. Scripted incoming hit; natural AI attack timing remains a separate playtest.

Movement measured: horizontal dash peak 22.46 m/s (configured 23), slam min vertical -27.40 m/s. Native slide log confirmed. Initial test failure was buffered BepInEx LogOutput reading before flush; real-time Player.log is now the runtime oracle. New crouch-to-slide entry reuses native slide physics and animation. Full combined runtime suite still under test.

Native coin model mapping: FBX hash fb46724754ff9044b80f6df9d583440d, GameObject coin, Mesh Cylinder (not coin). No coin sphere substitute in current build. Melty can pass secondary game folder through ULTRAHAUL_ULTRAKILL; Steam discovery remains a fallback. Asset gating deliberately refuses incompatible mappings.

Lifecycle now waits for native LateStart movement values before enabling gameplay, resets combat/style on controller replacement, waits for matching ready peer protocol, restores native movement/body for mixed lobbies, and does not overwrite global BepInEx config. G draw avoids native Q tumble; custom and native bindings appear in HUD. Shared materials prevent leaks on repeated weapon swaps/coin tosses.

Current native game PID 26852. No Melty draft/upload exists. Next: complete combined suite, authenticate two native Steam clients if supported, inspect package/recipe, capture this exact version, and obtain listing/credit/license/remix choices. Do not publish without a verified build, installation, actual media, user Melty Test and publication authorization.
