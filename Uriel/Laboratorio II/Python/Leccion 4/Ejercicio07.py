#Ejercicio 07: Juego adivina el numero
#Realizar un juego para adivinar un numero. Para ello se debe
#generar un numero aleatorio entre 1-100, luego ir pidiendo
#numeros indicando "Es mayor" o "Es menor" segun corresponda.
#El proceso termina cuando acierta, debe mostrar el numero de intentos
from random import randint
numero = randint(1, 100)
intentos = 0
while True:
    valor = int(input('Digite un numero entre 1 y 100\n'))
    if valor < numero:
        print('El numero ingresado es MENOR')
        intentos += 1
    elif valor > numero:
        print('El numero ingresado es MAYOR ')
        intentos += 1
    else:
        intentos += 1
        print(f'Felicidades. El numero es {numero}\nLo encontraste en {intentos} intentos')
        break
