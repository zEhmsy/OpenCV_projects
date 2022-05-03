import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # Convert a BGR tu HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([145, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Filtra solo il colore blu
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    #Visualizzazione
    image = np.zeros(frame.shape, np.uint8)
    mask_frame = cv2.resize(mask, (0,0), fx=0.5, fy=0.5)
    blue_filter = cv2.resize(result, (0,0), fx=0.5, fy=0.5)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    hsv_frame = cv2.resize(hsv, (0,0), fx=0.5, fy=0.5)
    
    # Aggiungo una dimensione alle maschera
    mask_frame = np.expand_dims(mask_frame, axis=2)
    
    image[:height//2, :width//2] = smaller_frame # top_left
    image[height//2:, :width//2] = hsv_frame # bot_left
    image[:height//2, width//2:] = mask_frame # top_right
    image[height//2:, width//2:] = blue_filter # bot_right
    
    # Draw text
    font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(source, text, center pos, font, font scale, color, thickness, type)
    image = cv2.putText(image, 'Normale', (0, 25), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image = cv2.putText(image, 'Maschera', (width-150, 25), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    image = cv2.putText(image, 'BLUE', (width-80, height-5), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    image = cv2.putText(image, 'HSV', (0, height-5), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('Camera', image)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()