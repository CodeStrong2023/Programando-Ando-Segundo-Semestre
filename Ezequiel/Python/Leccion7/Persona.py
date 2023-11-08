class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self.edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self.sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}'

empleado1 = Empleado("Ezequiel", 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)


#Tarea: encapsular los atributos y agregar los metodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado("Juan", 35, 78900)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'Jose'
empleado2.edad = 33
empleado2.sueldo = 2222000

print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)