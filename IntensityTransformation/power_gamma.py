from PIL import Image
import io
import numpy as np
import cv2
import base64

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    image = b64toArray(image)

    invGamma = 1.0 / gamma

    # ImgRow, ImgColumn = image.shape
    ImgRow = len(image)
    ImgColumn = len(image[0])
    r1 = np.zeros((ImgRow, ImgColumn), np.uint8)
    # print (r1)
    for i in range(ImgRow):
        for j in range(ImgColumn):
            print(((image[i,j]/ 255.0) ** invGamma) * 255)
            r1[i,j]=((image[i,j]/ 255.0) ** invGamma) * 255


    # apply gamma correction using the lookup table
    return Arraytob64(r1)

def b64toArray(b64str):
    img = base64.b64decode(b64str)
    img = Image.open(io.BytesIO(img))
    try:
        return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    except:
        # return cv2.cvtColor(np.array(img), cv2.COLOR_GRAY2BGR)
        print("Failed to conevt to GRAY Scale")

def Arraytob64(array):
    im = Image.fromarray(array.astype("uint8"))
    rawBytes = io.BytesIO()
    im.save(rawBytes, "JPEG")
    rawBytes.seek(0)  # return to the start of the file
    return base64.b64encode(rawBytes.read())