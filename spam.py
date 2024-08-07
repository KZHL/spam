import keyboard
import time

number = int(input("nombre de messages :"))
h = input("text a spam :")
time.sleep(1)


for i in range(number):
    keyboard.write(h)    
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(0.70)
