import cv2
import numpy as np
img=cv2.imread("venv/resources/shapes.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),1)
canny=cv2.Canny(blur,50,50)
copy=img.copy()
a=input("enter a shape")
if a=="triangle":
    j=3
elif a=="square":
    j=4
elif a=="rectangle":
    j=4
elif a=="trapezium":
    j=4
elif a=="pentagon":
    j=5
elif a=="hexagon":
    j=6
elif a=="heptagon":
    j=7
elif a=="oval" or a=="circle" or a=="octagon":
    j=8
def ctr(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(copy,cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        points = (len(approx))
        x, y, w, h = cv2.boundingRect(approx)
        if points == j:
            cv2.rectangle(copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(a+" detected within green box")
ctr(canny)
cv2.imshow("cnt", copy)
cv2.waitKey(0)
