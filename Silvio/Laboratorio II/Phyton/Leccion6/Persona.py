class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Silvio', 'Stefanucci', 31)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, Su edad es: {persona1.edad}')
persona2 = Persona('Juan', 'Cito', 48)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, Su edad es: {persona2.edad}')

persona1.nombre = 'Juanacio'
persona1.apellido = 'Viale'
persona1.edad = 11

print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, Su edad es: {persona1.edad}')

# Los atributos son las caracteristicas
# Los metodos son el comportamiento
persona1.mostrar_detalle()
persona2.mostrar_detalle()
