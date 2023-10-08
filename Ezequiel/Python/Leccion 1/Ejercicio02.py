#Ejercicio 2: Modificar los elementeos de una lista
# llenar una lista con los numeros de 1 al 10, luego modificar los elemetnos
# de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1,11))
print('Lista Original')

for i in lista:
    print(i,end='-')

valor = int(input('\nDigite un valor a multiplicar: '))

# Multiplicamos todos los elementos de la lista

for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')

for i in lista:
    print(i,end='-')