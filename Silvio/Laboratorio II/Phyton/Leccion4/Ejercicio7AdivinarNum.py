# Juego de avivinar un numero aleatorio entre 1 y 100. pistas "es mayor" o "es menor"
# al acertar, mostrar numero de intentos

import random

adivinar = random.randint(1, 100)

intentos = 0

num = int(input('Del 1 al 100... ¿Que numero estoy pensando?: '))

while num != adivinar:
    if num < adivinar:
        print('Es mas grande...')
    elif num > adivinar:
        print('Es mas chico...')
    intentos += 1
    num = int(input('¿Que numero estoy pensando?: '))

print(f"\n ¡Muy Bien! ¡Haz adivinado el numero en {intentos} intentos!")

