# Modificar los elementos de una lista multiplicandolos por un valor ingresado por el usuario

lista = []

for numero in range(1, 11):
    lista.append(numero)

print(f'Lista Original: {lista}')

multi = int(input('Ingrese el multiplicador: '))

for i in range(len(lista)):
    lista[i] = lista[i]*multi

print(f'Lista Multiplicada: {lista}')
