# Roadmap

What CubePilot is being built toward, roughly in the order it is being built.

This is a direction, not a delivery contract — items move between milestones
as they turn out to be harder, easier, or less useful than expected. Dates are
deliberately absent; a milestone ships when it is good enough to ship.

Want something here that isn't? Open a
[Feature request](https://github.com/cubepy/CubePilot/issues/new/choose) or
bring it up in [Discussions](https://github.com/cubepy/CubePilot/discussions).

---

## v0.1.0 — First public beta

The smallest version that is genuinely useful every day.

- [ ] Splash, onboarding and the dashboard
- [ ] Server management: add, edit, delete, search, folders, favorites, pinning
- [ ] SSH terminal with multi-tab sessions, professional color schemes, font
      and cursor selection
- [ ] SSH key manager — RSA, ED25519, ECDSA; import, generate, fingerprint,
      passphrase
- [ ] Encrypted local database and secure key vault
- [ ] App lock: fingerprint, Windows Hello, PIN, auto-lock
- [ ] Dark, Light and OLED themes
- [ ] English and Persian, with full RTL support
- [ ] Encrypted backup export and import
- [ ] Android and Windows builds published on Releases

## v0.2.0 — Files and tunnels

- [ ] SFTP file manager: dual-pane, drag & drop, upload, download, rename,
      delete, in-place edit, permissions, preview, folder size, search
- [ ] Port forwarding: local, remote, dynamic SOCKS5 and HTTP proxy, with
      saved tunnels
- [ ] Split terminal view and the session manager
- [ ] Command palette
- [ ] Command library and the built-in snippet collection

## v0.3.0 — Server Timeline

CubePilot's signature feature, and the reason the app exists.

- [ ] Per-server activity timeline: connections, session durations, commands,
      file transfers, permission changes, service and container restarts,
      tunnel lifecycle, errors, status changes
- [ ] Notes attached to any point on the timeline
- [ ] Search, filter, tag and bookmark across every event
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
