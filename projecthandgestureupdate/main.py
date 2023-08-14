import cv2
import time
import os
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)




folderPath = "Fingers"
myList =os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')

    overlayList.append(image)

pTime = 0

#detector
detector = HandDetector(detectionCon=0.7,maxHands=2)
tipIds = [4,8,12,16,20]
while True:
    success, img = cap.read()
    #h, w, c = overlayList[0].shape
    #img[0:h, 0:w] = overlayList[0]

    cTime =time.time()  #fps
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}',(400,70), cv2.FONT_HERSHEY_PLAIN,
                3,(255,0,0),3)


    hands, img = detector.findHands(img) #Draw
    #hands = detector.findHands(img, draw=False)#No Draw


    if hands:
        #hand1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]#21 land marks

        #bbox = hand1["bbox"]
        #centerPoint = hand1["center"]
        #handType1 = hand1["type"]
        #print(handType1)
        #fingers1 = detector.fingersUp(hand1)

        if len(hand1["lmList"]) != 0:
            fingers = []
            #Thumb
            if hand1["lmList"][tipIds[0]] > hand1["lmList"][tipIds[0] - 1]:
                fingers.append(1)
            else:
                fingers.append(0)


            #4 Fingers
            for id in range(1, 5):
                if hand1["lmList"][tipIds[id]] > hand1["lmList"][tipIds[id]-2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            #print(fingers)
            totalFingers = fingers.count(1)
            print(totalFingers)

            h, w, c = overlayList[totalFingers].shape
            img[0:h, 0:w] = overlayList[totalFingers]

#hand2

    if hands:
        # hand1
        hand2 = hands[0]
        lmList2 = hand2["lmList"]  # 21 land marks

        # bbox = hand1["bbox"]
        # centerPoint = hand1["center"]
        # handType1 = hand1["type"]
        # print(handType1)
        # fingers1 = detector.fingersUp(hand1)

        if len(hand2["lmList"]) != 0:
            fingers = []
            # Thumb
            if hand1["lmList"][tipIds[0]] < hand1["lmList"][tipIds[0] - 1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if hand1["lmList"][tipIds[id]] > hand2["lmList"][tipIds[id] - 2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)
            totalFingers = fingers.count(1)
            print(totalFingers)

            h, w, c = overlayList[totalFingers].shape
            img[0:h, 0:w] = overlayList[totalFingers]







    cv2.imshow("Image", img)
    cv2.waitKey(1)