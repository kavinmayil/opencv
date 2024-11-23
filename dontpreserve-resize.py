import cv2
img = cv2.imread("C:\\Users\\KAVIN\\OneDrive\\Pictures\\cherry.jpg")
#width=img.shape[1]
width=440
height=img.shape[0]
#height=440
dim=(width,height)
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('original',img)
cv2.imshow('resized',resized)
cv2.waitKey()
cv2.destroyAllWindows()
