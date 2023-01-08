from turtle import pos
import keyboard
import pyautogui
import PIL
import time
import random as rand


import pytesseract
from pytesseract import Output
import cv2
import numpy as nm
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
  
def seeTroutCatchTrout():
    cap_x = 900
    cap_y = 100
    cap_x2 = 1250
    cap_y2 = 1100

    capture = ImageGrab.grab(bbox =(cap_x,cap_y,cap_x2,cap_y2))
    img = nm.array(capture.convert("RGB"))
    results = pytesseract.image_to_data(img, output_type=Output.DICT)

    n_boxes = len(results['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (results['left'][i], results['top'][i], results['width'][i], results['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    print(results["text"])
    
    if "Trout" in results["text"]:
        troutIndex = results["text"].index("Trout")
        troutX = results["left"][troutIndex] + cap_x -20
        troutY = results["top"][troutIndex] + cap_y +10
        pyautogui.moveTo(troutX,troutY) #move mouse to random point. if point is clicked directly, client will not recognize
        time.sleep(1)
        pyautogui.click(troutX,troutY) #perform click
        return(True)
    elif "Traut" in results["text"]:
        troutIndex = results["text"].index("Trout")
        troutX = results["left"][troutIndex] + cap_x -20
        troutY = results["top"][troutIndex] + cap_y +10
        pyautogui.moveTo(troutX,troutY) #move mouse to random point. if point is clicked directly, client will not recognize
        time.sleep(1)
        pyautogui.click(troutX,troutY) #perform click
        return(True)
    elif "Trovt" in results["text"]:
        troutIndex = results["text"].index("Trout")
        troutX = results["left"][troutIndex] + cap_x -20
        troutY = results["top"][troutIndex] + cap_y +10
        pyautogui.moveTo(troutX,troutY) #move mouse to random point. if point is clicked directly, client will not recognize
        time.sleep(1)
        pyautogui.click(troutX,troutY) #perform click
        return(True)
    else:
        return(False)

    # troutX = results["left"][troutIndex] + cap_x -20
    # troutY = results["top"][troutIndex] + cap_y +10

    # pyautogui.moveTo(troutX,troutY) #move mouse to random point. if point is clicked directly, client will not recognize
    # time.sleep(3)
    # pyautogui.click(troutX,troutY) #perform click
    # # cv2.imshow('img', img)
    # # cv2.waitKey(0)

def dropInv():
    Xmin= 1645
    Xmax = 1800
    Xincrement = round((Xmax-Xmin)/3)
    Ymin = 735
    Ymax = 955
    Yincrement = round((Ymax-Ymin)/5)

    xRange = list(range(Xmin,Xmax+Xincrement,Xincrement))
    yRange = list(range(Ymin,Ymax+Yincrement,Yincrement))

    for x in xRange:
        for y in yRange:
            xRand = x + rand.randint(-10,10)
            yRand = y + rand.randint(-10,10)
            pyautogui.moveTo(xRand,yRand,0.15,pyautogui.easeInQuad)
            pyautogui.click(xRand,yRand)

run = True
while run:
    if keyboard.is_pressed("q"): # constantly check if q is being pressed
        run == False
        break

    trout = seeTroutCatchTrout()
    time.sleep(2)
    if trout == False:
        while trout == False:
            seeTroutCatchTrout()
            time.sleep(30)
            dropInv()
            trout = True
    elif trout == True:
        seeTroutCatchTrout()
        time.sleep(30)
        dropInv()








# for i in range(0, len(results)):
    
#     # We can then extract the bounding box coordinates
#     # of the text region from  the current result
#     x = results[i]
#     y = results["top"][i]
#     w = results["width"][i]
#     h = results["height"][i]
    
#     # We will also extract the OCR text itself along
#     # with the confidence of the text localization
#     text = results["text"][i]
#     conf = int(results["conf"][i])


#  imToString()

# cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 

# run = True

# while run:

#     if keyboard.is_pressed("q"): # constantly check if q is being pressed
#         run == False
#         break


  

# Calling the function
# imToString()

    # else:
    #     time.sleep(3) # give some time to start new loop
    #     position_blue = pyautogui.locateOnWindow('sturgeon.png', "RuneLite", confidence=0.6) #see if a jump or mark region is on screen

    #     # check if jump region is present. if not, mark must be present, player has fallen or finished the course.
    #     if position_blue:
    #         print("FOUND")

    #         clickPositionBlueX = position_blue[0]  #set position as random point inside matched region
    #         clickPositionBlueY = position_blue[1] 
    #         pyautogui.moveTo(clickPositionBlueX,clickPositionBlueY) #move mouse to random point. if point is clicked directly, client will not recognize
    #         time.sleep(3)
    #         pyautogui.click(clickPositionBlueX,clickPositionBlueY) #perform click

    #     else:
    #         print("NOT FOUND")


            # clickPositionBlueX = position_blue[0] + rand.randint(1,position_blue[2]) #set position as random point inside matched region
            # clickPositionBlueY = position_blue[1] + rand.randint(1,position_blue[3]) 
            # pyautogui.moveTo(clickPositionBlueX,clickPositionBlueY) #move mouse to random point. if point is clicked directly, client will not recognize
            # pyautogui.click(clickPositionBlueX,clickPositionBlueY) #perform click


        #     time.sleep(8+rand.randint(0,1)) #wait for a time defined by the time it takes to cross longest obstacle.
        #     #idea could be to add a counter to keep track on which obstacle one is and adjust wait. Reset counter on each teleport 

        # #check if mark is present. if yes, pick it up. Camera setup should be so that only one roof is on screen.
        # elif position_red:
        #     clickPositionRedX = position_red[0] + rand.randint(1,position_red[2]) +20
        #     clickPositionRedY = position_red[1] + rand.randint(1,position_red[3]) +20
        #     pyautogui.moveTo(clickPositionRedX,clickPositionRedY)
        #     pyautogui.click(clickPositionRedX,clickPositionRedY)
        #     time.sleep(4+rand.randint(0,1)) #do not need to wait as long after picking up mark
        # else:
        #     clickPositionTele = (1682+rand.randint(1,20),680+rand.randint(1,18)) # teleport is always on same location. Could also use imgage recognition here...
        #     pyautogui.moveTo(clickPositionTele)
        #     pyautogui.click(clickPositionTele)
        #     time.sleep(2+rand.randint(0,1))