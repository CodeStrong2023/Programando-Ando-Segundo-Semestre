#ejercicio 11: Agenda Telefonica
#hacer un programa que simule una agenda de contactos. Crear uin diccionario
#donde la clase sea el nombre del usuario y el calor
#sea el telefono, para el programa tendra el siguiente menu de opciones


#       1. Nuevo Contacto
#       2. Borrar Contacto
#       3. Ver Contactos Existentes
#       4. Salir

agenda = {}#iniciamos el diccionario vacio

while True:#ciclo while para hacer el menu
    print('\t :MENU:')
    print('1. Nuevo Contacto')
    print('2. Borrar Contacto')
    print('3. Ver Contactos Existentes')
    print('4. Salir')
    print()
    opcion = int(input('Digite una opcion en el menu.'))#leemos la opcion del usuario

    if opcion == 1:#opcion 1 para agregar un contacto
        nombre = input('Digite el nombre del Contacto: ')
        telefono = input('Digite el numero de Telefono: ')
        if nombre not in agenda :#si la variable Nombre no esta en el diccionario agenda
            agenda [nombre] = telefono#en el diccionario "Agenda" guardamos la clase llamada "Nombre" y su valor "Telefono"
            print('Contacto agregado exitosamente!.')
        else:
            print('Error! Ese contacto ya Existe')#si el contacto YA existe se lo hjacemos saber
    elif opcion == 2:#para borrar un contacto
        nombre = input('Cual es el nombre del Contacto: ')
        if nombre in agenda:#si el nombre esta en el contacto
            del (agenda[nombre])#borramos de la agenda la clave especifica "Nombre" y su valor
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda.')#si no existe
    elif opcion == 3:
        print('Agenda de contactos: ')#mostramos la agenda con un ciclo for para recorrer el diccionario
        for clave, valor in agenda.items():#con la variable clase,valor in"en" la agenda ponemos .items() vacio para mostrar los items que lleva la agenda
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar la agenda de Contactos.')
        break
    else:
        print('ERROR! Numero ingresado INCORRECTO!')#si el usuario se equivoca de OPC
