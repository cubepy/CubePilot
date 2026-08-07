<div align="center">

<img src="assets/logo/cubepilot-logo.svg" alt="CubePilot" width="420">

### Free. Professional. Cross Platform.

A modern workspace for managing all of your servers — SSH, SFTP, Docker, Kubernetes, tunnels and monitoring in one app, for **Android** and **Windows**.

[![Status](https://img.shields.io/badge/status-in%20development-8B5CF6?style=for-the-badge)](docs/roadmap.md)
[![Latest release](https://img.shields.io/github/v/release/cubepy/CubePilot?style=for-the-badge&color=3B6EF6&label=latest)](https://github.com/cubepy/CubePilot/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/cubepy/CubePilot/total?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/releases)
[![Platforms](https://img.shields.io/badge/platforms-Android%20%7C%20Windows-3B6EF6?style=for-the-badge)](docs/installation.md)
[![License](https://img.shields.io/badge/license-Freeware%20EULA-8B5CF6?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/cubepy/CubePilot?style=for-the-badge&color=22D3EE)](https://github.com/cubepy/CubePilot/stargazers)

**[فارسی](README-fa.md)** · [Download](#-download) · [Features](#-features) · [Roadmap](docs/roadmap.md) · [FAQ](docs/faq.md) · [Discussions](https://github.com/cubepy/CubePilot/discussions)

</div>

---

> **Heads-up:** CubePilot is under active development and has not shipped its first public build yet. This repository is where releases, documentation and issue tracking will live. Watch 👁 or Star ⭐ the repo to be notified when `v0.1.0` lands.

---

## 🧊 What is CubePilot?

Most SSH clients hand you a terminal and stop there. CubePilot is built around a different idea: your servers deserve a **workspace**, not a connection dialog.

Open the app and you land on a dashboard — how many servers you have, which are online, what you touched last, which tunnels are live. From there you're one keystroke away from a terminal, a file transfer, a container restart, or the full history of everything that has ever happened on a machine.

CubePilot is **completely free**, with no accounts, no subscriptions, no telemetry and no paywalled features. It is **closed source**, so this repository contains documentation and releases only — never source code.

## 🕒 Server Timeline — the signature feature

This is the part no other SSH client gets right.

Every server in CubePilot keeps a **complete, searchable timeline of its own history**:

- First connection and last connection
- Every session, with its duration
- Commands you ran
- Files uploaded and downloaded over SFTP
- Permission changes
- Services and Docker containers you restarted
- Tunnels created and torn down
- Important errors and status changes
- Your own notes, pinned to the moment you wrote them

Search it, filter it, tag it, bookmark it. Three weeks later, when something breaks, you no longer have to remember what you did — you scroll back and read it.

## ✨ Features

<details open>
<summary><b>Terminal</b></summary>

Multi-tab sessions · split view · session manager · in-terminal search · bookmarks · copy mode · paste history · command palette · zoom · professional color schemes · font and cursor selection
</details>

<details>
<summary><b>Server management</b></summary>

Rich server cards showing OS, country, IP, ping, CPU, RAM, disk, uptime, online status, last connection and tags · search · folders · workspaces · smart groups · favorites · pinning
</details>

<details>
<summary><b>SFTP file manager</b></summary>

Dual-pane layout · drag & drop · upload and download · rename, delete and edit in place · permission editor · file preview · folder size calculation · search
</details>

<details>
<summary><b>Docker</b></summary>

Containers, images, networks and volumes · start, stop and restart · live logs · shell into a container · resource stats · delete
</details>

<details>
<summary><b>Kubernetes</b></summary>

Pods, deployments, services, namespaces, ConfigMaps and secrets · logs · exec terminal
</details>

<details>
<summary><b>Port forwarding</b></summary>

Local forward · remote forward · dynamic SOCKS5 · HTTP proxy · saved and managed tunnels
</details>

<details>
<summary><b>Monitoring</b></summary>

Live CPU, RAM, disk, network, temperature, bandwidth, ping, uptime and load average, with clean charts
</details>

<details>
<summary><b>Command library & snippets</b></summary>

Save the commands you actually use — restart Nginx, restart Docker, update the system, run a backup, git pull, deploy — and fire them with one tap. Ships with a ready-made snippet library for SSH, Git, Docker, Kubernetes, Nginx and Linux.
</details>

<details>
<summary><b>Log viewer</b></summary>

Syntax-colored log output · search · regex · bookmarks · export
</details>

<details>
<summary><b>SSH key manager</b></summary>

RSA, ED25519 and ECDSA · import, export and generate · fingerprint display · passphrase support · keys held in the platform's secure storage
</details>

<details>
<summary><b>Security</b></summary>

Fingerprint unlock · Windows Hello · PIN · auto-lock · encrypted local database · secure key vault
</details>

<details>
<summary><b>Backup, no account required</b></summary>

Export and import an encrypted backup file. Your data stays yours — there is no CubePilot cloud, and nothing is uploaded anywhere.
</details>

### Platform-native touches

| Android | Windows |
| --- | --- |
| Material You with dynamic color | Fluent Design |
| Home-screen widget | Mica and Acrylic surfaces |
| Quick Settings tile | Tray icon |
| Floating terminal | Global shortcut |
| Session notification | Multi-window |
| Split-screen support | Multi-monitor support |

## 🎨 Design

Dark, Light, OLED and Glass themes built on a blue → purple palette with a cyan accent. Glassmorphism, acrylic blur, floating cards, soft shadows, and animations that stay smooth at 120 Hz on displays that support it.

## 📥 Download

All builds are published through **[GitHub Releases](https://github.com/cubepy/CubePilot/releases)** — that is the only official distribution channel.

| Platform | File | Requirement |
| --- | --- | --- |
| Android | `.apk` | Android 8.0 (API 26) or newer |
| Windows | `.exe` installer / `.msix` | Windows 10 1809 or newer, 64-bit |

Step-by-step instructions, including how to install an APK outside the Play Store and how to handle the SmartScreen prompt on Windows, are in **[docs/installation.md](docs/installation.md)**.

> Download CubePilot only from this repository's Releases page. Builds from anywhere else are not ours and are not safe to trust with your SSH keys.

## 📸 Screenshots

Screenshots and the introduction video will be added here with the first public release. We would rather show you the real app than a mockup.

## 🗺 Roadmap

See **[docs/roadmap.md](docs/roadmap.md)** for what is planned and what is being worked on right now.

## 📝 Changelog

Every released version is documented in **[CHANGELOG.md](CHANGELOG.md)**.

## 🐞 Reporting a bug

1. Search [existing issues](https://github.com/cubepy/CubePilot/issues?q=is%3Aissue) first — someone may have hit it already.
2. Open a **[Bug report](https://github.com/cubepy/CubePilot/issues/new/choose)** and fill in the template: app version, platform, OS version, steps to reproduce.
3. **Never paste an SSH private key, password, passphrase or a real server IP into an issue.** Replace them with placeholders. See [SECURITY.md](SECURITY.md) for how to report a security problem privately.

Stuck on something that may not be a bug? Try **[docs/troubleshooting.md](docs/troubleshooting.md)** first.

## 💡 Suggesting a feature

Open a **[Feature request](https://github.com/cubepy/CubePilot/issues/new/choose)**, or start a thread in **[Discussions → Ideas](https://github.com/cubepy/CubePilot/discussions)** if you want to talk it through before it becomes a formal request. Tell us the problem you're hitting, not only the solution you have in mind — it usually leads to a better feature.

## 📄 License

CubePilot is free to use, personally and commercially, under a proprietary end-user license. The source code is not published. See **[LICENSE](LICENSE)**.

---

<div align="center">

Part of the **Cube** ecosystem · [cubesystem.top](https://cubesystem.top)

</div>
