"""Build the README screenshot tour: python tools/build-demo.py (requires Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'app-demo.gif'
SIZE = (1080, 640)
SCENES = [
    ('01-dashboard', 'Your starting point.', 'DASHBOARD', ['See your workspace at a glance.', 'Quick-connect to a host.', 'Return to your open sessions.']),
    ('02-servers', 'Find the right server.', 'SERVERS', ['Organize hosts with folders and tags.', 'Keep favorites close.', 'Connect from one server list.']),
    ('03-terminal', 'Get straight to work.', 'SSH TERMINAL', ['Open an interactive SSH shell.', 'Keep sessions in separate tabs.', 'Use terminal controls within reach.']),
    ('05-sftp', 'Bring your files along.', 'SFTP FILES', ['Browse remote folders.', 'Inspect files and permissions.', 'Manage files beside your terminal.']),
    ('04-timeline', 'Remember what changed.', 'SERVER TIMELINE', ['Review recorded server activity.', 'Search and filter events.', 'Keep notes with your server history.']),
    ('06-tunnels', 'Reach what you need.', 'SSH TUNNELS', ['Manage your saved tunnels.', 'Forward ports over SSH.', 'Keep connection tools in one place.']),
]

def font(size, bold=False):
    candidates = ([r'C:\Windows\Fonts\segoeuib.ttf', 'DejaVuSans-Bold.ttf'] if bold
                  else [r'C:\Windows\Fonts\segoeui.ttf', 'DejaVuSans.ttf'])
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    raise RuntimeError('Install Segoe UI or DejaVu Sans to render the tour.')

slides = []
for index, (filename, title, category, lines) in enumerate(SCENES):
    im = Image.new('RGB', SIZE, '#0b1224')
    d = ImageDraw.Draw(im)
    for y in range(640):
        d.line((0, y, 1079, y), fill=(11 + y//100, 18, 36 + y//60))
    d.rounded_rectangle((40, 40, 195, 75), radius=17, fill='#213152')
    d.text((57, 46), 'CUBEPILOT', font=font(18, True), fill='#a9dffa')
    d.text((42, 135), f'0{index+1} / 06  ·  {category}', font=font(18, True), fill='#22d3ee')
    d.text((40, 191), title, font=font(36, True), fill='#f4f6ff')
    for j, line in enumerate(lines):
        d.ellipse((43, 284+j*53, 49, 290+j*53), fill='#a78bfa')
        d.text((66, 273+j*53), line, font=font(21), fill='#b7c5e2')
    d.text((42, 486), 'ANDROID + WINDOWS', font=font(17, True), fill='#8fa6cd')
    d.text((42, 517), 'A tour of real app screenshots', font=font(17), fill='#8fa6cd')
    d.rounded_rectangle((718, 23, 1022, 616), radius=27, fill='#060b16', outline='#455781', width=2)
    screenshot = ImageOps.contain(Image.open(ROOT/'assets/screenshots'/f'{filename}.jpg').convert('RGB'), (278, 565), Image.Resampling.LANCZOS)
    im.paste(screenshot, (870-screenshot.width//2, 320-screenshot.height//2))
    for j in range(6):
        d.rounded_rectangle((42+j*79, 586, 108+j*79, 590), radius=2,
                            fill='#22d3ee' if j==index else '#293856')
    slides.append(im)

# One palette for the entire tour keeps colours stable during transitions.
atlas = Image.new('RGB', (1080, 640*len(slides)))
for i, slide in enumerate(slides):
    atlas.paste(slide, (0, 640*i))
palette = atlas.quantize(colors=256)
frames = []
for i, slide in enumerate(slides):
    for step in range(20):
        frame = Image.blend(slides[(i-1)%len(slides)], slide, (step+1)/4) if step<4 else slide.copy()
        d = ImageDraw.Draw(frame)
        # A small progress indicator moves while each screenshot remains readable.
        d.rounded_rectangle((42+i*79, 596, 42+i*79+max(2,int(66*(step+1)/20)), 600), radius=2, fill='#a78bfa')
        frames.append(frame.quantize(palette=palette, dither=Image.Dither.NONE))
frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=150, loop=0, optimize=True, disposal=1)
slides[0].save(ROOT/'assets/app-demo-preview.png', optimize=True)
with Image.open(OUT) as gif:
    assert gif.n_frames==120 and gif.size==SIZE and gif.info['loop']==0
print(f'{OUT.name}: 120 frames, 18 seconds, {OUT.stat().st_size:,} bytes')
