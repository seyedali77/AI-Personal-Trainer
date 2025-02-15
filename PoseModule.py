import cv2
import mediapipe as mp
import time
import math


class poseDetector():
    def __init__(self, mode=False, modelcomplexity=1, smoothlandmark=True, enableseg=False,
                 smoothseg=True, detectioncon=0.5, trackingcon=0.5):

        # Initialize pose estimation parameters
        self.mode = mode
        self.modelcomplexity = modelcomplexity
        self.smoothlandmark = smoothlandmark
        self.enableseg = enableseg
        self.smoothseg = smoothseg
        self.detectioncon = detectioncon
        self.trackingcon = trackingcon

        # Load MediaPipe pose detection model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.modelcomplexity, self.smoothlandmark,
                                     self.enableseg, self.smoothseg, self.detectioncon,
                                     self.trackingcon)

    def findPose(self, img, draw=True):
        # Convert image to RGB format (required by MediaPipe)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                # Draw pose landmarks on the image
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosotion(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # Convert normalized landmark coordinates to pixel values
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])

                if draw:
                    # Draw a circle at the landmark position
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        #Get the landmarks
        x1, y1  = self.lmList[p1][1:]
        x2, y2  = self.lmList[p2][1:]
        x3, y3  = self.lmList[p3][1:]

        #Calculate the Angle
        angle = math.degrees(math.atan2(y1-y2, x1-x2)-
                            math.atan2(y3-y2, x3-x2))

        if angle < 0:
            angle += 360

        # print(angle)


        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0,255,0),3)
            cv2.line(img, (x3, y3), (x2, y2), (0,255,0),3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            # cv2.putText(img, str(int(angle)), (x2 -20, y2+50),
            #             cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
        return angle

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        if not success:
            break  # Stop loop if video ends or there's an issue

        img = detector.findPose(img)
        lmList = detector.findPosotion(img, draw=False)

        if len(lmList) != 0:
            # Highlight a specific landmark (e.g., elbow at index 14)
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        # Calculate and display FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Resize and display the image
        img_resized = cv2.resize(img, (800, 500))
        cv2.imshow("Image", img_resized)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()












