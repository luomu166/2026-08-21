from PIL import Image
import os

d = r"C:\Users\频繁落幕\Desktop\个人作品\作品1"
for name in sorted(os.listdir(d)):
    if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
        continue
    f = os.path.join(d, name)
    with Image.open(f) as im:
        w, h = im.size
        print(f"{name:24s} {w}x{h}  ratio={w/h:.3f}  {'landscape' if w > h else 'portrait'}")
