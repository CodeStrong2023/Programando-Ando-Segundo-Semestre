class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama metodo init Dunder
        self.nombre = nombre  # si utilizamos __nombre sería un encapsulamiento completo, solo accedible a travez de metodos, no se puede modificar
        self.apellido = apellido
        self._dni = dni  # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # this en otros lenguajes
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Silvio', 'Stefanucci', 234653456, 31)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, Su edad es: {persona1.edad}')
persona2 = Persona('Juan', 'Cito', 23563466, 48)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, Su edad es: {persona2.edad}')

persona1.nombre = 'Juanacio'
persona1.apellido = 'Viale'
persona1.edad = 11

print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, Su edad es: {persona1.edad}')

# Los atributos son las caracteristicas
# Los metodos son el comportamiento
persona1.mostrar_detalle()  # La referencia se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Si utilizamos una clase en vez de un objeto, debemos pasarle una referencia
persona1.telefono = '23784532'
print(persona1.telefono)  # Hemos creado un atributo de un objeto
print(f'Este es el telefono: {persona1.nombre} {persona1.telefono}')

# print(persona2.telefono) el objeto persona2 no tiene este atributo
persona3 = Persona('Hernan', 'Tosi', 34545677, 35, 'Telefono', '1278936', 'Calle Lanus', 234, 'Manzana', 77, Altura=1.45, Peso=78, Pelo='Castaño')
persona3.mostrar_detalle()

persona4 = Persona('Sol', 'Luna', 45624512, 30, 'Telefono', '34568956', 'Calle Cullen', 2768, 'Manzana', 10, Altura=1.70, Peso=60, Pelo='Rubio')
persona4.mostrar_detalle()
# persona1._dni # esta no se debe utilizar (esta encapsulado), esto dice que lo desconocemos Python
