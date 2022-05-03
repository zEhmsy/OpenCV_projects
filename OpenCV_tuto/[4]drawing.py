import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # cv2.line(source image, starting position, ending position, color, thickness)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 10)
    
    # cv2.rectangle(source image, center position, radius, color, thickness (-1 to fill))
    img = cv2.rectangle(img, (100, 100), (200,200), (128,128,128), 5)
    
    # cv2.circle(source, center position, radius, color, thickness (-1 to fill))
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    
    # Draw text
    font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(source, text, center pos, font, font scale, color, thickness, type)
    img = cv2.putText(img, 'Michael', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
        
    cv2.imshow('Camera', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()