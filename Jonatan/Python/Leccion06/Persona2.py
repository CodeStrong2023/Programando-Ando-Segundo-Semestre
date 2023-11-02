class Persona2:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre}{self._apellido}{self._edad}')

    @property
    def nombre(self):#metodo getter
        print('Estamos usando el metodo get')
        return self._nombre


    @nombre.setter
    def nombre(self,nombre):#metodo setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Apellido')
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        print('apellido')
        self._apellido = apellido

    @property
    def edad(self):
         print('edad')
         return self._edad

    @edad.setter
    def edad(self,edad):
       print("Edad")
       self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido}{self._edad}')

if __name__ == '__main__':
    persona1 =Persona2('Ariel','Bentancud',41)
    print(persona1._nombre)#llamamos al metodo getter
    print(persona1._apellido)
    print(persona1._edad)
    persona1.nombre = 'Manolito'#llamamos al metodo setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())
    #atributo read-only (solo lectura) seria la edad porquie no tiene el motodo set
    print(persona1.edad)

    #tarea crear tres objetos mas utilizando los metodos getter and setter
    #para modificar, y mostrar los cambios con el metodo mostrar detalles

    persona2 = Persona2('Antonio','Ramirez', 22)
    persona2.nombre = 'Manuel'
    persona2.apellido = 'Allende'
    persona2.edad = 22
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Analia','Perez', 16)
    persona3.nombre = 'MArin'
    persona3.apellido = 'Arebalo'
    persona3.edad = 28
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    persona4 = Persona2('Sebastian','Camilo', 50)
    persona4.nombre = 'Juan '
    persona4.apellido = 'Guerrero '
    persona4.edad = 28
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)





