# Ejercico 7: Juego adivina el numero
# Realiza un juego para adivinar un numero. Para ellos se debe
# Generar un numero aleatorioo entre 1 - 100, y luego ir pidiendo
# numero indicando "es mayor" o "es menor" segun sea mayor o menos
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos

import random

aleatorio = random.randint(1, 100)
contador = 0
print("\t.:Juego Adivina el numero:.")
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digite uno menor")
    elif numero < aleatorio:
        print("\tNo es el numero, digite uno mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el numero {aleatorio}")
        break

print(f"\nNumero d eintentos: {contador}")