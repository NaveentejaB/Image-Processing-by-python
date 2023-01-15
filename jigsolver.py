import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
input_file=sys.argv[1]
image=cv2.imread(input_file)
image_open=image.copy()
part1 =image_open.copy()[0:200,0:190]
part2 =image_open.copy()[200:410,0:190]
part3 =image_open.copy()[150:330,515:700]
part4 =image_open.copy()[370:421,370:798]
g1=part1.copy()[:,:,1]
b1=part1.copy()[:,:,0]
part1[:,:,0]=g1
part1[:,:,1]=b1
image_open[370:421,370:798]=np.flip(part4,0)
#image_open[190:390,0:190]=part1
image_open[150:330,515:700]=np.flip(part3,1)
part2=np.flip(part2,0)

part1_padd=cv2.copyMakeBorder(part1,0,8,0,0,cv2.BORDER_REPLICATE)
image_open[200:408,0:190,:]=part1_padd
part5=cv2.copyMakeBorder(image_open[410:412,0:190,:],2,0,0,0,cv2.BORDER_REFLECT)
image_open[408:412,0:190,:]=part5
image_open[0:200,0:190,:]=part2[0:200,0:190,:]
#directory=r'C:\Users\Teja\Downloads\EE604-Assign1-pictures'
#print('before saving image')
#print(os.listdir(directory))
#os.chdir(directory)
cwd = os.getcwd()
cv2.imwrite('saved image.jpg',image_open)
cv2.imshow('image',image_open)
print('after saving image')
#print(os.listdir(directory))
os.chdir(directory)
cv2.waitKey(0)
cv2.destroyAllWindows()

