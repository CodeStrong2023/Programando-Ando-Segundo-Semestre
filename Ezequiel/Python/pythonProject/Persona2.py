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

    # @nombre.setter  # decoratos
    # def edad(self, edad):  # Setter
    #     print('Estamos utilizando el metodo set')
    #     self._edad = edad

persona1 = Persona2('Ariel', 'Betancud', 41)
print(persona1.nombre) #llamamos al metodo getter

persona1.nombre = 'Juan Pedro' #Llamamos el metodo setter
print(persona1.nombre) # otra vez llamamos al metodo getter

print(persona1.nomstrar_detalles()) # Llamamos el metodo mostrar detalles

#Atributo read-only seria la edad porque no tiene el metodo set
print(persona1.edad)
