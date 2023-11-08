class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son: {self._nombre} {self._apellido} {self._edad}')

    @property #Decorador
    def nombre(self): #Metodo Getter
        return self._nombre
    @nombre.setter
    def nombre(self, nombre): #Metodo setter
        self._nombre = nombre
    @property
    def apellido(self): #Metodo getter
        return self._apellido
    @apellido.setter
    def apellido(self, apellido): #Metodo setter
        self._apellido = apellido
    @property
    def edad(self): #Metodo getter
        return self._edad
    @edad.setter
    def edad(self, edad): #Metodo setter
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self.nombre} {self.apellido} {self.edad}')

if __name__ == '__main__':
    persona1 = Persona2('Uriel', 'Pardo', 27)
    print(persona1.nombre)  # Llamamos al metodo Getter
    persona1.nombre = 'Gaston'
    print(persona1.apellido)
    persona1.apellido = 'Gomez'
    print(persona1.edad)
    # Atributo read-only porque no tiene setter
    persona1.edad = 30
    persona1.mostrar_detalle()

    # Tarea crear tres objetos mas utilizando los metodos getters y setter
    # para modificar, y mostrar los cambios
    persona2 = Persona2('Nerea', 'Pardo', 29)
    print(f'Persona2 Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')
    persona3 = Persona2('Abel', 'Blanco', 30)
    print(f'Persona3 Nombre: {persona3.nombre}, Apellido: {persona3.apellido}, Edad: {persona3.edad}')
    persona4 = Persona2('Maciel', 'Castro', 22)
    print(f'Persona4 Nombre: {persona4.nombre}, Apellido: {persona4.apellido}, Edad: {persona4.edad}')
    persona2.nombre = 'Aisha'
    persona2.apellido = 'Gimenez'
    persona2.edad = 32
    persona2.mostrar_detalle()
    persona3.nombre = "Eduardo"
    persona3.apellido = 'Perez'
    persona3.edad = 41
    persona3.mostrar_detalle()
    persona4.nombre = 'Gonzalo'
    persona4.apellido = 'Vazquez'
    persona4.edad = 25
    persona4.mostrar_detalle()
