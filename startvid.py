import cv2
import numpy as np
import time
from beepy import *
import datetime 
import sys
import call
import sendsms

def capFunc(*args):
    # loading the nn
    net = cv2.dnn.readNet("./weights/yolov3-tiny.weights", "./cfg/yolov3-tiny.cfg")
    classes = []
    with open ("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # load image
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   

    frame_width = int(cap.get(3)) 
    frame_height = int(cap.get(4)) 
    size = (frame_width, frame_height) 
    result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size) 
    font = cv2.FONT_HERSHEY_PLAIN

    start_time = time.time()
    frame_id = 0
    log_arr = []
    call_flag = 0
    while True:
        _, frame = cap.read()
        frame_id += 1
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result.write(frame) 
        height, width, channels = frame.shape     

        # detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0,0,0), True, crop = False)

        net.setInput(blob)
        outs = net.forward(output_layers)
        # print(outs)

        boxes = []
        confidences = []
        class_ids = []
        for out in outs:
            for detection in out:
                # print(detection)
                scores = detection[5:]
                # print(scores)
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)   
                    y = int(center_y - h / 2) 

                    boxes.append([x,y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # print(len(boxes))
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        human_check = []
        # print(indexes)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                if label not in human_check:
                    human_check.append(label)
                    if "person" in human_check:
                        call_flag += 1
                        if call_flag == 1:
                            call.makeCall()
                            sendsms.send()
                            print("sms generated")
                            print("call generated")
                        else:
                            pass
                        # beep(sound=1)
                        print("intrusion detected")
                        get_date = str(datetime.datetime.now()) + "\n"
                        # log_arr.append(str(datetime.datetime.now()))
                        # log_arr.append("\n")
                        log_arr.append(get_date)
                        frame_width = int(cap.get(3)) 
                        frame_height = int(cap.get(4)) 
       
                        size = (frame_width, frame_height) 
                            
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
                cv2.putText(frame, label, (x, y + 30), font, 3, (0,255,0), 3)

        elapsed_time = time.time() - start_time
        fps = round(frame_id / elapsed_time, 2)
        cv2.putText(frame, "fps = " + str(fps), (10, 50), font, 2, (0,0,0), 2)
        cv2.namedWindow('output',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('output', 600,600)
        cv2.imshow("output", frame)
        key = cv2.waitKey(1)  
        if key == 27:
            break

    path = 'time_stamp.txt'
    str1 = ''.join(log_arr)
    log_file = open(path, 'w+')
    log_file.write(str1)
    log_file.close()
    cap.release()
    result.release() 
    cv2.destroyAllWindows()
    print(human_check)