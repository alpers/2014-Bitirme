__author__ = 'alp'

from PIL import Image
from random import randint

class Baby:
    global background,mask, x, y, rotate
    #def __init__(self,background, mask, x, y, rotate):
    def __init__(self):
        #self.background = background
        #self.mask = mask
        #self.x = x
        #self.y = y
        #self.rotate = rotate
        pass

    def create_image(self):
        """
        rastgele farkli yerlerde ve
        farkli derecelerde dondurulmus gorseller olusturur
        """
        backgroundImg = Image.open(self.background)
        maskImg = Image.open(self.mask)
        sizeX, sizeY = backgroundImg.size
        coordinateX = randint(30, sizeX-30)
        coordinateY = randint(30, sizeY-30)
        self.x = randint(0, sizeX)
        self.y = randint(0, sizeY)
        self.rotate = randint(0,359)
        backgroundImg.paste(maskImg.rotate(self.rotate), (self.x, self.y), maskImg.rotate(self.rotate))
        return backgroundImg

    def save_image(self, background, mask, imgcount):
        """
        degistirilmis gorseli kaydeder. label text dosyasi olusturur, kaydeder
        """
        self.background = background
        self.mask = mask
        text = ""
        for p in range(imgcount):
            imgcurrent = self.create_image()
            imageFileName = background[:-4] + str(p) + ".png"
            filename = background[:-4] + "_" + str(p) + ".png"
            text += "ImageGenerate/Babydataset/" + filename + " " + background[:-4] + "\n"
            imgcurrent.save(filename)
        text_file = open(background[:-4] + "_train_label.txt", "w")
        text_file.write(text)
        text_file.close()

    def select_file(self):
        """
        gorseli secer. (varsayilan: root path)
        """
        for i in range(1,22):
            bg = "pd" + str(i) + "c.png"
            ms = "pd" + str(i) + "b.png"
            self.save_image(bg, ms, 5)
