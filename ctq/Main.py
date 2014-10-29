__author__ = 'alp'
from PIL import Image
from random import randint

def create_image(path, pxcount):
    """
    gorselin random piksel degerlerini degistirerek yeni gorsel olusturur
    pxcount: kac kez random piksel degistirme islemi yapiliyor
    """
    img = Image.open(path, 'r')
    pixels = img.load()
    for i in range(pxcount):
        x = randint(img.size[0]-1)
        y = randint(img.size[0]-1)
        if pixels[x, y] == (0,0,0):
            pixels[x, y] = 255,255,255
        else:
            pixels[x, y] = 0,0,0
    return img

def save_image(start, stop, imgcount, label):
    """
    degistirilmis gorseli kaydeder. label text dosyasi olusturur, kaydeder
    """
    text = ""
    imgfile = select_file(label)
    for p in range(imgcount):
        pxcnt = randint(start, stop)
        imgcurrent = create_image(imgfile, pxcnt)
        filename = "img_" + str(label) + "_" + str(p) + "_" + str(pxcnt) + ".png"
        text += filename + "\n"
        imgcurrent.save(filename)
    text_file = open(imgfile + "_label.txt", "w")
    text_file.write(text)
    text_file.close()

def select_file(imglabel):
    """
    etikete gore gorseli secer. (varsayilan: root path)
    """
    if imglabel == 0:
        imgfile = "circle.png"
    elif imglabel == 1:
        imgfile = "tri.png"
    elif imglabel == 2:
        imgfile = "quad.png"
    return  imgfile


#labels: circle=0, tri=1, quad=2
save_image(100, 300, 2000, 0)
