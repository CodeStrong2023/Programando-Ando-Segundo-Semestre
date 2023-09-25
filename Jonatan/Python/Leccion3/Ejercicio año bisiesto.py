#ejercicio del año bisiesto
while True: #ciclo while para repetir el programa
    año = int(input("Ingrese un año (0 para salir): "))#pedimos al usuario que ingrese un año o 0

    if año == 0:#si la OPC del usuario es 0 el programa se rompe con "Break"
        print('Hasta pronto')
        break

    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):#si no se rompe, comprobamos que el año ingresado comprobamos la exprecion
        print(f'{año} es un año bisiesto.')#si la comprovacion es positiva
    else:
        print(f'{año} no es un año bisiesto.')#si la comprovacion es negativa