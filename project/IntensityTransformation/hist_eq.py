
import io
import numpy as np
import cv2
import base64
from PIL import Image

def histogram_equalization(im):
    im= b64toArray(im)
    img = im
    M=len(img)
    N = len(img[0])

    histx=histy=histz=[0 for i in range(256)]
    for i in range(M):
        for j in range(N):
            histx[img[i,j,0]]=histx[img[i,j,0]]+1
            histy[img[i,j,1]]=histy[img[i,j,1]]+1
            histz[img[i,j,2]]=histz[img[i,j,2]]+1
    cdfx = [sum(histx[:i+1]) for i in range(len(histx))]
    cdfy =[sum(histy[:i+1]) for i in range(len(histy))]
    cdfz =[sum(histz[:i+1]) for i in range(len(histz))]
    cdfx1=cdfy1=cdfz1=[0 for i in range(256)]
    mx1 = min(i for i in cdfx if i > 0)
    my1 = min(i for i in cdfy if i > 0)
    mz1 = min(i for i in cdfz if i > 0)
    mx2=np.max(cdfx)
    my2=np.max(cdfy)
    mz2=np.max(cdfz)
    cx=mx2-mx1
    cy=my2-my1
    cz=mz2-mz1
    for i in range(256):
        if(cdfx[i]>0):
            cdfx1[i]=(cdfx[i]-mx1)*255/(cx)
        else:
            cdfx1[i]=cdfx[i]
    for i in range(256):
        if(cdfy[i]>0):
            cdfy1[i]=(cdfy[i]-my1)*255/(cy)
        else:
            cdfy1[i]=cdfy[i]
    for i in range(256):
        if(cdfz[i]>0):
            cdfz1[i]=(cdfz[i]-mz1)*255/(cz)
        else:
            cdfz1[i]=cdfz[i]
    
    new_img=im.copy()
    for i in range(M):
        for j in range(N):
            new_img[i, j,0] = cdfx1[img[i, j,2]]
            new_img[i, j,1] = cdfy1[img[i, j,1]]
            new_img[i, j,2] = cdfz1[img[i, j,0]]
    
    equalized_hist=[0 for i in range(256)]
    for i in range(M):
        for j in range(N):
            equalized_hist[new_img[i,j,0]]=equalized_hist[new_img[i,j,0]]+1

    return Arraytob64(new_img)


def b64toArray(b64str):
    img = base64.b64decode(b64str)
    img = Image.open(io.BytesIO(img))
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)


def Arraytob64(array):
    im = Image.fromarray(array)
    rawBytes = io.BytesIO()
    im.save(rawBytes, "JPEG")
    rawBytes.seek(0)  # return to the start of the file
    return base64.b64encode(rawBytes.read())
    
    #return base64.b64encode(array)


'''


from PIL import Image
import io
import numpy as np
import cv2
import base64






def histogram_equalization(im):
	im= b64toArray(im)
	img = im

	# M,N=img.shape
	M=len(im)
	N = len(im[0])
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
'''















from PIL import Image
import io
import numpy as np
import cv2
import base64

def histogram_equalization(im):
	im= b64toArray(im)
	img = im

	# M,N=img.shape
	M=len(im)
	N = len(im[0])
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


	return Arraytob64(new_img),hist,equalized_hist


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
'''