import cv2 as cv
import numpy as np
import pandas as pd
from PIL import Image
import os


def scan(image):
    path = os.path.join(os.getcwd(), "static/images", image)

    im = cv.imread(path, 0)
    image_copy = im.copy()

    ret, thresh = cv.threshold(im, 100, 255, cv.THRESH_BINARY)

    contours, hierarchy = cv.findContours(
        image=thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        if((w < 500 or h < 500) and (w > 80 or h > 80)):
            cv.rectangle(image_copy, (x-int(w*0.1), y-int(h*0.1)),
                         (x+w+int(w*0.1), y+h+int(h*0.1)), (0, 255, 0), 3)

    cv.namedWindow("Contours", cv.WINDOW_NORMAL)
    cv.imshow("Contours", image_copy)
    cv.waitKey(0)

    i = 0
    images = []
    for cnt in contours:
        (x, y, w, h) = cv.boundingRect(cnt)
        if((w < 500 or h < 500) and (w > 80 or h > 80)):
            photo = Image.fromarray(
                thresh[y-int(h*0.1):y+h+int(h*0.1), x-int(w*0.1):x+w+int(w*0.1)])
            photo = photo.resize((28, 28), Image.ANTIALIAS)
            photo_arr = np.array(photo)
            cv.imwrite(str(i)+".jpg", photo_arr)
            photo_arr = photo_arr.flatten()
            print("Start point:(%d,%d)" % (x, y))
            print("End point: (%d,%d)" % (x+w, y+h))
            print("\n")
            images.append((photo_arr, x))
            i += 1

    images = sorted(images, key=lambda a: a[1])
    images = [img for img, x in images]

    images = np.array(images)
    images = pd.DataFrame(
        images, columns=["pixel" + str(i) for i in range(0, 784)])

    images = images.values
    images = images.reshape(-1, 28, 28, 1)
    images = images.astype('float32')
    images = images/255.0

    return images
