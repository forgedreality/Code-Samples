import cv2
from mss import mss
from PIL import Image
import random
import time
import main
import numpy as np
# import nanogui

# bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}
bounding_box = {'top': 540, 'left': 1080, 'width': 1920, 'height': 1080}

# Capture a bbox using percent values

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "RGBX")
    imgLum = Image.frombytes("L", sct_img.size, sct_img.bgra, "raw", "L")
    coordinates = []
    lums = []
    for i in range(20):
        xcoord = random.randint(0, 1919)
        ycoord = random.randint(0, 1079)
        coordinate = x, y = xcoord, ycoord
        coordinates.append(img.getpixel(coordinate))
        lums.append(imgLum.getpixel(coordinate))

    r_avg = 0
    g_avg = 0
    b_avg = 0
    l_avg = 0

    for c in coordinates:
        r_avg += c[0]
        g_avg += c[1]
        b_avg += c[2]

    for l in lums:
        l_avg += l

    r_avg = int(r_avg / len(coordinates))
    g_avg = int(g_avg / len(coordinates))
    b_avg = int(b_avg / len(coordinates))
    l_avg = int(l_avg / len(coordinates))

    # print(f"({r_avg}, {g_avg}, {b_avg})")
    # img = list(img.getdata())

    # for c in range(0, len(img), 4):
    #     print(img[c])

    # img = img.effect_spread(5)
    # help(img.getdata)
    # img = img.transpose(Image.FLIP_TOP_BOTTOM)
    # iclrs = Image.Image.getcolors(img)

    # cv2.imshow('screen', np.array(img))

    # main.color_fill_init(panels, inhsv)

    # time.sleep(0.5)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
