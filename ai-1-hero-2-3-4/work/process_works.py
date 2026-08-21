"""Optimize the user's 5 works into the portfolio site's project folder."""
from PIL import Image
import os

src_dir = r"C:\Users\频繁落幕\Desktop\个人作品"
dst_dir = r"outputs\portfolio-site\assets\img\projects"
os.makedirs(dst_dir, exist_ok=True)

for i in range(1, 6):
    src = os.path.join(src_dir, f"{i}.png")
    dst = os.path.join(dst_dir, f"work-{i:02d}.jpg")
    with Image.open(src) as im:
        im = im.convert("RGB")
        # 目标 1600x900（16:9），原图即为 16:9，直接缩放到目标宽度
        w = 1600
        h = round(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"work-{i:02d}.jpg  {w}x{h}  {round(os.path.getsize(dst)/1024)} KB")
