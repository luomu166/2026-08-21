"""Optimize the 6 new works (作品1) into the portfolio site's project folder."""
from PIL import Image
import os

src_dir = r"C:\Users\频繁落幕\Desktop\个人作品\作品1"
dst_dir = r"outputs\portfolio-site\assets\img\projects"
os.makedirs(dst_dir, exist_ok=True)

names = sorted(n for n in os.listdir(src_dir) if n.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
for i, name in enumerate(names, start=6):
    src = os.path.join(src_dir, name)
    dst = os.path.join(dst_dir, f"work-{i:02d}.jpg")
    with Image.open(src) as im:
        im = im.convert("RGB")
        w = 1600
        h = round(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"{name:22s} -> work-{i:02d}.jpg  {w}x{h}  {round(os.path.getsize(dst)/1024)} KB")
