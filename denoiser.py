import cv2
import numpy as np
import math
import sys
 
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
###########
def remove_zero_pad(image):
    dummy = np.argwhere(image != 0) # assume blackground is zero
    max_y = dummy[:, 0].max()
    min_y = dummy[:, 0].min()
    min_x = dummy[:, 1].min()
    max_x = dummy[:, 1].max()
    crop_image = image[min_y:max_y, min_x:max_x]

    return crop_image
###########
#path=r'D:\IITK COURSES\EE604_assign_3_images\noisy1.JPG'
#img = cv2.imread(path)

#median = cv2.medianBlur(img, 5)
#uassian=cv2.GaussianBlur(img,(5,5),0)
#unsharp_image = cv2.addWeighted(median, 2, guassian, -1, 0)
###########
#bilateral = cv2.bilateralFilter(img, 57, 80, 40)

input_file=sys.argv[1]
img=cv2.imread(input_file)
out=img/255
out=out.astype("float32")
planes=[]
val=cv2.split(out)
for i in range(3):
    planes.append(np.uint8(bilateral_fil(val[i], 60, 0.004, 21)*255))
finn=cv2.merge(planes)   
res=remove_zero_pad(finn)


cv2.imwrite('denoised.jpg', res)

cv2.waitKey(0)

cv2.destroyAllWindows