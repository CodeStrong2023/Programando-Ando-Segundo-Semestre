class Persona2:
    def __init__(self, nombre, apellido, edad):  # esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # metodo getter
        print('estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # setter
        print('estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('estamos utilizando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('estamos utilizando el metodo set')
        self._apellido = apellido

    @property
    def edad(self):
        print('estamos utilizando el metodo get')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('estamos utilizando el metodo set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2:{self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('ariel', 'betancut', 41)
    print(persona1.nombre)  # llamamos al metodo getter
    persona1.nombre = 'juan pedro'  # llamamos al metodo setter
    print(persona1.nombre)  # otra vez con el metodo getter
    print(persona1.mostrar_detalles())  # llamamos al metodo mostrar_detalle
    # atributo read-only(solo lectura) seria la edad porque no tiene el metodo set
    print(persona1.edad)
    # tarea crear tres objetos mas, utilizando los metodos getter and setter
    # para modificar y mostrar los cambios con el metodo mostrar_detalle

    # objeto numero 1 de la tarea
    persona2 = Persona2('flor', 'romero', 22)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'florencia'
    persona2.apellido = 'romery'
    persona2.edad = 22
    print(persona2.mostrar_detalles())

    # objeto numero 2 de la tarea
    persona3 = Persona2('caro', 'felisa', 21)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona3.nombre = 'carolina'
    persona3.apellido = 'felix'
    persona3.edad = 31
    print(persona3.mostrar_detalles())

    # objeto numero 3 de la tarea
    persona4 = Persona2('naty', 'lucer', 35)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona4.nombre = 'natalia'
    persona4.apellido = 'lucero'
    persona4.edad = 33
    print(persona4.mostrar_detalles())

    print(__name__)
