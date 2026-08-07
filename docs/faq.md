# Frequently Asked Questions

## Is CubePilot really free?

Yes. Every feature, on both platforms, at no cost. There is no trial, no pro
tier, no seat limit, no ads, and nothing to unlock with a purchase.

## Then how is it funded?

CubePilot is built by [CubePy](https://cubesystem.top) alongside the rest of
the Cube ecosystem. It is not a business on its own and doesn't need to pay
for itself.

There is an optional
[crypto donation link](../README.md#️-support-the-project) for anyone who
wants to chip in toward hosting, signing certificates and test devices.
Donating changes nothing about the app: there is no supporter tier, no badge,
and no feature that donors get and you don't. Starring the repo and filing
good bug reports help just as much.

## Will there ever be a paid version?

No. Every feature stays free on both platforms. If we ever build something
genuinely separate — say team-oriented services — it would be additional,
never a fence around what you already have.

## Why is the source code not public?

CubePilot is closed source by choice. This repository exists for releases,
documentation and issue tracking — that is the whole of our public presence.
Free and open source are different things, and CubePilot is the first without
being the second.

Documentation in this repository *is* open to pull requests. See
[CONTRIBUTING.md](../CONTRIBUTING.md).

## Where does my data go?

Nowhere. Servers, credentials, SSH keys, session history and notes are stored
locally on your device in an encrypted database, with keys held in the
platform's secure storage. There is no CubePilot account system and no sync
server, so there is nothing for us to receive even if we wanted it.

Backups are files you export yourself, encrypted, and keep wherever you like.

## Does CubePilot collect telemetry or analytics?

No. There is no analytics SDK, no crash reporter phoning home, and no usage
tracking. If we ever want data from you, we will ask in an issue.

## How do I move my data to a new device?

Settings → Backup → Export. That produces a single encrypted file. On the new
device, Settings → Backup → Import. Keep the passphrase safe; without it the
backup cannot be recovered, by you or by us.

## Which platforms are supported?

Android 8.0 (API 26) and newer, and 64-bit Windows 10 1809 and newer. Linux
and macOS are [under consideration](roadmap.md#under-consideration) but not
committed to.

## Can I import my servers from Termius, PuTTY or an SSH config file?

Importing from `~/.ssh/config` is planned. Termius and PuTTY import are not
yet scheduled — if you need one of them, say so in a
[Feature request](https://github.com/cubepy/CubePilot/issues/new/choose), since
demand is how we order this kind of work.

## Does it support jump hosts / bastions?

Not in the first release. It is on the
[under consideration](roadmap.md#under-consideration) list.

## What key types does the key manager support?

RSA, ED25519 and ECDSA, with passphrase-protected keys. You can import
existing keys or generate new ones in the app, and inspect fingerprints
before trusting anything.

## Is it safe to keep my SSH keys in CubePilot?

Keys are stored in the encrypted local database, with the encryption key held
in Android Keystore or Windows DPAPI / Credential Manager rather than in the
app's own files. Enable app lock — fingerprint, Windows Hello or PIN — and set
an auto-lock timeout, because an unlocked device is the realistic threat.

Nothing protects you from a device that is already fully compromised. That is
true of every SSH client, including this one.

## What is Server Timeline, exactly?

A complete, searchable history for each server: connections, session
durations, commands, file transfers, permission changes, restarts, tunnels,
errors, status changes and your own notes — recorded automatically, in order.
It is the feature CubePilot is built around. See the
[README](../README.md#-server-timeline--the-signature-feature).

## Is the timeline sent anywhere?

No. It is stored in the same encrypted local database as everything else.

## Can I turn command logging off?

Yes. Timeline recording is configurable per category and per server, and can
be disabled entirely in settings.

## Why does Windows warn me when I run the installer?

Because SmartScreen doesn't recognize a new publisher yet. See
[installation.md](installation.md#windows) for what to check before you click
through it.

## Why isn't CubePilot on the Play Store or the Microsoft Store?

Store distribution may come later. For now, GitHub Releases is the only
official channel — anything calling itself CubePilot anywhere else is not
ours.

## When is the first release?

When it is good enough. Watch 👁 the repository and you'll be notified the
moment it lands. Progress is tracked in [roadmap.md](roadmap.md).

## I found a bug / I have an idea

[Open an issue](https://github.com/cubepy/CubePilot/issues/new/choose), or
start a thread in
[Discussions](https://github.com/cubepy/CubePilot/discussions). For security
problems, follow [SECURITY.md](../SECURITY.md) instead — not a public issue.
