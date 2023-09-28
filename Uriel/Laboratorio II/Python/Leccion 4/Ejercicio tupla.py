import math
tupla = (13, 1, 8, 3, 2, 5, 8)
numeros = []
for tup in tupla:
    if tup<5:
        numeros.append(tup)
print(numeros)
for numero in numeros:
    print(numero)

#Ejercicio de matematicas
# PAra sacar la raiz cuadrada de un numro positivo
numero = int(input('Digite un numero positivo: '))
while numero <0:
    print('Error. El numero debe ser positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es : {math.sqrt(numero)}')