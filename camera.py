import cv2
import numpy as np

def mostrar(mask, cor):
    contornos,_= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        if area > 3000:
            m= cv2.moments(c)
            if(m["m00"]==0): m["m00"]==1
            x = int(m["m10"]/m["m00"])
            y = int(m["m01"]/m["m00"])
            newContour = cv2.convexHull(c)
            cv2.rectangle(frame, (x, 10), (y, 10), (255,255,255),2)
            cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)
            cv2.drawContours(frame, [newContour],0,cor, 3)

camera = cv2.VideoCapture(0)

blueLow = np.array([100, 100,20], np.uint8)
blueHigh = np.array([125, 255, 255], np.uint8)

yellowLow = np.array([15, 103, 20], np.uint8)
yellowHigh = np.array([45, 255,255], np.uint8)

redHigh = np.array([0,100,20],np.uint8)
redLow = np.array([5,255,255],np.uint8)

redHigh2 = np.array([175, 100, 20], np.uint8)
redLow2 = np.array([179, 255, 255], np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret,frame = camera.read()
    if ret==True:
        frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV,blueLow, blueHigh)
        maskYellow = cv2.inRange(frameHSV,yellowLow,yellowHigh)
        maskRed1=cv2.inRange(frameHSV, redHigh, redLow)
        maskRed2=cv2.inRange(frameHSV, redHigh2, redLow2)
        maskRed=cv2.add(maskRed1,maskRed2)

        mostrar(maskBlue,(255,0,0))
        mostrar(maskYellow,(0,255,255))
        mostrar(maskRed,(0,0,255))


        #cv2.imshow("mask cor", maskcor)
        #cv2.imshow("mask", maskRed)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
camera.release()
cv2.destroyAllWindows()
