from PIL import Image
import pytesseract
import pyautogui
import re
from pygame import mixer
from time import sleep
import pyperclip
import keyboard
import requests
from translate import Translator
 
TOKEN = "6085093522:AAFXD1VJYDDs1Cq3x8LAwFIOsmMgTssLqV4"
chat_id = "635258639"
translator= Translator(to_lang="Russian")

def translator_translate(word):
    result = translator.translate(word, dest = 'ru')
    return result.text 
def write(name):
    pyperclip.copy(name) #Копирует в буфер обмена информацию
    pyperclip.paste()

#Вызываем функцию записи в буфер обмена

def initPoints():
    points = []
    f = open('members.csv')
    points = f.read().splitlines()
    f.close()
    print(points)
    for p in points:
        

        write(p)

        pyautogui.hotkey('ctrl','v')
        
        
       
while True:
    if keyboard.is_pressed("z"):
        pyautogui.hotkey('ctrl','c')
    if keyboard.is_pressed("c"):
        x = pyperclip.paste()
        a = x
        translation = translator.translate(a) 
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={translation}"
        print(type(a))
        print(requests.get(url).json())
    if keyboard.is_pressed("x"):
        x = pyperclip.paste()
        a = x 
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={a}"
        print(type(a))
        print(requests.get(url).json())
        




