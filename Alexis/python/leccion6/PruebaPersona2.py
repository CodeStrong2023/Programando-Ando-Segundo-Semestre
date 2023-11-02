from Persona2 import Persona2
print('creacion de objetos'.center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 36)
    persona5.mostrar_detalles()

    print(__name__)

print('eliminacion de objetos'.center(30, '-'))
del persona5
