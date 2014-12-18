# -*- coding: utf-8 -*-

# girdi: negatiflerin olduguna emin oldugumuz buyuk resimmlerin oldugu bir klasor
# cikti: negatif orneklemelerin bulundugu dosya

# parametre: resim boyutu

from PIL import Image
from random import randint
from os.path import join
import argparse
import sys
import os
import random


# Orneklemek icin acilacak resimlerin hangi formatta olduklari
IMAGE_EXTENSIONS = [
    "ppm",
    "png",
]


def is_picture(filename):
    """
    Dosyanin uzantisina bakarak resim dosyasi olup olmadigini doner
    :return:
    """
    return True


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


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input-dir", "-i", help="Orneklenecek resimlerin oldugu klasor")
    parser.add_argument("--output-dir", "-o", default=None, help="Orneklenmis resimlerin koyulacagi klasor")
    parser.add_argument("--examples-per-image", "-e", default=10, help="Her buyuk resimden kac tane cikarilacak")
    parser.add_argument("--dimensions", "-d", default=None, help="Orneklenmis resimlerin boyutu")

    args = parser.parse_args()

    if args.dimensions is not None:
        args.dimensions = args.dimensions.split("x")

        args.dimensions[0] = int(args.dimensions[0])
        args.dimensions[1] = int(args.dimensions[1])

    filenames = os.listdir(args.input_dir)

    for fname in filenames:
        if is_picture(fname):
            img = Image.open(join(args.input_dir, fname))
            for i in range(args.examples_per_image):
                box = get_random_coordinates(img.size, args.dimensions)
                sample = img.crop(box)
                sample.save(join(args.output_dir, "%s_%d.png" % (fname.split(".")[0], i+1)))

    return 0




if __name__ == "__main__":
    retval = main()
    sys.exit(retval)




























