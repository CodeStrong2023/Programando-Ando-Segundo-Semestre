#Ejercicio 02: Modificar los elementos de una lista
#Llenar una lista con los umeros del 1 al 10, luego modificar los
#eementos de la lista, multiplicandolos por un valor ingresado por el usuario
lista = list(range(1, 11))
print('Lista original')
for i in lista:
    print(i, end='-')
numero = int(input('\nDigite un numero a multiplicar: '))

for indice, i in enumerate(lista):
    lista[indice] *= numero
print(f'Lista final con los elementos multiplicados por  {numero}')
for i in lista:
    print(i, end='-')