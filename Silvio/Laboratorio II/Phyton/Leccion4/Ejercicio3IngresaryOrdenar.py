# Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0,
# nuestro programa dedjaría de insertar. Mostrar elementos ordenados

lista = []
numero = int(input('Ingrese numeros a la lista, finalice con un "0": '))

while numero != 0:
    numero = int(input('Ingrese el siguiente elemento: '))
    lista.append(numero)

lista.sort()

print(lista)

