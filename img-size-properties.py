import cv2
img = cv2.imread("C:\\Users\\KAVIN\\OneDrive\\Pictures\\cherry.jpg")
shape=img.shape
height=img.shape[0]
width=img.shape[1]
channel=img.shape[2]
size=img.size
print('image shape:',shape)
print('image height:',height)
print('image width:',width)
print('image channel:',channel)
print('image size in bytes:',size)

#(output:
# mage shape: (414, 736, 3) ,image height: 414 ,image width: 736 ,image channel: 3
#image size in bytes: 914112)
