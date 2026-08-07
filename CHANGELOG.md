# Changelog

All notable changes to CubePilot are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Every entry corresponds to a build published on the
[Releases](https://github.com/cubepy/CubePilot/releases) page.

## [Unreleased]

Work in progress toward `v0.2.0` is tracked in [docs/roadmap.md](docs/roadmap.md).

## [0.1.0] - 2026-08-07

First public beta, for Android and Windows.

### Added
- **Server Timeline** — per-server history of connections, session durations,
  commands, file transfers, permission changes, tunnel lifecycle and errors,
  with search, filters, tags, bookmarks and notes pinned to any moment.
- **Terminal** — multi-tab sessions, 256-colour support, selectable font size
  and colour scheme, and client-side syntax highlighting of plain server
  output: URLs, IPs, paths, sizes, permission bits, versions, timestamps,
  quoted strings and status keywords.
- **Servers** — folders, favourites, pinning, search and tags, with per-server
  HTTP and SOCKS5 proxy support for hosts that cannot be reached directly.
- **SFTP** — browse, upload, download, rename, delete and edit permissions.
- **Tunnels** — local, remote and dynamic SOCKS5 port forwarding, saved and
  managed.
- **Command library** — 26 built-in snippets for Linux, Nginx, Docker, Git,
  Kubernetes and SSH, plus your own, each runnable in the active session.
- **SSH keys** — generate and import RSA, ED25519 and ECDSA, with passphrases
  and fingerprints, held in the platform's secure storage.
- **Security** — AES-256-GCM encrypted vault with the master key in the
  platform keystore, biometric and PIN lock with auto-lock, host key
  verification, and encrypted backup export and import.
- **Background sessions** — an Android foreground service keeps sessions alive
  while the app is not in the foreground.
- English and Persian, with full RTL.

### Known limitations
- The Windows build is unsigned and portable; SmartScreen warns on first run
  and there is no installer yet.
- The Android build is sideloaded, so Play Protect warns on install.
- Aggressive battery management on some devices can still kill background
  sessions unless CubePilot is set to unrestricted.
- Docker, Kubernetes and monitoring are not in this release.

---

<!--
Template for each release — copy this block above when cutting a version.

## [X.Y.Z] - YYYY-MM-DD

### Added
### Changed
### Fixed
### Removed
### Security
-->
