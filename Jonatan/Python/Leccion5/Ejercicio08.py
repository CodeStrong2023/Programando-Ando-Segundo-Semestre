#Ejercicio 8: Menu interactivo - Cajero Auitomatico
#hacer un programa que simule un cajero automatico con un salgo
#inicial de 1000 y tendra el siguiente menu de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000 #saldo inicial en 1000

while True:#ciclo while mientras que sea verdadero el menu se cumplen los if si no es por que el usuario ingreso mal el numero
    print('\t :MENU:')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    print()

    opcion = int(input('Digite una Opcion de menu: '))
    print()
    if opcion == 1:#ciclo if
        extra = float(input('Digite cuando dinero desea ingresar: '))
        saldo += extra
        print(f'Dinero disponible en la cuenta: ${saldo}')
    elif opcion == 2:
        retiro = float(input('Digite cuanto dinero desea Retirar: '))
        saldo -= retiro
        print(f'Dinero disponible en la cuenta: ${saldo}')
    elif opcion == 3:
        print(f'Dinero disponible en la cuenta: ${saldo}')
    elif opcion == 4:
        print('Muchas Gracias por utilizar este Cajero. Hasta pronto.')
        break#con el break terminamos si el usuario elige opc 4
    else:
        print('Digito un numero Erroneo, intente nuevamente.')


