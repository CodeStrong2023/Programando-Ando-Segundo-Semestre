class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad  # Encapsulamiento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
class Empleado(Persona):#Empleado es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

empleado1 = Empleado('Antonio', 43, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
#Tarea: Encapsular los atributos y agregar los metodos getters and setters
#Crear otro objeto, pasar los datos para nombre ,edad y sueldo
#Mostrar estos datos, luiego modificar y mostrar nuevamente

empleado2 = Empleado('Liliana', 39, 70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'Natalia'
empleado2.edad = 36
empleado2.sueldo = 80000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

#11.5
