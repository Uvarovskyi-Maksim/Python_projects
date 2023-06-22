from PIL import Image
import pytesseract
import pyautogui
import requests
import re
from pygame import mixer
from time import sleep
TOKEN = "6085093522:AAFXD1VJYDDs1Cq3x8LAwFIOsmMgTssLqV4"
chat_id = "635258639"
message = "Новый ЛОХ на связи"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
sleep(3)
def check(x):
    s1 = "".join(c for c in x if  c.isdecimal())
    s1 = int(s1)
    return s1
def circ():
    screenshot = pyautogui.screenshot(region=(537, 192, 39, 40))
    screenshot.save('screenshot.png')
    image = Image.open('screenshot.png')
    text = pytesseract.image_to_string(image)
    a = check(text)
    k = a
    while True:
        sleep(4)
        pyautogui.moveTo(106, 60)
        pyautogui.click(button='left')
        pyautogui.PAUSE = 3
        sleep(4)
        screenshot = pyautogui.screenshot(region=(537, 192, 39, 40))
        screenshot.save('screenshot.png')
        image = Image.open('screenshot.png')
        text = pytesseract.image_to_string(image)
        new = check(text)
        
        print(new)
        
        if(new > k):
            mixer.init()
            print(requests.get(url).json()) 
            mixer.music.load("bebr.mp3")
            mixer.music.play()
            input()
            k==new
            exit()
sleep(3)
circ()










