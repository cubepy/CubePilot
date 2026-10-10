# Animated app tour

The animation beneath the README banner is an 18-second tour assembled from
six existing, real CubePilot screenshots: Dashboard, Servers, Terminal, SFTP,
Timeline and Tunnels. Captions describe the screens; transitions and the
progress indicator are presentation effects.

It is a screenshot tour, not a recording of taps or a new recording of
v0.5.0. The interface may differ in the latest build. The screenshots use
demo data or redacted sessions; see [the screenshot guide](screenshots.md).

[View the static preview](../assets/app-demo-preview.png).

To rebuild from the repository root with Python, Pillow and Segoe UI or
DejaVu Sans installed:

```sh
python tools/build-demo.py
```

The script only uses the public screenshot assets. It does not launch the
app, connect to servers, or access credentials.
