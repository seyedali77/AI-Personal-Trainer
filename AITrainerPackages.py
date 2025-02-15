import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("6.mp4")
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (620, 620))
    # img = cv2.imread("Personal AI Trainer/test2.png")
    img = detector.findPose(img, False)
    lmList = detector.findPosotion(img, False)
    # print(lmList)
    if len(lmList) != 0 :
        #Right Arm
        angle = detector.findAngle(img, 11, 13, 15)
        # #Left Arm
        # detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (90,130), (0,100))
        bar = np.interp(angle, (90,130), (650, 100))
        # print(angle, per)

        # Check for the dumble curls
        color = (255,0,255)
        if per == 100:
            color = (0,255,0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        print(count)

        #Draw bar
        cv2.rectangle(img, (480,100), (530,600), color, 3)
        cv2.rectangle(img, (480,int(bar)), (530,600), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (480, 40), cv2.FONT_HERSHEY_PLAIN, 3,
                    color, 4)

        #Draw counting
        cv2.rectangle(img, (0,450), (250,620), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 620), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255,0,0), 25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)