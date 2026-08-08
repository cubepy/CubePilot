# Troubleshooting

Common problems and what to check before opening an issue.

> If something here didn't help you, that is worth an
> [issue](https://github.com/cubepy/CubePilot/issues/new/choose). This page
> grows from real cases.

---

## Connection

### "Connection refused"

The port is closed or nothing is listening on it.

- Confirm the port — SSH is usually 22, but a hardened server often isn't.
- Check the server's firewall (`ufw status`, `firewall-cmd --list-all`) and any
  cloud security group in front of it.
- Confirm `sshd` is running: `systemctl status sshd`.

### "Connection timed out"

Traffic isn't reaching the server at all.

- Try from another network — mobile data instead of Wi-Fi is the fastest test.
- Check whether a cloud firewall allows your current IP.
- On a mobile network, some carriers block outbound port 22. If the same
  server works over Wi-Fi and not over mobile data, that is what you're
  hitting; run SSH on an alternate port.

### "Host key verification failed"

The server presented a different host key than the one CubePilot remembered.

Do not dismiss this by reflex. It means either the server was rebuilt or
reinstalled, or you are being intercepted. Verify the fingerprint out of band —
on the server, run:

```sh
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

If it matches what CubePilot shows, accept the new key. If it doesn't, stop and
find out why.

### "Permission denied (publickey)"

- Make sure the public half of your key is in `~/.ssh/authorized_keys` on the
  server, for the user you're connecting as.
- Check permissions on the server: `~/.ssh` must be `700`, `authorized_keys`
  must be `600`, and the home directory must not be group-writable.
- Confirm you selected the right key in the server's settings — CubePilot uses
  the key attached to that server, not every key you have.
- If the key has a passphrase, make sure you entered it, not the account
  password.

### The password prompt keeps coming back

The server may have `PasswordAuthentication no`. Use a key instead.

---

## Terminal

### Boxes, question marks or broken line drawing

Your font lacks the glyphs. Pick a font with good coverage in
**Settings → Terminal → Font**; a Nerd Font is the right answer if your prompt
uses Powerline symbols.

### Colors look wrong

Check that the server's `TERM` is sensible (`xterm-256color`) and that your
prompt or `LS_COLORS` isn't assuming a light background while you run a dark
theme.

### Text is misaligned in `htop`, `vim` or `tmux`

Usually a terminal size mismatch after a rotation or window resize. Run
`resize` on the server, or reconnect the session.

---

## SFTP

### "Permission denied" on upload

You lack write permission in the target directory. Check the owner and mode of
the remote path — CubePilot uses your SSH user's permissions and nothing more.

### Transfers are slow

- Compare against `scp` from a desktop on the same network to see whether the
  bottleneck is CubePilot or the link.
- Many small files are far slower than one large file; archive them first.
- On mobile, a weak signal shows up as throughput collapse long before the
  connection drops.

---

## App lock and keys

### Biometric unlock stopped working

Adding or removing a fingerprint, or a face enrolment, invalidates the
platform key on both Android and Windows. This is a security property, not a
bug. Unlock with your PIN and re-enable biometrics in settings.

### I forgot my PIN / backup passphrase

There is no recovery. The database is encrypted with a key derived from it, we
hold no copy, and there is no account to reset. You will need to reinstall and
start over — or restore from a backup whose passphrase you do remember.

---

## Android

### The session dies when the app goes to the background

CubePilot runs a foreground service — the notification you see while a session
is open — precisely to stop this. If sessions still die, the manufacturer's
battery manager is killing the process anyway; Xiaomi, Samsung, Huawei and
OnePlus are the usual ones. Exclude CubePilot in **Android Settings → Apps →
CubePilot → Battery → Unrestricted**.

Note that a dropped session is not necessarily a killed app: CubePilot
reconnects by itself and says so in the terminal, keeping your scrollback.

### The app isn't installing

See [installation.md](installation.md#android) — "install from unknown
sources" has to be granted to the app you're installing *from*, which is your
browser or file manager, not CubePilot.

---

## Windows

### SmartScreen blocks the app

Expected: the executable is unsigned, and an unsigned binary has no reputation
with Microsoft. Verify the checksum first, then **More info → Run anyway**. See
[installation.md](installation.md#windows).

### The app starts but my servers are gone after updating

The Windows build is portable, but its data is not stored beside the
executable — it lives in `%APPDATA%\top.cubesystem\cubepilot`. Replacing the
program folder never touches it. If servers really did vanish, it means the app
is running as a different Windows user than the one that created them.

### The Glass theme looks flat on Windows

The Glass theme blurs what is behind each card *inside* the app; it is not
Windows 11 Mica and does not sample your wallpaper. Mica, Acrylic and a tray
icon are on the [roadmap](roadmap.md), not in the app yet.

### Antivirus quarantines the app

Report it as a false positive to your vendor, and
[tell us](https://github.com/cubepy/CubePilot/issues/new/choose) which product
and which detection name — we can submit it for review.

---

## Docker, Kubernetes and logs

### "docker: command not found" or a permission error on the socket

These screens run the real `docker` and `kubectl` on the server you are
connected to, as the user you connected as. If the command is missing or your
user is not in the `docker` group, CubePilot says so rather than pretending —
the fix is on the server, not in the app.

### Kubernetes says there is no kubeconfig

`kubectl` finds its config in the home directory of the user you connected as.
Connecting as a different user than the one that set the cluster up is the
usual cause.

### A log file will not open

Most logs under `/var/log` are readable only by root or by a group your user
may not be in. `Permission denied` here is the server's answer, not a bug.

---

## Jump hosts

### "The jump host … no longer exists"

The server it was set to connect through has been deleted. Edit the server and
pick another one, or set it back to **Directly**. CubePilot refuses to connect
straight to the target instead, because that would send the traffic somewhere
you never agreed to send it.

### "These jump hosts point at each other in a loop"

Two servers are each set to connect through the other, so there is no way in.
Edit either one.

---

## Still stuck?

1. Update to the [latest release](https://github.com/cubepy/CubePilot/releases/latest).
2. Search [existing issues](https://github.com/cubepy/CubePilot/issues?q=is%3Aissue).
3. Open a [Bug report](https://github.com/cubepy/CubePilot/issues/new/choose)
   with your version, platform and reproduction steps — and **redact your keys,
   passwords and real server addresses** before you paste any logs.
