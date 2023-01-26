import time

import keyboard
import pyautogui
import pytesseract as tess
from PIL import Image
from pynput.mouse import Listener

A = "Larvesta"
C = "Marowak"
B = "Wild"
AreaX = -1
AreaY = -1
Area2X = -1
Area2Y = -1
tess.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def coordenadas():
    def on_move(x, y):
        pass

    def on_click(x, y, button, pressed):
        global AreaX 
        global AreaY 
        global Area2X
        global Area2Y 
        if pressed:
            if AreaX == -1:
                AreaX = x
                AreaY = y
                print("primeiro preenchido")
            else:
                Area2X = x
                Area2Y = y
                print("segundo preenchido")
                listener.stop()

    def on_scroll(x, y, dx, dy):
        pass

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

def andar():
    time.sleep(1)
    while True:
        keyboard.press('d')
        keyboard.press('a')
        time.sleep(0.7)
        # para mexer sideways d/a para up/down trocar por w/s   andar em blocos de 6 o ideal é 0.7
        keyboard.release('a')
        time.sleep(0.7)
        printString = tess.image_to_string(pyautogui.screenshot(region=(AreaX,AreaY,Area2X - AreaX + 10,Area2Y - AreaY + 5)))
        print(printString)
        if B in printString:
            keyboard.release('d')
            break
    apanhar() 
def apanhar():
    apanhar = True
    falsewipe = True
    printString = tess.image_to_string(pyautogui.screenshot(region=(AreaX,AreaY,Area2X - AreaX + 10,Area2Y - AreaY + 5)))

    if A not in printString and C not in printString:
        fugir()
        apanhar = False
        
    while apanhar:
        print("Vais ser meu")
        if falsewipe:
            falsewipe = False
            falseswipe(1)
        
        
        pokebola()
        
        
        printString = tess.image_to_string(pyautogui.screenshot(region=(AreaX,AreaY,Area2X - AreaX + 10,Area2Y - AreaY + 5)))
        if A not in printString and C not in printString:
            print("ES MEU QUE TE FODES")
            apanhar = False
    andar()


def falseswipe(numeroDeFalseWIPES):
    i = 0
    while i < numeroDeFalseWIPES:
        time.sleep(3.5)
        keyboard.press('1')
        time.sleep(0.2)
        keyboard.release('1')
        time.sleep(0.2)
        keyboard.press('4')
        time.sleep(0.2)
        keyboard.release('4')
        time.sleep(5)
        i+=1

def pokebola():
    time.sleep(1.5)
    keyboard.press('3')
    time.sleep(0.2)
    keyboard.release('3')
    time.sleep(0.2)
    keyboard.press('1')
    time.sleep(0.2)
    keyboard.release('1')
    time.sleep(15)

def fugir():
    time.sleep(4)
    keyboard.press('4')
    time.sleep(0.2)
    keyboard.release('4')
    time.sleep(0.5)
                       
coordenadas()
andar()
