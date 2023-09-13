# Ejerciio 3: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en un lista, cuando el usuario introduzca
# un numero 0, nuestro programa dejari a de insertar.
# por ultimo, mostrar los numeros ordenados de menor a mayor

lista = []
salir = False

while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort()
print(f'\nLista ordenada: \n{lista}')