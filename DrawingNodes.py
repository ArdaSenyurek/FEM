from cv2 import circle
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
dragging = False
dragCircle = False
circlePos = []
height = 700
width = 700
radius = 20
TempMousePos = ()
color = (100,155,0)
def drawcircle(event, x, y, flags, param):
    global dragging, circlePos, dragCircle, TempMousePos
    if not dragging: #Draw Mode 
        if event == cv.EVENT_RBUTTONDOWN:
            print(img)
        if event == cv.EVENT_MBUTTONDOWN:
            img[np.where(img == 100)] = 0 #clears all circles.
            circlePos = []
        if event == cv.EVENT_LBUTTONDOWN:
            cv.circle(img, (x,y), radius, color, thickness= cv.FILLED)
            circlePos.append((x - radius, x + radius, y - radius, y + radius))
            print(circlePos)
            print(x,y)
    else: #Edit Mode 
        print((x,y))
        if event == cv.EVENT_LBUTTONDOWN:
            dragCircle = True  
            TempMousePos = (x,y)         
        if dragCircle: 
            if event == cv.EVENT_MOUSEMOVE:
                img[TempMousePos[1] - radius -1: TempMousePos[1] + radius + 1, TempMousePos[0] - radius - 1: TempMousePos[0] + radius + 1] = 0 #Eraser.   
                TempMousePos = (x,y)
                if not circlePos == []:
                    cv.circle(img, TempMousePos, radius, color, thickness= cv.FILLED)
        if event == cv.EVENT_LBUTTONUP:
            dragCircle = False
img = np.zeros((height, width), np.uint8)
cv.namedWindow('image')    
cv.setMouseCallback('image', drawcircle)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(5) & 0xFF == 27:
        break
    elif cv.waitKey(10) & 0xFF == ord('e'):
        print('Edit Mode')
        dragging = not dragging

