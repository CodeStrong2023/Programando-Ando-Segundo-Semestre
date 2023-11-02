#EJercicio 08: Menu interactico -Cajero automatico
#Hacer un programa que simule un cajero automatico
#con un saldo de $1000 y tendra las siguientes opciones
#1. Ingresar dinero a la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dinero diponible
#4. Salir


def ingresar(saldo):
    ingreso = int(input('Digite el monto a ingresar\n'))
    saldo = saldo + ingreso
    return saldo
def retirar(saldo):
    egreso = int(input('Digite el monto a retirar\n'))
    saldo = saldo - egreso
    if saldo < 0:
        print('Error. Saldo no disponible.\n')
        saldo = saldo + egreso
    return saldo
def mostrar(saldo):
    print(f'Saldo disponible: {saldo}\n')

saldo = 1000
while True:
    print("\t\tCajero Automatico")
    print("\t\t\t\tMenú")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero diponible")
    print("4. Salir")
    opcion = int(input("Digite el numero correspondiente a la opcion deseada\n"))
    match(opcion):
        case 1:
            saldo = ingresar(saldo)
        case 2:
            saldo = retirar(saldo)
        case 3:
            mostrar(saldo)
        case 4:
            break
        case default:
            print("Error. Digite una opcion valida\n\n")