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

The demo APK is not built on every commit — it is a second full compile,
and paying for one per push is how a month of CI minutes disappears. Run
the **CI** workflow manually with **demo** ticked, then grab
`cubepilot-android-demo` from that run's artifacts. It
installs as a separate app — package `top.cubesystem.cubepilot.demo`,
labelled **CubePilot Demo** — so it sits beside the real app rather than
replacing it. Install it, take the shots, uninstall it; the real app and
its vault are untouched.

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

| File | Screen | What should be on screen | Status |
| --- | --- | --- | --- |
| `01-dashboard.jpg` | Dashboard | Non-zero stat cards, quick-connect field, an open session listed | ✅ |
| `02-servers.jpg` | Servers | Four servers, folder chips visible, a pinned and a starred entry | ✅ |
| `03-terminal.jpg` | Terminal | Two tabs open, colorized `ls -l` output, prompt visible | ⏳ |
| `04-timeline.jpg` | Timeline | Mixed event kinds, at least one bookmarked note and one tagged event | ✅ |
| `05-sftp.jpg` | Files | A populated remote directory with permission strings | ⏳ |
| `06-tunnels.jpg` | Tunnels | One running and one stopped tunnel | ✅ |
| `07-keys.jpg` | SSH Keys | Two keys with fingerprints | ✅ |
| `08-settings.jpg` | Settings | Theme picker and the terminal section | ✅ |

The two pending shots both need a **live session**, which the demo build
cannot give you — its servers are documentation-range addresses that
deliberately route nowhere. Take those two against a real host and blur
the hostname, prompt and any path that identifies the machine before
committing. The README gallery already omits them, so nothing renders
broken until they land.

The first four carry the most weight — a reader rarely scrolls past them.

## Naming and format

- JPEG, quality 85–90. The gallery is six images on one page; PNG
  screenshots of a dark UI came out several megabytes each, which is a
  slow README on a phone.
- No scaling, borders or device frames added afterwards.
- Numbered prefixes as above, so the gallery order is stable.
- Commit them to `assets/screenshots/`.

Once the files are in place the README gallery renders automatically; the
markup already references these exact names.
