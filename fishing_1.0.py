import keyboard
import pyautogui
import time
import random as rand
import pytesseract
from pytesseract import Output
import cv2
import numpy as nm
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
  
def seeTrout():
    cap_x = 900
    cap_y = 100
    cap_x2 = 1250
    cap_y2 = 1100

    capture = ImageGrab.grab(bbox =(cap_x,cap_y,cap_x2,cap_y2))
    img = nm.array(capture.convert("RGB"))
    results = pytesseract.image_to_data(img, output_type=Output.DICT)
    # # cv2.imshow('img', img)
    # # cv2.waitKey(0)
    n_boxes = len(results['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (results['left'][i], results['top'][i], results['width'][i], results['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    print(results["text"])
    
    if "Pike" in results["text"]:
        troutIndex = results["text"].index("Pike")
        troutX = results["left"][troutIndex] + cap_x -rand.randint(-20,-10)
        troutY = results["top"][troutIndex] + cap_y +rand.randint(-5,5)
        return True, troutX, troutY
    else:
        return False, 0, 0

def clickTrout(troutX,troutY):
        pyautogui.moveTo(troutX,troutY,0.5,pyautogui.easeInQuad) #move mouse to random point. if point is clicked directly, client will not recognize
        time.sleep(1)
        pyautogui.click(troutX,troutY) #perform click

def dropInv():
    Xmin= 1645
    Xmax = 1800
    Xincrement = round((Xmax-Xmin)/3)
    Ymin = 735
    # Ymax = 955
    Ymax = 900 #only drop to 4 row (each row is 55px)
    Yincrement = round((Ymax-Ymin)/5) 

    xRange = list(range(Xmin,Xmax+Xincrement,Xincrement))
    yRange = list(range(Ymin,Ymax+Yincrement,Yincrement))

    for x in xRange:
        for y in yRange:
            xRand = x + rand.randint(-10,10)
            yRand = y + rand.randint(-10,10)
            pyautogui.moveTo(xRand,yRand,0.1,pyautogui.easeInQuad)
            pyautogui.click(xRand,yRand)

run = True
while run:
    if keyboard.is_pressed("q"): # constantly check if q is being pressed
        run == False
        break

    trout = seeTrout()
    while trout[0] == False:
        trout = seeTrout()
        time.sleep(0.5)
    clickTrout(trout[1],trout[2])
    time.sleep(50)
    dropInv()