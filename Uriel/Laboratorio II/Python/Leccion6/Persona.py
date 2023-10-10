class Persona:
    def __init__(self, nombre, apellido, edad): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre}, {self.apellido}, {self.edad}')
persona1 = Persona('Juan', 'Zalazar', 22)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Uriel', 'Pardo', 27)
print(f'Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')

print(f'Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'Obejto modificado -> Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}')

#Los atributos son caracteristicas
#Los metodos son el comportamiento de los objetos(acciones)

persona1.mostrarDetalle()
persona2.mostrarDetalle()