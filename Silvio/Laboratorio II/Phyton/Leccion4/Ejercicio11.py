agenda = {}
while True:
        print('\t.:MENU:.')
        print('1. Nuevo contacto')
        print('2. Borrar contacto')
        print('3. Ver contactos')
        print('4. Salir')
        opcion = int(input('Seleccione una opcion: '))
        if opcion == 1:
            nombre = input('Ingrese el nombre del contacto: ')
            telefono = input('Ingrese el numero de telefono: ')
            if nombre not in agenda:
                agenda[nombre] = telefono
                print('Contacto agregado exitosamente')
            else:
                print('El Contacto ya existe')
        elif opcion == 2:
            nombre = input('Cual es el nombre del contacto:')
            if nombre in agenda:
                del(agenda[nombre])
                print('Se ha elimindo el contacto seleccionado')
            else:
                print('Contacto Inexistente')
        elif opcion == 3:
            print('Agenda de contactos')
            for clave, valor in agenda.items():
                print(f'Nombre: {clave}, Telefono: {valor}')
        elif opcion == 4:
            print('Aplicacion Finalizada')
            break
        else:
            print('Se equivoco de opcion de menu')
        print()