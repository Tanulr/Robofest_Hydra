import cv2
import numpy as np
import time
import serial
ser = serial.Serial('COM5', 9600, timeout=1)

import aruco
from speak import speak_text
video = cv2.VideoCapture(1)
move = 1
while True:
    ret, orig_frame = video.read()
    arucoVal = aruco.arucoFunc(orig_frame)
    if arucoVal == 0:
        #turn left, blink light, tell its turning right
        ser.write(b's')
        string = "Turning left"
        speak_text(string)
    if arucoVal == 1:
        #turn right
        ser.write(b's')
        string = "Turning right"
        speak_text(string)
    frame = cv2.GaussianBlur(orig_frame, (9,9), 0) #(5,5)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    edges = cv2.Canny(frame, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cnts,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)  
        ((x, y), radius) = cv2.minEnclosingCircle(c) 
        center=int(x),int(y)
        print(int(x), int(y))
        #200,400 0
        if move==1:
            if int(x)<250:
                print("left")
                ser.write(b'a')
                time.sleep(1)

            if int(x)>250 and int(x)<450:
                print("forward")
                ser.write(b'w')
                time.sleep(1)

            if int(x)>450:
                print("right")
                ser.write(b'd')
                time.sleep(1)

    if len(cnts) == 0 and move==1:
        print("left")
        ser.write(b'a')
        time.sleep(1)


    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
video.release()