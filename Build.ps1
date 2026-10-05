$ErrorActionPreference='Stop'
$taskRoot = $PSScriptRoot
$taskPython = 'C:\Users\roryk\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $taskPython (Join-Path $taskRoot 'Tools/preflight.py')
if($LASTEXITCODE -ne 0) { throw 'Sheet preflight failed; build cancelled.' }
dotnet build (Join-Path $taskRoot 'UltraHaul.csproj') -c Release --nologo
if($LASTEXITCODE -ne 0) { throw 'Build failed.' }
