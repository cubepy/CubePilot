# Changelog

All notable changes to CubePilot are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Every entry corresponds to a build published on the
[Releases](https://github.com/cubepy/CubePilot/releases) page.

## [Unreleased]

Work in progress is tracked in [docs/roadmap.md](docs/roadmap.md).

## [0.1.11] - 2026-08-08

### Added
- **Smart groups** — rule-based views over the server list (name, host, tag,
  folder, user, port, favourite, pinned, last used within N days), matching
  all rules or any of them, with a live count of what they match while you
  edit. Favourites and Recent are built in and need no setup.
- **Connect all** — with a group selected, one button opens every server
  listed under it, sequentially, reporting how many of how many opened.

## [0.1.10] - 2026-08-08

### Added
- **Network throughput** on the dashboard, summed across every interface
  except loopback, with the rate divided by the time that actually elapsed
  rather than by the poll interval.
- **Temperature** — the warmest thermal zone the kernel exposes, red past
  80°C, and absent entirely on machines that expose none.
- **Charts** — a sparkline of the last two minutes under CPU, memory and the
  link, drawn directly rather than with a charting dependency.

## [0.1.9] - 2026-08-08

### Added
- **Docker images, networks and volumes**, each with a delete button. Images
  show their size and age, and a dangling one is shown dimmed by its id.
- **Live CPU, memory and network per running container**, fetched with the
  list. A daemon that will not report stats costs you the numbers, not the
  screen, and a container with no reading yet shows nothing rather than 0%.

## [0.1.8] - 2026-08-08

### Added
- **Kubernetes** — pods, deployments, services, ConfigMaps and Secrets for
  whatever cluster the connected server can reach, in one namespace or all of
  them. Pod logs, a shell inside a pod, delete a pod, rollout restart and
  scale a deployment. `kubectl` runs on the server, using the kubeconfig it
  already has, so no cluster credential is kept on the phone. Secrets are
  listed by name and type only — their values are never requested.

## [0.1.7] - 2026-08-08

### Added
- **Log viewer** — the systemd journal, the usual files under `/var/log`,
  `dmesg`, or any path you type, read once or followed live over the
  connection already open. Lines are coloured by severity, read from a
  declared field, a bracketed level, a bare word, or the status code of an
  access line. Filter literally or with a regular expression, with a severity
  filter alongside; an expression that does not compile says why. Bookmark
  lines by their number, filter to just the marks, and export exactly what is
  on screen.

## [0.1.6] - 2026-08-08

### Added
- **Split view** — a second terminal beside the first, side by side or stacked
  depending on the window, with a draggable divider and a coloured border on
  the pane the keyboard is going to.
- **Sessions** — one list of every open connection: what it is, how long it
  has been up, whether it is still reconnecting, and which pane it is in, with
  reconnect, open-beside, and close-all-disconnected.

### Fixed
- Attaching a file announced `Uploading $name…` literally instead of the file
  name, in both languages.

## [0.1.5] - 2026-08-08

### Added
- **Live monitoring** on the dashboard — CPU, memory and disk as bars, with
  load average, uptime, hostname and distribution, read over the connection
  you already have. CPU appears on the second sample rather than claiming 0%,
  and `MemAvailable` falls back to free + buffers + cached on older kernels.

## [0.1.4] - 2026-08-08

### Added
- **Docker** — a server's containers, running and stopped, with start, stop,
  restart, remove, logs and a shell into a running container, over the SSH
  connection already open.

### Fixed
- The Windows zip put every file at its root, so extracting it onto the
  desktop scattered thirty-odd DLLs across it. Everything now sits inside a
  single `CubePilot` folder.

## [0.1.3] - 2026-08-08

### Added
- **Text selection** — the session's output as ordinary selectable text, which
  brings Android's own handles, magnifier, word and paragraph selection and
  copy menu, plus a copy-all button.

### Fixed
- The arrow keys were pushed off the right edge of the key bar on narrow
  phones. The row is now ordered by how often a key is actually pressed.

## [0.1.2] - 2026-08-08

### Added
- **Copy and paste** in the terminal, with bracketed paste so a multi-line
  paste arrives as text instead of executing itself a line at a time.
- **A key bar above the keyboard** — Esc, Tab, Ctrl, Alt and the arrows, and a
  second row with Home, End, PgUp, PgDn and the characters a phone buries.
- **Search a session's output**, every hit with its line number.
- **A command palette** on `Ctrl+K`, over every screen, server and saved
  command.
- **Timeline export** as Markdown, CSV or JSON, exporting what your filters
  have left on screen.

### Fixed
- The notification icon rendered as a white blob; Android draws small icons as
  silhouettes, so it now ships a proper monochrome glyph.

## [0.1.1] - 2026-08-07

### Fixed
- **Sessions reconnect themselves.** A WiFi handover, a sleeping phone or a
  server-side timeout used to close the tab and take the scrollback with it.
  The session now stays put and reconnects in place, with backoff, and refuses
  a host key that changed while it was away.

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
