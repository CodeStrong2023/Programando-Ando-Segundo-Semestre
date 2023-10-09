import math #importamos la clase math para hacer el uso de funcion sqrt (rtaiz cuadrada)
#dada la siguiente TUPLA
tupla = (13, 1, 8, 3, 2, 5, 8)#$definimos la tupla
#crear una Lista que solo incluyan los numeros menores a 5
#e imprima por consola [1, 3 , 2]

lista = []#definimos la lsita
#filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio de Matematicas
#Para sacar la Raiz cuadrada de un numero positivo
numero = int(input('Digite un numero Positivo: '))#solciitamos al usuario un numero positivo

while numero < 0:#ciclo while para primero comprobar el dato ingresado
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo'))
print(f'\n Su raiz cuadrada es: {math.sqrt(numero):.2f}')#funcion math.sqrt para sacar la raiz