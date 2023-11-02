#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un
#diccionario donde la clave sea el nombre del usuario y el valor sea
#el numero de tlefono. El programa tendra l siguiente menu de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

def nuevoContacto(agenda):
    nombre = input('Digite el nombre:\n')
    telefono = input('Digite el numero de telefono:\n')
    if nombre not in agenda:
        agenda[nombre] = telefono
        print('Contacto creado exitosamente:\n')
    else:
        print('Este contacto existe actualmente\n')
    return agenda

def borrarContacto(agenda):
    nombre = input('Digite el  ombre del contacto')
    if nombre in agenda:
        del(agenda[nombre])
        print('Contacto borrado exitosamente\n')
    return agenda

def verContactos(agenda):
    print('\nAgenda de contactos:')
    for clave, valor in agenda.items():
        print(f'Nombre: {clave}, Telefono: {valor}')


agenda = {}
while True:
    print('\tMenu:')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opcion del menu\n\n'))
    match(opcion):
        case 1:
            agenda = nuevoContacto(agenda)
        case 2:
            agenda = borrarContacto(agenda)
        case 3:
            verContactos(agenda)
        case 4:
            print('Gracias')
            break
        case default:
            print('Error. El numero debe ser una opcion valida del menu')