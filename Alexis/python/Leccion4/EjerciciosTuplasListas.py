import math # importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
# dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) # definimos la tupla
# crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]

lista = [] # definimos la lista
# filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# ejercicio de matematicas
# para sacar la raiz cuadrada de un numero positivo
numero = int(input("dijite un numero positivo"))
while numero < 0:
    print("error -> deberia ser un numero positivo")
    numero = int(input("dijite un numero positivo"))
print(f"\nsu raiz cuadrada es: {math.sqrt(numero):.2f}")








