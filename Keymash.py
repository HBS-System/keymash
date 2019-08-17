from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
from random import choice, randint
import string

COMBINATIONS = [{keyboard.Key.end}]

Keyboard = Controller()

current = set()

def execute():
    table = string.ascii_lowercase
    times = randint(5, 15)
    loops = 0
    while(loops < times):
        char = choice(table)
        Keyboard.press(char)
        Keyboard.release(char)
        loops += 1

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()