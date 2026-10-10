"""Rebuild the README demo from real Android recordings; requires FFmpeg."""
import argparse, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--ffmpeg',default='ffmpeg')
args=parser.parse_args()
assets=ROOT/'assets'
sources=[assets/'recordings/ssh-terminal.mp4',assets/'recordings/sftp-transfer.mp4']
# Retain the real connection, commands, file selection and transfer results.
ranges=[(0,9,21),(0,39,59),(0,67,93),(0,98,113),(1,19,38),(1,49,56),(1,73,93)]
filters=[]
labels=[]
for i,(source,start,end) in enumerate(ranges):
    label=f'v{i}'
    filters.append(f'[{source}:v]trim=start={start}:end={end},setpts=(PTS-STARTPTS)/3[{label}]')
    labels.append(f'[{label}]')
filters.append(''.join(labels)+f'concat=n={len(labels)}:v=1:a=0,fps=12,format=yuv420p[out]')
def run(arguments):
    subprocess.run([args.ffmpeg,'-hide_banner','-loglevel','error','-y',*arguments],check=True)
video=assets/'app-demo.mp4'
run(['-i',str(sources[0]),'-i',str(sources[1]),'-filter_complex',';'.join(filters),'-map','[out]',
     '-an','-c:v','libx264','-crf','21','-movflags','+faststart',str(video)])
run(['-i',str(video),'-filter_complex',
     'fps=8,split[a][b];[a]palettegen=max_colors=192:stats_mode=diff[p];[b][p]paletteuse=dither=none',
     '-loop','0',str(assets/'app-demo.gif')])
run(['-ss','17','-i',str(video),'-frames:v','1',str(assets/'app-demo-preview.png')])
print('Built real screen recording: MP4, looping GIF and static preview.')
