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

def saveimage(start, stop, imgcount):
    text = ""
    for p in range(0,imgcount):
        pxcnt = randint(start, stop)
        imgcurrent = setimage(imgfile, pxcnt)
        filename = "img_" + str(pxcnt) + "_" + str(randint(0, 1000)) + ".png"
        text += "/images/" + imgfile + "/" + filename + ", 0" + "\n"
        imgcurrent.save(filename)

    text_file = open(imgfile + "_label.txt", "w")
    text_file.write(text)
    text_file.close()

imgfile = "circle.png"

saveimage(100, 200, 1000)
saveimage(200, 300, 1000)
