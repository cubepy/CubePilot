# Real app recording

The README demo was recorded from the official **CubePilot v0.5.0 Android
x86_64 APK**, running in an Android emulator. Every app screen, typed command,
SSH response and SFTP progress indicator comes from a real screen recording.
It replaces the previous screenshot slideshow.

The recording shows:

1. Connecting from the saved server list to a disposable local SSH lab.
2. Running `ls -Name` and `cat hello.txt` in the app's terminal. The lab runs
   PowerShell on Windows; these are real command aliases in that shell.
3. Browsing the lab through the app's SFTP client.
4. Selecting and uploading `cubepilot-upload.txt` (204,800 bytes), reaching
   **Completed**, and seeing the file appear on the server.
5. Downloading the same file, reaching **Completed**, and opening Android's
   share sheet.

The uploaded file was compared byte-for-byte with the original. Its SHA-256 is:

```text
b1293372fd2404f73452f56eea15143392599be61055945c2609b01c8f63199e
```

The SSH endpoint is loopback `127.0.0.1:2222`, forwarded to the local lab from
the emulator. All filenames and file contents are disposable demo data.
The lab uses a temporary SSH host key and an isolated SFTP directory;
no production server, user credential or private infrastructure is shown.

The demo combines two capture segments, omits long pauses and plays retained
footage at **3× speed**. It adds no simulated UI, command output, transfer
results or screenshot transitions. Audio is not included.

- [Watch the edited MP4](../assets/app-demo.mp4)
- Original recordings: [SSH and terminal](../assets/recordings/ssh-terminal.mp4)
  and [SFTP transfer](../assets/recordings/sftp-transfer.mp4)

[View the static preview](../assets/app-demo-preview.png).

To regenerate the edited MP4, GIF and preview with Python and FFmpeg:

```sh
python tools/build-live-demo.py --ffmpeg /path/to/ffmpeg
```

The generator uses only the two public recordings. The app's private source,
lab host key and server process are not included in this repository.
