class Persona: # creamos una clase
    def __int__(self, nombre, apellido, edad): # se lo llama metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona("ariel", "betancut", 40) # necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f"el objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}")
persona2 = Persona("osvaldo", "giordanini", 45)
print(f"el objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}")

persona1.nombre = "liliana"
persona1.apellido = "buccela"
persona1.edad = 40
print(f"el objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}")

# los atributos son: caracteristicas
# los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle()


