#from scipy.misc import imsave, imread
import numpy as np
import cv2
import base64
from PIL import Image
import io

def histmatch(imsrc, imtint):
    imsrc = b64toArray(imsrc)
    imtint=b64toArray(imtint)

    nbr_bins=255
    if len(imsrc.shape) < 3:
        imsrc = imsrc[:,:,np.newaxis]
        imtint = imtint[:,:,np.newaxis]

    imres = imsrc.copy()
    for d in range(imsrc.shape[2]):
        imhist,bins = np.histogram(imsrc[:,:,d].flatten(),nbr_bins,normed=True)
        tinthist,bins = np.histogram(imtint[:,:,d].flatten(),nbr_bins,normed=True)

        cdfsrc = imhist.cumsum() #cumulative distribution function
        cdfsrc = (255 * cdfsrc / cdfsrc[-1]).astype(np.uint8) #normalize

        cdftint = tinthist.cumsum() #cumulative distribution function
        cdftint = (255 * cdftint / cdftint[-1]).astype(np.uint8) #normalize

        im2 = np.interp(imsrc[:,:,d].flatten(),bins[:-1],cdfsrc)
        im3 = np.interp(im2,cdftint, bins[:-1])
        imres[:,:,d] = im3.reshape((imsrc.shape[0],imsrc.shape[1] ))


    return Arraytob64(imres)

#result = cv2.imread("histnormresult.jpg", 0)
#image_hist3 = histogram(result)
#plt.plot(image_hist3)
#plt.show()


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