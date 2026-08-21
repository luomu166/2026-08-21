from PIL import Image
import os

files = [
    r"C:\Users\频繁落幕\Desktop\个人资料\跑车1-封面.jpg",
    r"C:\Users\频繁落幕\Desktop\个人资料\超跑11.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\911_b.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\911_b2.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\911_c.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\brake_di.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\brake_diB.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\欧莱雅.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\精华.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\盾牌.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\展示厅.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\画室.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\音乐室最终.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\阅读成.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\发泄区.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\1.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\2.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\22.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\3.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\4.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\无标题.png",
    r"C:\Users\频繁落幕\Desktop\个人资料\645f66f545ee98007a6792181ea1ab5.png",
    r"C:\Users\频繁落幕\Desktop\动画渲染\gt3rs_m.png",
]

for f in files:
    try:
        with Image.open(f) as im:
            w, h = im.size
            print(f"{os.path.basename(f):34s} {w}x{h}  {'landscape' if w > h else 'portrait'}")
    except Exception as e:
        print(os.path.basename(f), "ERR", e)
