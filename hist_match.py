#from scipy.misc import imsave, imread
import numpy as np
import cv2
import base64
from PIL import Image
import io

def histatch(imsrc, imtint):
    imsrc = b64toArray(imsrc)
    imtint=b64toArray(imtint)
    values_int= 255
    if len(imsrc.shape) < 3:
        imsrc = imsrc[:,:,np.newaxis]
        imtint = imtint[:,:,np.newaxis]
    imres = imsrc.copy()
    for d in range(imsrc.shape[2]):
        srcimage,bins = np.histogram(imsrc[:,:,d].flatten(),values_int,normed=True)
        destimage,bins = np.histogram(imtint[:,:,d].flatten(),values_int,normed=True)
        value_cdf_src  = srcimage.cumsum()
        value_cdf_src = (255 * value_cdf_src / value_cdf_src[-1]).astype(np.uint8)
        value_cdf_dest  = destimage.cumsum()
        value_cdf_dest = (255 * value_cdf_dest / value_cdf_dest[-1]).astype(np.uint8)
        image2  = np.interp(imsrc[:,:,d].flatten(),bins[:-1],value_cdf_src)
        image3  = np.interp(image2,value_cdf_dest, bins[:-1])
        imres[:,:,d] = image3.reshape((imsrc.shape[0],imsrc.shape[1] ))

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