import cv2
import numpy as np
image=cv2.imread("C:\\Users\\KAVIN\\OneDrive\\Pictures\\cherry.jpg")
kernel=np.ones((5,5),dtype='uint8')
erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(image,kernel,iterations=1)
#opening=cv2.morphologyEX(image,cv2.MORPH_OPEN,kernel)
#closing=cv2.morphologyEX(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('original image',image)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
