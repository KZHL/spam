import keyboard
import time

number = int(input("nombre de messages :"))
h = input("text a spam :")
# Attendre quelques secondes pour donner le temps de se concentrer sur la fenêtre où la frappe sera effectuée
time.sleep(1)

# Boucler à travers chaque mot et simuler la frappe

for i in range(number):
    keyboard.write(h)    
    keyboard.press('enter')
    keyboard.release('enter')
    # Ajouter une pause entre chaque mot (ajustez si nécessaire)
    time.sleep(0.70)
