import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import random
import time

#webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

#find function
#x is the distance and y is value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2) #y=ax^2 + bx + c

#game variable
cx = random.randint(100, 1100)
cy = random.randint(100, 600)
col = (0, 0, 255)
counter = 0
score = 0
timestart = time.time()
totaltime = 20

#loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if time.time() - timestart < totaltime:

        hands, img = detector.findHands(img, draw=False)

        if hands:
            lmlist = hands[0]['lmList']
            x, y, w, h = hands[0]['bbox']
            #print(lmlist)
            x1, y1, z1 = lmlist[5]
            x2, y2, z2 = lmlist[17]

            dist = int(((y2-y1)**2 + (x2-x1)**2)**0.5)
            A, B, C = coff
            #distance in cm
            distance = A*dist**2 + B*dist + C
            #print(distance)

            if distance<40:
                if x < cx < x+w and y < cy < y+h:
                    counter = 1
            
            if counter:
                counter +=1
                col = (0, 255, 0)
                if counter == 3:
                    cx = random.randint(100, 1100)
                    cy = random.randint(100, 600)
                    col = (0, 0, 255)
                    score += 1
                    counter = 0

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
            cvzone.putTextRect(img, f'{int(distance)} cm', (x,y))

        #draw button
        cv2.circle(img, (cx,cy), 30, col, cv2.FILLED)
        cv2.circle(img, (cx,cy), 20, (255,255,255), 2)
        cv2.circle(img, (cx,cy), 10, (255,255,255), cv2.FILLED)

        #game disp
        cvzone.putTextRect(img,f'Time: {int(totaltime-(time.time()-timestart))}', (1000, 75), scale=3, offset=20)
        cvzone.putTextRect(img, f'Score: {str(score).zfill(2)}', (60, 75), scale=3, offset=20)

    else: 
        cvzone.putTextRect(img,'Game Over', (400, 400), scale=5, offset=30, thickness=7)
        cvzone.putTextRect(img, f'Your Score: {score}', (425, 500), scale=3, offset=20)
        cvzone.putTextRect(img, "Press R to restart", (400, 575), scale=3, offset=10)



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        score = 0
        timestart = time.time()
