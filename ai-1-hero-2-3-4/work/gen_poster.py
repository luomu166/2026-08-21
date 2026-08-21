"""Generate the hero poster (dark gradient + glow) for the portfolio site."""
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080
img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

top = (17, 17, 25)
bottom = (6, 6, 9)
for y in range(H):
    t = y / (H - 1)
    c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

grid = (30, 30, 37)
for x in range(0, W, 72):
    d.line([(x, 0), (x, H)], fill=grid)
for y in range(0, H, 72):
    d.line([(0, y), (W, y)], fill=grid)

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)


def glow(cx, cy, r, color, strength):
    for i in range(20, 0, -1):
        rr = r * i // 20
        a = int(strength * (21 - i))
        od.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=color + (a,))


glow(960, 470, 720, (255, 59, 59), 7)
glow(260, 200, 480, (255, 82, 82), 5)
glow(1660, 830, 520, (163, 18, 18), 5)
overlay = overlay.filter(ImageFilter.GaussianBlur(70))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

v = Image.new("L", (W, H), 0)
vd = ImageDraw.Draw(v)
vd.ellipse([-W * 0.25, -H * 0.25, W * 1.25, H * 1.25], fill=255)
v = v.filter(ImageFilter.GaussianBlur(220))
dark = Image.new("RGB", (W, H), (0, 0, 0))
img = Image.composite(img, dark, v)

img.save(r"outputs/portfolio-site/assets/media/hero-poster.jpg", quality=90)
print("poster saved")
