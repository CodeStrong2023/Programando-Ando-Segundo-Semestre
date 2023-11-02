# ejercicio 7: juego adivina el numero
# realizar un juego para adivinar un numero. para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. el proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos
import random
print("\t.:juego: adivina el numero:.")
aleatorio = random.randint(0, 100) # tom de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tno es el numero, digite un numero menor")
    elif numero < aleatorio:
        print("\tno es el numero, digite un numero mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el numero {aleatorio}")
        break # rompe el ciclo y el bucle
print(f"\nnumero de intentos: {contador}")



