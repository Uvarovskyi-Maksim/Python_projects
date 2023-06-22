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
 
TOKEN = "TOKEN"
chat_id = "chat_id"
translator= Translator(to_lang="Russian")

def translator_translate(word):
    result = translator.translate(word, dest = 'ru')
    return result.text 
def write(name):
    pyperclip.copy(name) #Копирует в буфер обмена информацию
    pyperclip.paste()
           
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
        




