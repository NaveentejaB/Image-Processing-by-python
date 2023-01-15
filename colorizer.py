import cv2
import numpy as np
import math
import sys
from PIL import Image
#########  functions  ###########
########  o change the colour space from ycbcr to rgb  #########
def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)

    rgb[:,:,[1,2]] -= 128
    return np.uint8(rgb.dot(xform.T))
#########################################
######### bilateral filtering ###########
def vec_gaussian(img: np.ndarray, vari: float) -> np.ndarray:
    # For applying gaussian function for each element in matrix.
    sigma = math.sqrt(vari)
    cons = 1 / (sigma * math.sqrt(2 * math.pi))
    return cons * np.exp(-((img / sigma) ** 2) * 0.5)

# spa_vari = spatial varience  inte_vari = intensity varience#
def bilateral_fil(img: np.ndarray,spa_vari: float, inte_vari: float,k_size: int)-> np.ndarray:
    res = np.zeros(img.shape)

    #to create the guassian kernel of given dimensions
    gaus_ker = np.zeros((k_size, k_size))
    for i in range(0, k_size):
        for j in range(0, k_size):
            gaus_ker[i, j] = math.sqrt(abs(i - k_size // 2) ** 2 + abs(j - k_size // 2) ** 2)
    gaussKer=vec_gaussian(gaus_ker, spa_vari)
    
    sizeX,sizeY=img.shape
    for i in range(k_size // 2, sizeX - k_size // 2):
        for j in range(k_size // 2, sizeY - k_size // 2):
            half = k_size // 2
            imgS=img[i - half : i + half + 1, j - half : j + half + 1]
            imgI = imgS - imgS[half, half]
            imgIG = vec_gaussian(imgI, inte_vari)
            weights = np.multiply(gaussKer, imgIG)
            vals = np.multiply(imgS, weights)
            val = np.sum(vals) / np.sum(weights)
            res[i, j] = val
    return res
###############################################
###############################################
###### main code #########
#pathcbr=r'D:\IITK COURSES\EE604_assign_3_images\Cb4.jpg'
#pathcr=r'D:\IITK COURSES\EE604_assign_3_images\Cr4.jpg'
#pathY=r'D:\IITK COURSES\EE604_assign_3_images\Y.jpg'
input_Y=sys.argv[1]
input_cb=sys.argv[2]
input_cr=sys.argv[3]
imgY=cv2.imread(input_Y)
imgCbr=cv2.imread(input_cb)
#blCb= cv2.bilateralFilter(imgCbr, 31, 20, 20)
imgCr=cv2.imread(input_cr)
#blCr= cv2.bilateralFilter(imgCr, 71, 15, 15)
##
icr=cv2.pyrUp(imgCr)
icr1=cv2.pyrUp(icr)

##
icbr=cv2.pyrUp(imgCbr)
icbr1=cv2.pyrUp(icbr)
##
imgYf=cv2.copyMakeBorder(imgY,0,2,0,0,cv2.BORDER_CONSTANT,0)
##
y=cv2.split(imgYf)
cr=cv2.split(icr1)
cb=cv2.split(icbr1)

fin=cv2.merge([y[0],cr[0],cb[0]])
fin1=cv2.merge([y[1],cr[1],cb[1]])
fin2=cv2.merge([y[2],cr[2],cb[2]])

final_dup=cv2.addWeighted(fin,0.5,fin1,0.5,0)
final=cv2.addWeighted(final_dup,0.5,fin2,0.5,0)
#bilateral1= cv2.bilateralFilter(final, 91, 50, 80)
#bilateral2=bilateral_fil(final, 91, 50, 21)
#cv2.imshow('sdfsd',icr1)
outt=(final/255.0).astype("float32")
ycbcr_pln=[]
spi=cv2.split(outt)
for i in range(3):
    ycbcr_pln.append(np.uint8(bilateral_fil(spi[i], 41, 0.0045, 21)*255))
    
nav = cv2.merge(ycbcr_pln)
teja=ycbcr2rgb(nav)

size=teja.shape
#im1 = teja.crop((10, 10, 950, 614))
appu=teja[ 10:614,10:950]
#cv2.imshow('ffssff',appu)
cv2.imwrite('flyingelephant.jpg',appu)
#cv2.imwrite('image.jpg',teja)
cv2.waitKey(0)
cv2.destroyAllWindows