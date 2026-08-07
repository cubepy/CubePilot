# Installation

CubePilot is distributed **only** through
[GitHub Releases](https://github.com/cubepy/CubePilot/releases). Do not install
a build from anywhere else — you would be handing your SSH keys to a stranger.

> No public build exists yet. This page describes how installation will work
> once `v0.1.0` is released. Watch 👁 the repository to be notified.

---

## Android

**Requirements:** Android 8.0 (API 26) or newer, arm64 or armeabi-v7a.

1. Open the [latest release](https://github.com/cubepy/CubePilot/releases/latest)
   on your phone.
2. Under **Assets**, download the `.apk`. If several are listed, pick the one
   matching your device's ABI; `arm64-v8a` is correct for nearly every phone
   made since 2016. A universal APK is also published if you are unsure.
3. Tap the downloaded file. Android will ask you to allow installing apps from
   this source — grant it for your browser or file manager, then go back and
   tap the file again.
4. Play Protect may show a warning because the app is not distributed through
   the Play Store. **Install anyway** is safe *if* you downloaded from this
   repository and the checksum matches (see below).

### Updating

Download the newer APK and install it over the existing app. Your servers,
keys and timeline are preserved. Never uninstall first — that wipes the
encrypted database.

---

## Windows

**Requirements:** Windows 10 version 1809 or newer, 64-bit.

### Installer (`.exe`)

1. Download the `.exe` from the
   [latest release](https://github.com/cubepy/CubePilot/releases/latest).
2. Run it. SmartScreen will likely show *"Windows protected your PC"* — new
   publishers have no reputation with Microsoft until enough people have
   installed the app.
3. Before clicking through: click **More info** and confirm the publisher, and
   verify the checksum (below). If either looks wrong, stop.
4. Click **More info → Run anyway**.

### Package (`.msix`)

Double-click the `.msix` and confirm. Installing a signed MSIX may require
trusting the certificate first; the release notes for each build spell out the
exact steps for that build.

### Portable build

If a portable `.zip` is published, extract it anywhere and run
`CubePilot.exe`. It stores its data alongside the executable, so it works from
a USB drive — with the obvious caveat that an encrypted database on a stick you
can lose is only as safe as the passphrase on it.

---

## Verifying your download

Every release publishes a `SHA256SUMS.txt` file listing the checksum of each
artifact.

**Windows (PowerShell):**

```powershell
Get-FileHash .\CubePilot-Setup.exe -Algorithm SHA256
```

**Linux / macOS / Android (Termux):**

```sh
sha256sum CubePilot.apk
```

Compare the output against `SHA256SUMS.txt`. If it does not match, delete the
file and download it again. If it still does not match,
[tell us](https://github.com/cubepy/CubePilot/issues/new/choose) — do not
install it.

---

## First run

1. Pick your language and theme during onboarding.
2. Set an app lock — fingerprint, Windows Hello or PIN — and an auto-lock
   timeout. Do this before you add a single credential.
3. Add your first server, or import an existing key from
   **SSH Keys → Import**.
4. Once you have a setup you care about, go to **Settings → Backup → Export**
   and store the encrypted backup somewhere safe.

---

## Uninstalling

**Android:** uninstall from Settings → Apps as usual.
**Windows:** Settings → Apps → CubePilot → Uninstall.

Both remove the encrypted local database along with the app. Export a backup
first if you want your servers, keys and timeline back later — there is no
cloud copy to restore from.

---

Something went wrong? See [troubleshooting.md](troubleshooting.md).
