import cv2
import os

sill = 0.5

# img = cv2.imread('schifo.png')
cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 2560)

classNames = []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
    
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
numfiles = len(next(os.walk("output_files"))[2])
frame_size = (int(cap.get(3)), int(cap.get(4)))
output = cv2.VideoWriter("output_files/" + str(numfiles) + ".mp4", fourcc, 30.0, frame_size)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=sill)
    print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId-1], (box[0]+10, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1, (0,255, 0), 2)
            cv2.putText(img, str(round(confidence*100,2)), (box[0]+50, box[1]+60),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    
    output.write(img)
    
    cv2.imshow("Output", img)
    
    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cap.release()
cv2.destroyAllWindows()