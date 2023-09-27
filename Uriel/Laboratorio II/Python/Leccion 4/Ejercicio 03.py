#Ejercicio 03: Insetar los elementos y ordenarlos
#Pedir numeros y meterlos en la lista, cuando el usuario
#introduzca el numero 0, nuestro programa dejaria de insertar
#Por ultimo mostrar los numeros de menor a mayor
lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero'))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()
print(f'Lista ordenada\n{lista}')