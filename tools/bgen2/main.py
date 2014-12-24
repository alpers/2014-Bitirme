# -*- coding: utf-8 -*-
#/usr/bin/python

# her bebek icin 100 arkaplan ornekle, ornekleri 1, arkaplanlari 0 yap.

# arkaplan ornekleri, bebeklerin koyulacagi arkaplanlarin buyuklukleri 120x120 gibi bisey olsun.
# Salt negatif orneklemelerde 20x20'den 200x200'ye kadar alsin, sonra belirlenen buyukluge bunu resize edelim.
# Butun ornekleri 140x210'a resize edelim.
import sys
from random import randint
from PIL import Image
from os.path import join

BACKGROUND_SOURCE = "data/babies/core/background"
BABIES_SOURCE = "data/babies/core/baby/cropped"

SAMPLE_AMOUNT = 100
BABYIMG_COUNT = 22
BACKGROUND_DIM = (480, 640)


def get_random_coordinates(imagesize, dimensions):
    """
    Rastgele ornek icin koordinat ureteci
    """
    wid, hei = imagesize

    y1 = randint(0, wid - dimensions[0])
    x1 = randint(0, hei - dimensions[1])
    y2 = y1 + dimensions[0]
    x2 = x1 + dimensions[1]

    return y1, x1, y2, x2


# Her bebek icin 100 tane ornekle. Bu arkaplanlar ayni olmasin lakin
MAX_FAILCOUNT = 100
def sample_backgrounds(babyimg_size, babyimg_no, existing_samples):
    failcount = 0

    for i in range(SAMPLE_AMOUNT):
        coords = get_random_coordinates(BACKGROUND_DIM, babyimg_size)
        randbg = randint(1, 22)
        descstr = "%d-%d--%d-%d-%d-%d" % (babyimg_no, randbg, coords[0], coords[1], coords[2], coords[3])

        if existing_samples[babyimg_no].get(descstr, False):
            failcount += 1
            print failcount
            if failcount == MAX_FAILCOUNT:
                raise Exception("MAXFAILCOUNT")
        else:
            existing_samples[babyimg_no][descstr] = True


# Bebekleri orneklerin ustune oturt
def place_baby(descarr, descstr):
    babyimg = Image.open(join(BABIES_SOURCE, "pd%db.png" % descarr[0]))
    background = Image.open(join(BACKGROUND_SOURCE, "pd%dc.png") % descarr[1])


    croppedback = background.crop(box=descarr[2:])
    croppedresize = croppedback.resize((140, 210))
    croppedresize.save("data/babies/training/background/%s.png" % descstr)

    croppedback.paste(babyimg, (0, 0), babyimg)
    resized = croppedback.resize((140, 210))
    resized.save("data/babies/training/merged/%s.png" % descstr)

    with open("data/babies/training/labels.txt", "a") as file_:
        file_.write("data/babies/training/background/%s.png 0\n" % descstr)
        file_.write("data/babies/training/merged/%s.png 1\n" % descstr)


def write_images(descdict):
    for imgno in descdict.keys():
        for key in descdict[imgno].keys():
            tkey = key.replace("--", "-")
            vals = tkey.split("-")
            vals = map(lambda it: int(it), vals)
            image = place_baby(vals, key)


def main():
    background_image_desc = {}

    for i in range(1, BABYIMG_COUNT+1):
        background_image_desc[i] = {}
        currbabyim = Image.open(join(BABIES_SOURCE, "pd%db.png" % i))
        sample_backgrounds(currbabyim.size, i, background_image_desc)

    write_images(background_image_desc)

    return 0


if __name__ == "__main__":
    retval = main()
    sys.exit(retval)