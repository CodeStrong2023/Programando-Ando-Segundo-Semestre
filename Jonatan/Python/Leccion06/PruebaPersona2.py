from Persona2 import Persona2
print('Creacion de objetos'.center(50, '-'))
if __name__ =='__main__':
    persona5 = Persona2('Andres', 'Gomez', 40)
    persona5.mostrar_detalles()
    print(__name__)#sirve para ver de donde se esta ejecutando


print('Eliminacion de objetos'.center(50, '-'))
del persona5