from PIL import Image
import io
import numpy as np
import cv2
import base64



def Image2Histogram(im):
    im = b64toArray(im)
    img = im

    row = len(im)
    col = len(im[0])
    hist = [0] * 256
    for i in range(row):
        for j in range(col):
            hist[im[i, j]] += 1

    # print hist
    return hist

def b64toArray(b64str):
    img = base64.b64decode(b64str)
    img = Image.open(io.BytesIO(img))
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

