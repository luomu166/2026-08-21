import os

for d in [r"C:\Users\频繁落幕\Desktop\个人资料", r"C:\Users\频繁落幕\Desktop\动画渲染"]:
    print("DIR:", d, "exists:", os.path.isdir(d))
    try:
        for name in sorted(os.listdir(d)):
            print("  ", repr(name))
    except Exception as e:
        print("  ERR", e)
