from PIL import Image
import io
import numpy as np
import cv2
import base64

def negativeImage(im):
	im = b64toArray(im)

	height=len(im)
	width = len(im[0])
	for row in range(height):
		for col in range(width):
			red = 255-im[row][col][0]
			green = 255-im[row][col][1]
			blue = 255-im[row][col][2]
			im[row][col]=[blue,green,red]

	return Arraytob64(im)


def b64toArray(b64str):
	img = base64.b64decode(b64str)
	img = Image.open(io.BytesIO(img))
	return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

def Arraytob64(array):
	im = Image.fromarray(array.astype("uint8"))
	rawBytes = io.BytesIO()
	im.save(rawBytes, "JPEG")
	rawBytes.seek(0)  # return to the start of the file
	return base64.b64encode(rawBytes.read())