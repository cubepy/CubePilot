# Security Policy

CubePilot handles SSH private keys, passwords and access to production
infrastructure. We take reports about it seriously.

## Supported versions

Only the latest release published on the
[Releases](https://github.com/cubepy/CubePilot/releases) page receives
security fixes. If you are running an older build, update before reporting.

| Version | Supported |
| --- | --- |
| Latest release | ✅ |
| Anything older | ❌ |

## Reporting a vulnerability

**Do not open a public issue for a security problem.**

Use GitHub's private reporting instead:

1. Go to the [Security tab](https://github.com/cubepy/CubePilot/security).
2. Click **Report a vulnerability**.
3. Describe the issue, the CubePilot version and platform, and how to
   reproduce it.

The report stays private between you and the maintainers until a fix is
released.

### What to include

- CubePilot version and platform (Android / Windows), and OS version
- What an attacker can do — reading stored keys, escaping the key vault,
  bypassing auto-lock, intercepting a session, and so on
- Reproduction steps, and a proof of concept if you have one
- Whether the issue needs physical access to the device, a malicious server,
  or a network position

### What not to include

Never send us your real private keys, passwords, passphrases or backup
files, and never include the hostname or IP of a live production server.
Reproduce the problem against a throwaway server with throwaway credentials.

## What to expect

- We aim to acknowledge a report within **72 hours**.
- We will tell you whether we consider it a vulnerability, and if so, our
  planned fix and timeline.
- Once a fix ships, we credit you in the release notes and in
  [CHANGELOG.md](CHANGELOG.md) — unless you would rather stay anonymous.

We ask that you give us a reasonable window to release a fix before
disclosing the issue publicly.

## Out of scope

- Vulnerabilities in third-party servers you connect **to** with CubePilot
- Vulnerabilities in the Android or Windows platform itself
- Attacks that require an already-compromised device with the app unlocked
- Reports from automated scanners with no demonstrated impact
- Missing hardening that has no exploitable consequence

## A note on distribution

CubePilot is distributed **only** through this repository's Releases page.
A build obtained anywhere else is not ours, may be modified, and should
never be given access to your keys. If you find CubePilot being
redistributed elsewhere, please
[tell us](https://github.com/cubepy/CubePilot/discussions).
