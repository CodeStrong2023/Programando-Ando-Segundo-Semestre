# Simular un cajero aumtomatico, salgo inicioal $1000 y con las siguientes opciones
# 1 - Ingresar dinero a la cuenta
# 2 - Retirar dinero
# 3 - Mostrar dinero
# 4 - Salir

saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion del menu: "))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero quiere ingresar: "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retiro = float(input("Cuanto dinero quiere retirar: "))
        if reito > saldo:
            print(f"No tiene esa cantidad de dinero, su saldo actual es de ${saldo}")
        else:
            saldo -= retiro
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar nuestro servicio")
        break
    else:
        print("Esa opcion no existe")
        print("Seleccione una de las opciones disponibles")
