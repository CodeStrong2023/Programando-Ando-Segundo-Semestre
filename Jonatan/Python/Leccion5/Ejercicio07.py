#Ejercicio 7 : juego adivina el numero
#realizar un juego para adivinar un numero. Para ello se debe
#generarar un numero aleatorio entre 1-100 y luego ir pidiendo
#numeros indicando "es mayor" o "es menor" segun sea mayor o menor
#con respecto a N. El proceso Termina cuando el usuario acierta
#y alli debe mostrar el numero de intentos.
import random
print('\tJUEGO ADIVINA EL NUMERO!')
aleatorio = random.randint(0,100)#primero importar random, y usar randint para poner un aleatorio de 0 a 100
contador = 0
while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print('\t NO ES EL NUMERO, DIGITE UN NUMERO MENOR')
    elif numero < aleatorio:
        print('\t NO ES EL NUMERO, DIGITE UN NUMERO MAYOR')
    else:
        print(f'FELICIDADES, ACABAS DE ADIVINAR EL NUMERO!!!  EL NUMERO ES: {aleatorio}')
        break#ciclo break para romper el ciclo
print(f'Lograste adivinar el numero en: {contador} Intentos.')