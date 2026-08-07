# Screenshot guide

Notes for producing the images in the README gallery, so they stay
consistent between releases — and so none of them leak real infrastructure.

## Rule zero: never photograph a real server

A screenshot of an SSH client is a screenshot of someone's infrastructure.
Hostnames, IP addresses, usernames, prompts and command history are all
reconnaissance material once they're in a public README.

Use the **demo build** instead. It ships a fabricated workspace whose
addresses all come from the documentation ranges reserved by
[RFC 5737](https://www.rfc-editor.org/rfc/rfc5737) and
[RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) — `203.0.113.x`,
`198.51.100.x`, `192.0.2.x`, `*.example.com`. Those can never route to
anything real.

Grab `cubepilot-android-demo` from the latest CI run's artifacts. It is a
separate build; install it, take the shots, uninstall it.

If a shot must show something the demo build can't produce, blur or edit
the identifying parts before committing it.

## Device and settings

- **Phone:** any 1080×2400-ish display. Consistency across shots matters
  more than the exact device.
- **Theme:** Dark for the whole gallery. It's the default and it's what
  the brand palette is designed around.
- **Language:** English for `README.md`, Persian for `README-fa.md` where
  a shot contains UI text.
- Turn off the notification shade clutter, and use a full battery / full
  signal status bar if your device can fake one.

## Shot list

| File | Screen | What should be on screen |
| --- | --- | --- |
| `01-dashboard.png` | Dashboard | Non-zero stat cards, quick-connect field, an open session listed |
| `02-servers.png` | Servers | Four servers, folder chips visible, a pinned and a starred entry |
| `03-terminal.png` | Terminal | Two tabs open, colorized `ls -l` output, prompt visible |
| `04-timeline.png` | Timeline | Mixed event kinds, at least one bookmarked note and one tagged event |
| `05-sftp.png` | Files | A populated remote directory with permission strings |
| `06-tunnels.png` | Tunnels | One running and one stopped tunnel |
| `07-keys.png` | SSH Keys | Two keys with fingerprints |
| `08-settings.png` | Settings | Theme picker and the terminal section |

The first four carry the most weight — a reader rarely scrolls past them.
If time is short, do those properly and add the rest later.

## Naming and format

- PNG, no scaling or borders added afterwards.
- Numbered prefixes as above, so the gallery order is stable.
- Commit them to `assets/screenshots/`.

Once the files are in place the README gallery renders automatically; the
markup already references these exact names.
