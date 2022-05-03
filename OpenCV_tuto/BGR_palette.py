import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

Name = 'OpenCV BGR Color Palette'
cv2.namedWindow(Name)

def emptyFunction(x):
    return

cv2.createTrackbar('B', Name, 0, 255, emptyFunction)
cv2.createTrackbar('G', Name, 0, 255, emptyFunction)
cv2.createTrackbar('R', Name, 0, 255, emptyFunction)

while (True):
    blue = cv2.getTrackbarPos('B', Name)
    green = cv2.getTrackbarPos('G', Name)
    red = cv2.getTrackbarPos('R', Name)
    
    img[:] = [blue, green, red]

    cv2.imshow(Name, img)

    if cv2.waitKey(1) == ord('q'):
        break