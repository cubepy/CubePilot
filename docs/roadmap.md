# Roadmap

What CubePilot is being built toward, roughly in the order it is being built.

This is a direction, not a delivery contract — items move between milestones
as they turn out to be harder, easier, or less useful than expected. Dates are
deliberately absent; a milestone ships when it is good enough to ship.

**A ticked box means built and working — not released.** Nothing has been
published yet; the first public build lands when the last open v0.1.0 item
does.

Want something here that isn't? Open a
[Feature request](https://github.com/cubepy/CubePilot/issues/new/choose) or
bring it up in [Discussions](https://github.com/cubepy/CubePilot/discussions).

---

## v0.1.0 — First public beta

The smallest version that is genuinely useful every day.

- [x] Splash, onboarding and the dashboard
- [x] Server management: add, edit, delete, search, folders, favorites, pinning
- [x] SSH terminal with multi-tab sessions, professional color schemes, font
      and cursor selection
- [x] SSH key manager — RSA, ED25519, ECDSA; import, generate, fingerprint,
      passphrase
- [x] Encrypted local database and secure key vault
- [x] App lock: fingerprint, Windows Hello, PIN, auto-lock
- [x] Dark, Light and OLED themes
- [x] English and Persian, with full RTL support
- [x] Encrypted backup export and import
- [ ] Android and Windows builds published on Releases

## v0.2.0 — Files and tunnels

- [x] SFTP file manager: dual-pane, drag & drop, upload, download, rename,
      delete, in-place edit, permissions, preview, folder size, search
- [x] Port forwarding: local, remote, dynamic SOCKS5 and HTTP proxy, with
      saved tunnels
- [ ] Split terminal view and the session manager
- [ ] Command palette
- [x] Command library and the built-in snippet collection

## v0.3.0 — Server Timeline

CubePilot's signature feature, and the reason the app exists.

- [x] Per-server activity timeline: connections, session durations, commands,
      file transfers, permission changes, service and container restarts,
      tunnel lifecycle, errors, status changes
- [x] Notes attached to any point on the timeline
- [x] Search, filter, tag and bookmark across every event
- [ ] Timeline export

## v0.4.0 — Containers and orchestration

- [ ] Docker: containers, images, networks, volumes; start, stop, restart,
      logs, shell, stats, delete
- [ ] Kubernetes: pods, deployments, services, namespaces, ConfigMaps,
      secrets, logs, exec terminal
- [ ] Log viewer with syntax coloring, regex search, bookmarks and export

## v0.5.0 — Monitoring and polish

- [ ] Live monitoring: CPU, RAM, disk, network, temperature, bandwidth, ping,
      uptime, load average, with charts
- [ ] Smart groups and workspaces
- [ ] Glass theme
- [ ] Animation and performance pass targeting 120 fps on supported displays

## v1.0.0 — Platform integration

- [ ] Android: Material You dynamic color, home-screen widget, Quick Settings
      tile, floating terminal, session notification, split-screen
- [ ] Windows: Fluent Design, Mica and Acrylic, tray icon, global shortcut,
      multi-window, multi-monitor
- [ ] Full accessibility pass
- [ ] Stable release

---

## Under consideration

Not committed to, but on our minds:

- Linux and macOS builds
- Mosh support
- Jump hosts and bastion chains
- Agent forwarding
- Serial console
- Team backup sharing that still requires no account

## Explicitly not planned

- User accounts or a mandatory login
- A cloud sync service that holds your keys
- Telemetry or analytics
- Paid tiers, or any feature locked behind a purchase
- Ads
