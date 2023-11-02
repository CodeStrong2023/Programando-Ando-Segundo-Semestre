class Persona2:
    def __init__(self, nombre, apellido, edad): # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo getter
        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos utilizando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el metodo set')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos utilizando el metodo get')
        return self._edad

    @edad.setter  # Quitando el setter, el elemento solo seria read-only
    def edad(self, edad):
        print('Estamos utilizando el metodo set')
        self._edad = edad

    def __del__(self):  # Metodo Destructor
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':  # Comprobacion del modulo principal en ejecucion
    # Crear tres objetos más
    persona2 = Persona2('Ana', 'Gonzalez', 25)
    persona3 = Persona2('Carlos', 'Perez', 30)
    persona4 = Persona2('Maria', 'Rodriguez', 35)

    # Utilizar los métodos getter para mostrar los detalles iniciales
    print("Detalles iniciales:")
    persona2.mostrar_detalles()
    persona3.mostrar_detalles()
    persona4.mostrar_detalles()

    # Utilizar los métodos setter para modificar los detalles
    persona2.nombre = 'Andrea'
    persona3.apellido = 'Lopez'
    persona4.edad = 40

    # Utilizar los métodos getter para mostrar los cambios
    print("Detalles después de las modificaciones:")
    persona2.mostrar_detalles()
    persona3.mostrar_detalles()
    persona4.mostrar_detalles()

    print(__name__)
