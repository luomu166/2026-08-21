from PIL import Image
import os

d = r"C:\Users\频繁落幕\Desktop\个人作品"
for name in sorted(os.listdir(d)):
    if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
        continue
    f = os.path.join(d, name)
    with Image.open(f) as im:
        w, h = im.size
        gray = im.convert("L").resize((64, 64))
        px = list(gray.getdata())
        avg = sum(px) / len(px)
        print(f"{name:12s} {w}x{h}  ratio={w/h:.3f}  "
              f"{'landscape' if w > h else 'portrait'}  avgBrightness={avg:.0f}")
