import cv2
import numpy as np
import sys

#path=r'D:\IITK COURSES\EE604_assign_3_images\WhatsApp Image 2022-11-10 at 03.01.08 (1).jpeg'
#img=cv2.imread(path)
input_file=sys.argv[1]
img=cv2.imread(input_file)
#  1-building 2-grass 3-road
gb=np.array([[0,6],[0,80],[7,20]])
g2rb=np.array([[1,8],[12,85],[0,12]])
x=img.shape
size=x[0]*x[1]
tot_gb=0
tot_g2rb=0
for i in range(x[0]):
    for j in range(x[1]):
        v=(img[i][j]).astype(int)
        tot_gb += abs (v[1]-v[2])
        tot_g2rb += (abs(v[1]-v[0]) + abs (v[1]-v[2]))
avg_gb=tot_gb/size
avg_g2rb=tot_g2rb/size
print(avg_gb)
print(avg_g2rb)
val=0
for i in range(3):
    if (avg_gb >= gb[i][0] and avg_gb <= gb[i][1]):
        if(avg_g2rb >= g2rb[i][0] and avg_g2rb <= g2rb[i][1]):
            v=i+1
print(v)