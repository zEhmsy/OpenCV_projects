import cv2
import time
import datetime

from numpy import true_divide

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Video Setting
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DET = 5
# Save video
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            out = cv2.VideoWriter(f"record/{current_time}.mp4", fourcc, 20, frame_size)
            print("Started recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DET:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')
                
        else:
            timer_started = True
            detection_stopped_time = time.time()
    
    if detection:
        out.write(frame)
    
    for (x, y, w, h) in faces:
        # x + w, y + h
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(source, text, center pos, font, font scale, color, thickness, type)
        frame = cv2.putText(frame, 'FACE', (x, w), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, f'{current_time}', (0, 15), font, 0.50, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Camera", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()