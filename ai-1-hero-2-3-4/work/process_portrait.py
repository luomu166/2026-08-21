"""Center-crop the user's portrait to 4:5 and optimize for the site."""
from PIL import Image

src = r"C:\Users\频繁落幕\Desktop\个人作品\大头照片\大头照片.png"
dst = r"outputs\portfolio-site\assets\img\portrait.jpg"

with Image.open(src) as im:
    im = im.convert("RGBA")
    # 透明区域用站点背景色填充，避免转 JPG 后变黑
    bg = Image.new("RGBA", im.size, (13, 13, 18, 255))
    im = Image.alpha_composite(bg, im).convert("RGB")

    w, h = im.size
    target_ratio = 4 / 5  # 竖版 4:5，与头像框一致
    if w / h > target_ratio:
        new_w = round(h * target_ratio)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        new_h = round(w / target_ratio)
        top = (h - new_h) // 2
        im = im.crop((0, top, w, top + new_h))

    im = im.resize((800, 1000), Image.LANCZOS)
    im.save(dst, "JPEG", quality=88, optimize=True, progressive=True)

import os
print("portrait.jpg", im.size, round(os.path.getsize(dst) / 1024), "KB")
