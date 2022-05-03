import cv2

img = cv2.imread('assets/test.jpeg', -1)

print(img.shape) # (height, width, channels)