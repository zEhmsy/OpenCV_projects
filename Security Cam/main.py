import datetime
import cv2
import numpy as np
import os

video = cv2.VideoCapture(0)
sill = 450000

record_buffer_max = 15
record_buffer = 0

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
numfiles = len(next(os.walk("output_files"))[2])
frame_size = (int(video.get(3)), int(video.get(4)))
output = cv2.VideoWriter("output_files/" + str(numfiles) + ".mp4", fourcc, 30.0, frame_size)



while True:
    now = datetime.datetime.now()
    _, frame = video.read()
    _, last_frame = video.read()
    net_diff = 0.0
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray_last = cv2.cvtColor(last_frame, cv2.COLOR_RGB2GRAY)
    
    diff = cv2.absdiff(gray, gray_last)
    blur = cv2.GaussianBlur(diff, (5,5),0)
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate (threshold, None, iterations=3)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea (c) < 5000:
            continue
        #cv2.drawContours (frame, contours, -1, (0, 255, 0), 2)
        x,y,w,h = cv2.boundingRect (c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        record_buffer = record_buffer_max

    w = np.size(diff, 0)
    h = np.size(diff, 1)
    
    
    
    for i in range(0, w):
        for j in range(0, h):
            if i % 5 == 0 & j % 5 == 0:
                r = diff[i, j] 
                g = diff[i, j]
                b = diff[i, j]
                
                net_diff += (r + g + b)
        
    cv2.rectangle(frame, (int(video.get(3)) - 254, int(video.get(4) - 70)), (int(video.get(3)) - 30, int(video.get(4) - 35)), (0, 0, 0), -10)
    cv2.putText (frame, now.strftime("%d/%m/%Y %H:%M:%S"), (int(video.get(3)) - 250, int(video.get(4) - 50)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    if record_buffer < 0:
        cv2.putText(frame, "Not Moving", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Moving", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        output.write(frame)
    record_buffer -= 1
    if record_buffer < -100:
        record_buffer = -100
    
    image = np.zeros((720, 960*2, 3), np.uint8)
    threshold = cv2.resize(threshold, (0,0), fx=1.5, fy=1.5)
    threshold = np.expand_dims(threshold, axis=2)
    frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
    image[:720, :960] = threshold
    image[:720, 960:] = frame 
    
    cv2.imshow("Security Camera", image)
    #cv2.imshow("Security Camera", frame)
    last_frame = frame
    
    if cv2.waitKey(1) == ord('q'):
        break

output.release()
video.release()
cv2.destroyAllWindows()