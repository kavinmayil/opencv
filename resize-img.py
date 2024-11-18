import cv2
img = cv2.imread("C:\\Users\\KAVIN\\OneDrive\\Pictures\\LUFFY.jpg")
print("original dimension:",img.shape)
#width=img.shape[1]
width=500
height=img.shape[0]
#height=300
dim=(width,height)
#dim=(200,300)
resize=cv2.resize(img,dim)
cv2.imshow('resized image',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print("current dimension",dim)
