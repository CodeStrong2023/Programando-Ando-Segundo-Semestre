# ejercicio 8: menu interactivo - cajero automatico
# hacer un programa que simule cajero automatico con un saldo
# inicial de $1000 y tendran el siguiente menu de opciones:
#                               1. ingresar dinero en la cuenta
#                               2. retirar dinero de la cuenta
#                               3. mostrar dinero de la cuenta
#                               4. salir
saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. ingresar dinero en la cuenta")
    print("2. retirar dinero de la cuenta")
    print("3. mostrar dinero disponible")
    print("4. salir")
    opcion = int(input("digite una opcion de menu: "))
    print()
    if opcion == 1:
        extra = float(input("cuanto dinero desea ingresar -> "))
        saldo += extra
        print(f"dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("cuanto dinero desea retirar -> "))
        if retirar > saldo:
            print("no tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print(f"gracias por utilizar su cajero automatico, hasta pronto")
        break
    else:
        print("error, se equivoco de opcion de menu")
        print()







