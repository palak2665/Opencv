import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False,maxhands = 2,modelComplexity=1, detectionconf = 0.5,trackconf = 0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.modelComplex = modelComplexity
        self.detectionconf = detectionconf
        self.trackconf = trackconf


        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.maxhands,self.modelComplex, self.detectionconf, self.trackconf)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)     

        if self.results.multi_hand_landmarks :
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mphands.HAND_CONNECTIONS)
               
        return img       

    def findPosition(self, img, handNo=0, draw = True):
        lmlist = []

        if self.results.multi_hand_landmarks :
            myhand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w) , int(lm.y*h)
                #print(id, cx,cy)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
        return lmlist

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist)!=0:
            print(lmlist[0])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),2)

        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

if __name__ == "__main__":
    main()