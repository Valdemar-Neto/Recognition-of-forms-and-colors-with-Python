import cv2

image = cv2.imread('formas.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

#_, th = cv2.threshold(gray, 10, 155, cv2.THRESH_BINARY)
ctns,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image, ctns, -1, (255,255,255), 2)

for c in ctns:
    epsilon = 0.01 *cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    print(len(approx))

    x,y,w,h = cv2.boundingRect(approx)

    if len(approx) == 3:
        cv2.putText(image, "Triangulo", (x-5, y-15),1,1,(255,255,255),1)
    if len(approx) == 4:
        aspect_ratio = float(w)/h
        print("Aspect ratio", aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(image, "Quadrado", (x,y-20), 1,1,(255,255,255), 1)
        else:
            cv2.putText(image, "Retangulo", (x,y-20), 1, 1, (255,255,255),1)
    if len(approx) == 5:
        cv2.putText(image, "Pentagono", (x,y-20),1,1,(255,255,255),1)
    if len(approx) == 6:
        cv2.putText(image, "Hexagono", (x, y-20), 1, 1, (255,255,255),1)
    if len(approx) == 10:
        cv2.putText(image, "Decagono", (x, y-20),1, 1,(255,255,255),1)
    if len(approx) == 12:
        cv2.putText(image, "Duodecagono", (x, y-20), 1, 1,(255,255,255),1)
    if len(approx) > 12:
        cv2.putText(image, "circulo", (x, y-20), 1, 1, (255,255,255),1)

    cv2.drawContours(image, [approx], -1, (255,255,255), 4)
    cv2.imshow("image", image)
    cv2.waitKey(0)

cv2.imshow("image", image)
#cv2.imshow("canny", canny)
#cv2.imshow("th", th)
cv2.waitKey(0)
cv2.destroyAllWindows()