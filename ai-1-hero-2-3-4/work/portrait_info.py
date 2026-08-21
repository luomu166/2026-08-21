from PIL import Image

f = r"C:\Users\频繁落幕\Desktop\个人作品\大头照片\大头照片.png"
with Image.open(f) as im:
    print(im.size, im.mode)
