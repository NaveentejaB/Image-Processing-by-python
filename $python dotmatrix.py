import os
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
#to make the the required circles to darken according to the input
def making_dig(circle_img,mydic,num):
    clr_blc=(0,0,0)
    if (num==0):
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[8],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
    if(num==1):
        for i in range(1,16,3):
            circle_img=cv2.circle(circle_img,mydic[i],30,clr_blc,-1)
        for j in range(3,18,3):
            circle_img=cv2.circle(circle_img,mydic[j],30,clr_blc,-1)
    if(num==2):
        circle_img=cv2.circle(circle_img,mydic[4],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[12],30,clr_blc,-1)
    if(num==3):
        circle_img=cv2.circle(circle_img,mydic[4],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[10],30,clr_blc,-1)
    if(num==4):
        circle_img=cv2.circle(circle_img,mydic[2],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[10],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[13],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[14],30,clr_blc,-1) 
    if (num==5):
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[6],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[10],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
    if (num==6):
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[6],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
    if (num ==7):
        for i in range(4,16,3):
            circle_img=cv2.circle(circle_img,mydic[i],30,clr_blc,-1)
        for j in range(5,17,3):
            circle_img=cv2.circle(circle_img,mydic[j],30,clr_blc,-1)
    if(num == 8):
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)
    if(num == 9):
        circle_img=cv2.circle(circle_img,mydic[5],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[10],30,clr_blc,-1)
        circle_img=cv2.circle(circle_img,mydic[11],30,clr_blc,-1)  
    return circle_img
#for making the digits....
def make_img(num,mydic,mydic1,img):
    tens=0
    ones=0
    if(num<10):
        ones=num
        tens=0
        img=making_dig(img, mydic1, ones)
        img=making_dig(img, mydic, tens)
    else:
        ones=num%10
        tens=num%100 //10
        img=making_dig(img, mydic1, ones)
        img=making_dig(img, mydic, tens)
    return img
        
    
num=int(input("enter the number: "))
#to make a grid of circles of white colour
blank_img=np.zeros((300,500,3),np.uint8)
circle_img=blank_img.copy()
radius=25
thck=-1
offset=10
x=25+offset+20
y=25+offset
centre_cor=(x,y)
color=(255,255,255)
for i in range(1,8):
    for j in range(1,8):
        centre_cor=(x,y)
        if  j!=4 :
            circle_img=cv2.circle(circle_img,centre_cor,radius,color,thck)
        x=x+2*radius+offset
    y=y+2*radius+offset
    x=radius+offset+20
#ended
#the co-ordinates of the centres of circles
mydic={1 :(50,35),2:(110,35),3:(170,35),4:(50,95),5:(110,95),6:(170,95),7:(50,155),8:(110,155),
       9:(170,155),10:(50,215),11:(110,215),12:(170,215),13:(50,275),14:(110,275),15:(170,275)}
mydic1={1 :(290,35),2:(350,35),3:(410,35),4:(290,95),5:(350,95),6:(410,95),7:(290,155),8:(350,155),
       9:(410,155),10:(290,215),11:(350,215),12:(410,215),13:(290,275),14:(350,275),15:(410,275)}
img=make_img(num, mydic, mydic1, circle_img)
cur_direc= os.getcwd()
cv2.imwrite('dotmatrix.jpg',img)
cv2.imshow('image',img)
#print(os.listdir(directory))
cv2.waitKey(0)
cv2.destroyAllWindows()
