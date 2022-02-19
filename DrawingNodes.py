#3.02.2022| 13.13
from Field import *
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
dragging = False
dragCircle = False
ActiveDrag = False
circlePos = []
height = 1000
width = 1000
radius = 20
TempMousePos = ()
color = (100,155,0)
counter = 1
f = field(radius)
def drawcircle(event, x, y, flags, param):
    global dragging, circlePos, dragCircle, TempMousePos, counter
    #Draw Mode 
    if not dragging: 
        if event == cv.EVENT_RBUTTONDOWN:
            print(img)
        #clears all circles.
        if event == cv.EVENT_MBUTTONDOWN:
            img[np.where(img == 100)] = 0 
            circlePos = []
            counter = 0
            f.clearNodes()
            print('Field is cleared.')
        if event == cv.EVENT_LBUTTONDOWN:
            
            if f.addNode(Node(counter), x, y) == False:
                pass
            else:
                cv.circle(img, (x,y), radius, color, thickness= cv.FILLED)
                counter += 1 
            circlePos.append((x - radius, x + radius, y - radius, y + radius))
            # print(circlePos)
            # print(x,y)
            # print(f)
    else: #Edit Mode 
        print((x,y))
        if event == cv.EVENT_LBUTTONDOWN:
            dragCircle = True  
            TempMousePos = (x,y)         
        if dragCircle: 
            if event == cv.EVENT_MOUSEMOVE:
                print(img[TempMousePos[1], TempMousePos[0]])
                if img[TempMousePos[1], TempMousePos[0]] == color[0]:    
                    img[TempMousePos[1] - radius -1 : TempMousePos[1] + radius + 1, TempMousePos[0] - radius - 1: TempMousePos[0] + radius + 1] = 0 #Eraser.   
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

