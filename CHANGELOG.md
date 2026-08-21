# Changelog

All notable changes to CubePilot are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Every entry corresponds to a build published on the
[Releases](https://github.com/cubepy/CubePilot/releases) page.

## [Unreleased]

Work in progress is tracked in [docs/roadmap.md](docs/roadmap.md).

## [0.2.1] - 2026-08-21

Your servers on the home screen, a terminal that floats over other apps, and
the version the app shows is now the version it is.

### Added
- A home-screen widget: the servers you use, one tap from the launcher —
  pinned first, then favourites, then most recently connected. It holds a
  name and an internal id and nothing else: no host, no username, no port,
  no key, no password, so nothing in it can reach a machine. With the app
  lock on it lists nothing at all.
- A Quick Settings tile, landing on the dashboard with quick connect
  focused. It connects to nothing on its own on purpose — a tile can be
  tapped over a lock screen.
- A floating terminal: shrink a session into a small window that stays on
  top of other apps. Output only, no input, because a floating window has no
  keyboard and a stray tap that reached a root shell would be a bad way to
  find that out.
- "Connect outside the VPN" now does something. The setting has existed
  since v0.2 and the Android side of it was never written, so it answered
  "not supported" on every device.
- The version, faintly, beside the Dashboard title — the first question of
  every bug report, previously four taps deep in Settings.

### Fixed
- Shell prompts are coloured, all of them. v0.2 coloured the first prompt of
  a session and no others: a prompt is alone only once, and from the second
  one on it arrives inside a complete line with the command you just typed
  after it.
- Every filled button was under the contrast standard. White on the brand
  blue was 4.42:1 and on the brand purple 4.23:1, against WCAG AA's 4.5:1.
  Both colours are one step deeper now.
- Tapping a row in Settings looked like nothing happened — the ripple was
  painted behind the card it was meant to appear on.
- About said 0.2.0 in every build since 0.1.0, and called itself a
  pre-release regardless of how the release was published. Both come from
  one constant now, checked against `pubspec.yaml` by a test.

### Changed
- Every screen is run through Flutter's accessibility guidelines on every
  build: tap-target size, labelled controls, text contrast in both themes,
  right-to-left layout and the largest system font. The two fixes above are
  what the first run found.

## [0.2.0] - 2026-08-13

Two things found by using v0.1.17 rather than by reading it.

### Fixed
- The last server in a full list sat behind the floating Add button and could
  not be tapped at all. Servers, tunnels, keys, commands and the timeline all
  leave room for the button now.
- Shell prompts are coloured — this time actually. The colouring shipped in
  v0.1.17 and never once fired on a real server: a shell does not send a
  prompt on its own. bash turns on bracketed-paste mode first and the stock
  PS1 sets the window title, so a prompt always arrives with control
  sequences in front of it — and anything carrying an escape was left alone
  as output something had already coloured.

## [0.1.17] - 2026-08-13

No new features. Eighteen rounds of one question asked over and over: does
this screen tell the truth, and does this button do what it says?


### Fixed — things that could lose something
- Two saves landing at once could destroy the whole vault. Every save wrote
  the store to one temporary file and renamed it into place, with nothing
  keeping two of them apart — and the timeline records an entry, without
  waiting for it, on every command, connection and file transfer. When they
  overlapped, what ended up as the vault was half a JSON document, which the
  next launch could only read as corrupt: set aside, start empty. Saves now
  run one at a time.
- Restoring a backup asked nothing and replaced everything — every server,
  key, tunnel, saved command, group and the whole timeline, including private
  keys that exist nowhere else. It now decrypts first and then asks, showing
  what is on the device, what is in the file, and that keys do not come back.
- When the vault could not be read, the app said nothing: it set the file
  aside and opened empty, which is indistinguishable from having thrown your
  servers away. It now says what happened and where the old file is. If the
  store cannot be opened at all, it says that too.
- Installing an older build over a newer one would have dropped everything
  the newer one added, on its first save. Unknown fields are carried through
  untouched now.

### Fixed — things that ran on the wrong machine
- Docker and Kubernetes actions re-resolved the active session at the moment
  they ran, rather than using the one the list came from. Containers have
  random ids so those mostly missed; volumes and networks are addressed by
  name, and `db_data` exists on staging and on production. Actions are pinned
  to the list's session now, and both pages finally say which machine they
  are showing.
- The command library fires at whichever session is active and said only
  "Ran X" afterwards. It names the machine before you tap anything now.
- A log follow survived switching servers, printing one server's lines into a
  page that belonged to another. The log export named the wrong server in its
  header for the same reason.

### Fixed — SFTP
- After a reconnect the file browser was talking to a socket that no longer
  existed, for every listing, upload and delete, until the app was restarted.
- Rename, delete, mkdir and chmod returned quietly when the session was gone:
  renaming a file on a closed session looked exactly like success.
- Two panes showing the same session were the same pane.
- Downloads and uploads held the whole file in memory, and downloads asked
  where to save only after transferring. Both stream now, and an upload that
  would replace a file asks first.

### Fixed — security
- The app lock counted nothing: a four-digit PIN is ten thousand guesses and
  none of them cost anything. Five wrong now starts a wait that doubles.
- A vault saying the lock is on with no PIN stored no longer locks you out of
  your own data permanently.
- The CSV timeline export was executable: spreadsheets read a field starting
  with `=` as a formula, and those fields hold whatever a server printed.
- A changed host key showed only the new fingerprint — not the old one it did
  not match. Fingerprints now print the way `ssh` prints them.
- Closing a session takes its tunnels with it, and says so first.
- A connection failure reported the phone's own ephemeral port where a reader
  expects the port that was dialled, because that is what Dart's
  SocketException text contains. Failures now name what was being reached —
  the server, the proxy in front of it, or a named jump host — and say why in
  words rather than an errno.

### Better
- Selecting text works where the text is: a bar appears over the terminal the
  moment something is selected. Right-click copies a selection or pastes when
  there is none.
- Shell prompts are coloured — the one line the highlighter could never touch,
  and the only landmark when scrolling back through a long session.
- Imported keys carry a fingerprint and a public key, derived from the key
  itself, so they can be told apart and pasted into `authorized_keys`.
- A jump-host loop is caught when the server is saved, not weeks later.
- Deleting a note or a bookmarked timeline entry asks first.
- Launch is about two and a half seconds shorter, and the system splash hands
  over to the app's own without the logo jumping.
- A per-server "connect outside the VPN" switch on Android. The platform half
  is not in this build, and a session set to use it says so rather than
  pretending.

## [0.1.16] - 2026-08-08

### Fixed
- Deleting a server asked nothing and cleaned up nothing: its open session
  kept running with its tab and notification, and its saved tunnels stayed in
  the vault unstartable. It now confirms first, naming how many sessions,
  tunnels and dependent jump hosts are attached to that server, and closes
  and deletes what belonged to it.
- Deleting a private key asked nothing either — one tap, no confirmation, for
  the one thing that cannot be recovered. It now confirms, and says how many
  servers authenticate with it.
- A tunnel whose session closed stayed listed as running with its local port
  still bound, which made starting a replacement on the same port fail.
  Sessions now stop the tunnels they carry.
- The dashboard's tunnel counter was a hardcoded zero and had been since the
  first release. All three counters now also open the screen they count.

## [0.1.15] - 2026-08-08

### Added
- **Jump hosts** — a server can be reached through another saved server, and
  through chains of up to four. CubePilot forwards a channel through the
  bastion and runs the real connection down it, so the traffic stays
  encrypted end to end. A hop authenticates with its own credentials and gets
  the same host-key checking as anything else. A deleted jump host is an
  error rather than a silent direct connection, and servers pointing at each
  other in a loop are reported as one.

### Changed
- The documentation was brought in line with what actually ships: the
  installation page described an `.exe` installer, an `.msix` and per-ABI
  APKs that have never existed, and said no public build was available.

## [0.1.14] - 2026-08-08

### Added
- **Material You** — on Android 12 and later, CubePilot can take its accent
  colours from the system wallpaper palette. Off by default, and a switch
  under the theme list rather than a fifth theme, since it applies to
  whichever theme is chosen. Only the accents follow the wallpaper: the
  surfaces stay as they are so a dark theme stays dark and OLED stays black,
  and error red stays CubePilot's in every theme.

## [0.1.13] - 2026-08-08

### Fixed
- Icon-only keys in the terminal key bar announced nothing to a screen
  reader; each now carries a label.
- A monitoring reading is announced once — "CPU, 34%" — instead of as three
  unrelated fragments, and the sparklines are hidden from screen readers
  since they repeat the number above them.
- A server in the list is announced as one item rather than a name, an
  address, tags and icons separately.
- The terminal's tab strip clipped its labels at large system text sizes.

## [0.1.12] - 2026-08-08

### Changed
- The Glass theme now shares one backdrop blur across every card on screen
  instead of blurring the screen once per card, so the cost no longer grows
  with the length of a list.
- Terminal output was held for one frame at 60 Hz before being drawn, capping
  what a 120 Hz display could show. The hold is now one frame at 120.
- Charts and terminal views paint on their own layers, so a new sample or an
  incoming byte no longer repaints the card and page around them.

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
