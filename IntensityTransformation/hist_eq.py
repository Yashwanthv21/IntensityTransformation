from PIL import Image
import io
import numpy as np
import cv2
import base64

def histogram_equalization(im):
	im= b64toArray(im)
	img = im

	M,N=img.shape
	hist=[0 for i in range(256)]
	for i in range(M):
		for j in range(N):
			hist[img[i,j]]=hist[img[i,j]]+1
	cdf = [sum(hist[:i+1]) for i in range(len(hist))]
	cdf1=[0 for i in range(256)]
	m1 = min(i for i in cdf if i > 0)
	m2=np.max(cdf)
	c=m2-m1
	for i in range(256):
		if(cdf[i]>0):
			cdf1[i]=(cdf[i]-m1)*255/(c)
	else:
		cdf1[i]=cdf[i]
	new_img=np.zeros((int(M),int(N)),np.uint8)
	for i in range(M):
		for j in range(N):
			new_img[i, j] = cdf1[img[i, j]]

	equalized_hist=[0 for i in range(256)]
	for i in range(M):
		for j in range(N):
			equalized_hist[new_img[i,j]]=equalized_hist[new_img[i,j]]+1


	return Arraytob64(new_img)


def b64toArray(b64str):
	img = base64.b64decode(b64str)
	img = Image.open(io.BytesIO(img))
	return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)

def Arraytob64(array):
	im = Image.fromarray(array.astype("uint8"))
	rawBytes = io.BytesIO()
	im.save(rawBytes, "JPEG")
	rawBytes.seek(0)  # return to the start of the file
	return base64.b64encode(rawBytes.read())
