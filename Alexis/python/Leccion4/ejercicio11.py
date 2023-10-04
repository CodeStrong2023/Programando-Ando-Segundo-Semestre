# ejercicio 11: agenda telefonica
# hacer un programa que simule una agenda de contactos. crear un
# diccionario donde a clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opciones:
#       1. nuevo contacto
#       2. borrar contacto
#       3. var contactos existentes
#       4. salir
agenda = {}
while True:
    print("\t.:MENU:.")
    print("1. nuevo contacto")
    print("2. bprrar contacto")
    print("3. ver contacto existentes")
    print("4. salir")
    opcion = int(input("digite una opcion de menu: "))
    if opcion == 1:
        nombre = input("digite un nombre de contacto: ")
        telefono = input("digite el numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("contacto agregado exitosamente")
        else:
            print("este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("cual es el nombre de contacto: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("se ha eliminado el contacto requerido")
        else:
            print("este contacto no existe en la agenda")
    elif opcion == 3:
        print("agenda de contacto")
        for clave, valor in agenda.items():
            print(f"nombre: {clave}, telefono: {valor}")
    elif opcion == 4:
        print("gracias por utilizar su agenda de contacto")
        break
    else:
        print("se equivoco de opcion de menu")
    print()







