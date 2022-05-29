## This script will simulate a keypress and prevent Windows from locking
import pyautogui
import time

def no_lock_default():
    try:
        print ('Press CTRL+C to stop.')
        while True:
            pyautogui.press('volumedown')
            time.sleep(1)
            pyautogui.press('volumeup')
            time.sleep(5)
    except Exception as ex:
        print ('no_lock | Error: ', ex)


def no_lock(button):
    try:
        print ('Press CTRL+C to stop.')
        while True:
            pyautogui.press(button)     # Key pressed "capslock"
            time.sleep(2)

            pyautogui.press('volumedown')
            time.sleep(1)
            pyautogui.press('volumeup')
            time.sleep(5)
    except Exception as ex:
        print ('no_lock | Error: ', ex)

def main():
    try:
        print ('\nPrevent Windows screenlock')
        kb_button = str(input('Enter keyboard button: '))
        
        print ('\nRunning')
        no_lock(kb_button)

    except KeyboardInterrupt:
        print('\nStopped')

    except Exception as ex:
        print ('main | Error: ', ex)

if __name__ == "__main__":
    # main()
    no_lock_default()