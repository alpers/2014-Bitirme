__author__ = 'alp'
from PIL import Image
from random import randint

def setimage(path, pxcount):
    img = Image.open(path, 'r')
    pixels = img.load()
    for i in range(0, pxcount):
        x = randint(0, img.size[0]-1)
        y = randint(0, img.size[0]-1)
        if pixels[x, y] == (0,0,0):
            pixels[x, y] = 255,255,255
        else:
            pixels[x, y] = 0,0,0
    return img

def saveimage(start, stop, imgcount, label):
    text = ""
    for p in range(0,imgcount):
        pxcnt = randint(start, stop)
        imgcurrent = setimage(imgfile, pxcnt)
        filename = "img_quad_train" + str(pxcnt) + "_" + str(p) + ".png"
        text += "ctq/dataset/train/" + filename + " " + str(label) + "\n"
        imgcurrent.save(filename)

    text_file = open(imgfile + "_label.txt", "w")
    text_file.write(text)
    text_file.close()

imgfile = "quad.png"
#labels: circle=0, tri=1, quad=2
saveimage(100, 300, 2000, 2)
