; Boostly Tweaks Installer Script
; Requires Inno Setup (free): https://jrsoftware.org/isdl.php
;
; This turns dist\BoostlyTweaks.exe (built by build_exe.bat) into a proper
; Setup.exe that:
;   - Installs to C:\Program Files\Boostly Tweaks
;   - Creates a Start Menu shortcut
;   - Creates a Desktop shortcut
;   - Optionally installs MSI Afterburner via winget (real winget package,
;     fetched live from Guru3D's own source at install time - nothing
;     bundled in this repo)
;   - Optionally opens NVIDIA's official NVIDIA App download page - the new
;     NVIDIA App isn't in the winget repository yet (blocked by NVIDIA's own
;     hardware-validation requirements as of writing - see
;     github.com/microsoft/winget-pkgs/issues/140696), so a direct silent
;     install isn't possible; this is the honest alternative instead of
;     guessing at a fragile direct-download URL that goes stale every release
;   - Launches the app automatically when setup finishes
;
; HOW TO BUILD:
;   1. Run build_exe.bat first (creates dist\BoostlyTweaks.exe)
;   2. Open this file in Inno Setup Compiler (double-click it once Inno Setup is installed)
;   3. Click Build > Compile (or press Ctrl+F9)
;   4. Your installer appears in the Output\ folder as BoostlyTweaks-Setup.exe

#define MyAppName "Boostly Tweaks"
#define MyAppVersion "1.1.0"
#define MyAppPublisher "Boostly Tweaks"
#define MyAppExeName "BoostlyTweaks.exe"

[Setup]
AppId={{6A0CB70F-0E13-4D78-93D0-A2C26AD166CD}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputDir=Output
OutputBaseFilename=BoostlyTweaks-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
; Installer itself needs admin to write to Program Files
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"
Name: "installafterburner"; Description: "Install MSI Afterburner (via winget - GPU monitoring/overclocking)"; GroupDescription: "Optional companion apps:"; Flags: unchecked
Name: "opennvidiaapp"; Description: "Open the NVIDIA App download page after setup"; GroupDescription: "Optional companion apps:"; Flags: unchecked

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; winget ships built-in on Windows 10 1809+ and Windows 11. If it's missing (rare, usually
; only on very minimal/older installs), this step just fails quietly - Flags: skipifdoesntexist
; and the "ignore exit code" behavior of runhidden keep setup from halting because of it.
Filename: "{cmd}"; Parameters: "/C winget install --id Guru3D.Afterburner -e --silent --accept-package-agreements --accept-source-agreements"; \
    StatusMsg: "Installing MSI Afterburner..."; Tasks: installafterburner; Flags: runhidden

Filename: "{cmd}"; Parameters: "/C start https://www.nvidia.com/en-us/software/nvidia-app/"; \
    Tasks: opennvidiaapp; Flags: runhidden postinstall

Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
