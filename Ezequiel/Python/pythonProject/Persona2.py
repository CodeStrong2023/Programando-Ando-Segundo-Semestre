class Persona2:
    def __init__(self, nombre, apelido, edad): #esta encapsulado
        self._nombre = nombre
        self._apelido = apelido
        self._edad = edad

    def nomstrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apelido} {self._edad}')

    @property #decorator
    def nombre(self): #Getter
        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter  # decoratos
    def nombre(self, nombre):  # Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property  # decorator
    def apellido(self):  # Getter
        print('Estamos utilizando el metodo get')
        return self._apellido

    @nombre.setter  # decoratos
    def apellido(self, apellido):  # Setter
        print('Estamos utilizando el metodo set')
        self._apellido = apellido

    @property  # decorator
    def edad(self):  # Getter
        print('Estamos utilizando el metodo get')
        return self._edad

    @nombre.setter  # decoratos
    def edad(self, edad):  # Setter
        print('Estamos utilizando el metodo set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apelido} {self._edad}')

persona1 = Persona2('Ariel', 'Betancud', 41)
print(persona1.nombre) #llamamos al metodo getter

persona1.nombre = 'Juan Pedro' #Llamamos el metodo setter
print(persona1.nombre) # otra vez llamamos al metodo getter

print(persona1.nomstrar_detalles()) # Llamamos el metodo mostrar detalles

#Atributo read-only seria la edad porque no tiene el metodo set
print(persona1.edad)

# Tarea crear tres objetos mas, utilizando los metodos getters and setters
# para modificar, y mostrar los cambios

persona2 = Persona2('María', 'López', 30)
persona2.nombre = 'Laura'
persona2.apellido = 'González'
persona2.edad = 35
print(persona2.nomstrar_detalles())

persona3 = Persona2('Pedro', 'Gómez', 25)
persona3.nombre = 'Roberto'
persona3.apellido = 'Martínez'
persona3.edad = 28
print(persona3.nomstrar_detalles())

persona4 = Persona2('Luis', 'Perez', 35)
persona4.nombre = 'Elena'
persona4.apellido = 'Ramírez'
persona4.edad = 45
print(persona4.nomstrar_detalles())