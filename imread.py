import cv2
import numpy as np


#泛洪填充(彩色图像填充）
def fill_color_demo(image):
   copyImg =image.copy()
  # h, w=image.shape[:2]#image.shape属性是读入图片后的一个元组tuple，返回图片的(高,宽,位深)
   h,w,_=image.shape#h,w,d = image.shape
   mask =np.zeros([h+2,w+2],np.uint8)
   cv2.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv2.FLOODFILL_FIXED_RANGE)
   cv2.imshow('fill_color_demo',copyImg)

#二值图像填充
def fill_binary():
   image =np.zeros([400,400,3],np.uint8)
   image[100:300,100:300,:] = 255
   cv2.imshow('fill_binary',image)


   mask =np.ones([402,402,1],np.uint8)
   mask[101:301,101:301] = 0
   cv2.floodFill(image,mask,(200,200),(0,0,255),cv2.FLOODFILL_MASK_ONLY)
   cv2.imshow('filled_binary',image)


src =cv2.imread('e:/cat.jpg')
new =cv2.resize(src,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)#对原图像进行缩小
cv2.namedWindow('cat')
cv2.imshow('cat',new)
fill_color_demo(new)
fill_binary()
cv2.waitKey(0)
cv2.destroyAllWindows()