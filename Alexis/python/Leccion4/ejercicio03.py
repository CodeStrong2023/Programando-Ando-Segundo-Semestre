# ejercicio 3: insertar elementos y ordenarlos
# pedir numeros y meterlos en una lista, cuando el usuario
# introduzca un numero 0, nuestro programa dejaria de insertar
# por ultimo, mostrar los numeros ordenados de menor a mayor
lista = []
salir = False
while not salir:
    numero = int(input("dijite un numero"))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # la lista esta ordenada con esta funcion
print(f"\nlista ordenada: \n{lista}")





