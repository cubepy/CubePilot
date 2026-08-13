# Installation

CubePilot is distributed **only** through
[GitHub Releases](https://github.com/cubepy/CubePilot/releases). Do not install
a build from anywhere else — you would be handing your SSH keys to a stranger.

Every release publishes exactly two files:

| File | Platform |
| --- | --- |
| `CubePilot-vX.Y.Z-android.apk` | Android 8.0 (API 26) and newer |
| `CubePilot-vX.Y.Z-windows-x64.zip` | 64-bit Windows 10 1809 and newer |

There is no installer, no MSIX and no store listing. Anything else claiming to
be CubePilot is not.

---

## Android

1. Open the [latest release](https://github.com/cubepy/CubePilot/releases/latest)
   on your phone and download the `.apk`.

   Releases carry one APK per processor type, because a single universal
   file is nearly three times the size for no benefit to anyone:

   | File | For |
   |---|---|
   | `…-arm64-v8a.apk` | **Almost every phone.** Anything sold since roughly 2016. Start here. |
   | `…-armeabi-v7a.apk` | Older or very cheap 32-bit phones. Use this only if the arm64 file refuses to install. |
   | `…-x86_64.apk` | Emulators and Chromebooks. Not a phone. |

   If the wrong one is picked, Android refuses it at install time with
   "App not installed" rather than installing something broken.

2. Tap the downloaded file. Android will ask you to allow installing apps from
   this source; grant it for your browser or file manager, then tap the file
   again.

3. Play Protect will warn you, because the app is not distributed through the
   Play Store. That warning is about the *distribution channel*, not about
   anything found in the app. **Install anyway** is safe *if* you downloaded
   from this repository and the checksum matches — see below.

### Updating

Download the newer APK and install it over the existing app. Your servers,
keys and timeline are preserved.

**Never uninstall first.** Uninstalling wipes the encrypted database and the
key that opens it, and no update needs you to.

---

## Windows

The Windows build is portable. There is nothing to install.

1. Download the `.zip` from the
   [latest release](https://github.com/cubepy/CubePilot/releases/latest).
2. Extract it. Everything sits inside a single `CubePilot` folder, so
   extracting onto your desktop leaves one folder rather than forty loose
   files.
3. Run `cubepilot.exe` inside that folder.

SmartScreen will likely show *"Windows protected your PC"*: the executable is
unsigned, and an unsigned binary has no reputation with Microsoft. Verify the
checksum first (below), then **More info → Run anyway**.

Keep the folder together — the `.exe` needs the DLLs and the `data` directory
beside it.

### Where your data lives

Not in that folder. The encrypted vault is written to

```
%APPDATA%\top.cubesystem\cubepilot
```

so it survives replacing the program folder with a newer one, which is how you
update: extract the new zip over the old folder, or delete the old folder and
extract the new one. Either way your servers and keys stay where they are.

Copying the program folder to a USB stick therefore does **not** carry your
servers with it. Use **Settings → Backup → Export** for that.

### Uninstalling

Delete the folder. To remove your data as well, delete the `%APPDATA%` path
above — export a backup first if you might want it back.

---

## Verifying your download

Every release lists the SHA-256 of both files at the bottom of its release
notes, under **Checksums**.

**Windows (PowerShell):**

```powershell
Get-FileHash .\CubePilot-v0.1.14-windows-x64.zip -Algorithm SHA256
```

**Linux / macOS / Android (Termux):**

```sh
sha256sum CubePilot-v0.1.14-android.apk
```

Compare the output with the release notes, ignoring case. If it does not
match, delete the file and download it again. If it still does not match,
[tell us](https://github.com/cubepy/CubePilot/issues/new/choose) — and do not
install it.

The APK is also signed with a release key that does not change between
versions. That is what lets an update install over the previous build: if a
`.apk` claiming to be CubePilot refuses to install over yours, it was signed by
someone else, and that is worth reporting rather than working around.

---

## First run

1. Pick your language and theme during onboarding.
2. Set an app lock — fingerprint, Windows Hello or PIN — and an auto-lock
   timeout. Do this before you add a single credential.
3. Add your first server, or import an existing key from
   **SSH Keys → Import**.
4. Once you have a setup worth keeping, go to **Settings → Backup → Export**
   and store the encrypted backup somewhere safe.

---

## Android and background sessions

CubePilot runs a foreground service while a session is open, which is what
keeps SSH connections alive when the app is not in front of you. You will see a
notification for as long as at least one session exists; it disappears with the
last one.

Some manufacturers — Xiaomi, Samsung, Huawei, OnePlus among them — kill
background apps aggressively regardless. If sessions still die while you are in
another app, find CubePilot in your system battery settings and set it to
**unrestricted**.

---

Something went wrong? See [troubleshooting.md](troubleshooting.md).
