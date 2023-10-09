#Ejercicio 2 : Modificar los elementos de una lista
#llenar una lista con los numeros del 1 al 10, luego modificar los
#elementos de una lista multiplicandolos por un valor ingresado por el usuario


lista = list(range(1,11))
print('Lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))

#multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):#funcion para modificar los indices de la lista
    lista[indice] *= valor#el iterador solo recorre los indices, en esta linea se multiplica
print(f'Lista final con los elementos multiplicador por {valor}')
for i in lista:
    print(i, end='-')

