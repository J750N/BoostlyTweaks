# Boostly Tweaks

A free, beginner-friendly Windows tuning tool. Every tweak is explained in
plain English, shows you the PC default vs. the recommended value, and can be
undone with one click.

## Download & Run

**[⬇ Download the latest release](https://github.com/J750N/BoostlyTweaks/releases/latest)**

1. Download `BoostlyTweaks.exe` from the Releases page above
2. Run it. If Windows shows a "Windows protected your PC" SmartScreen
   warning, click **More info → Run anyway** (the exe just isn't
   code-signed)
3. Click **Yes** when it asks for administrator access, so tweaks can be
   applied

No Python, no installer, no dependencies. Everything is bundled inside the
exe.

**Before your first tweaking session**, open the **Backup** page and click
**Create Restore Point**.

## Features

- **Home**: live CPU, memory and disk graphs, PC specs, recent changes and
  quick actions
- **Tweak categories**: Core, Privacy, Power, Network, Explorer & UI,
  Storage, Services and Advanced, each with its own sidebar page
- **Services**: background Windows services split into "Safe" and
  "Advanced" groups
- **Gaming**: detects your GPU/CPU, one-click launches into NVIDIA App, AMD
  Adrenalin, Intel Graphics Center and MSI Afterburner, imports NVIDIA
  driver profiles, plus gaming and input tweaks
- **Debloat**: remove pre-installed Windows apps, with a Reinstall button if
  you change your mind
- **Install Apps**: one-click installs of common apps (Chrome, Discord,
  Steam, VLC and more)
- **History**: every change is logged with a one-click Revert / Re-Apply
- **Backup**: System Restore Points or registry exports
- **Fixes**: one-click repairs for network, audio, Windows Update, SFC/DISM,
  temp files, Bluetooth and clipboard
- **System Info**: a clear rundown of your hardware and software
- **Settings**: 10 theme presets, launch with Windows, restart prompts and a
  health scan

Every tweak shows a risk dot (🟢 safe / 🟡 moderate / 🔴 risky), a hover
tooltip explaining what it does, and its default vs. recommended value.

## Optional: NVIDIA Profile Inspector

The Gaming page can import NVIDIA driver profiles using the free
[nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector).
Download it, then point to it in **Settings → System Tools**.

## Safety

- Nothing is downloaded or run from the internet behind your back
- Every change is logged in **History** and can be reverted
- There's no automatic GPU/CPU overclocking. The Gaming page links you to
  the vendors' own tools instead, which are built to do that safely

## License

MIT. See [LICENSE](LICENSE).
