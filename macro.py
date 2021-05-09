# Created by kor_a at 09/05/2021
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


def toggle(pin):
    if pin.value == 1:
        pin.value = 0
    else:
        pin.value = 1


while True:
    if button.value:
        toggle(led)
        time.sleep(0.5)

    if led.value == 1:
        keyboard.press(Keycode.Z)
        time.sleep(0.01)
        keyboard.release(Keycode.Z)
        time.sleep(0.01)
        keyboard.press(Keycode.Z)
        time.sleep(0.01)
        keyboard.release(Keycode.TWO)
        time.sleep(0.01)
        keyboard.press(Keycode.TWO)
        time.sleep(0.01)
        keyboard.release(Keycode.TWO)
        time.sleep(0.01)
        keyboard.press(Keycode.TWO)
        time.sleep(0.01)
        keyboard.release(Keycode.TWO)
        time.sleep(0.1)
