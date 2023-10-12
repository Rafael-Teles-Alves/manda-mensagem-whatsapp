
import pywhatkit 
import keyboard
import time
from datetime import *


contatos = ['+551199999999']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'https://youtu.be/vmtqNpLVGZI?si=sjpapJD-YA7v0Y5q', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(20)
    keyboard.press_and_release('ctrl+w')
