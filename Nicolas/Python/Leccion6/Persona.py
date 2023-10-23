class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, edad): # Se lo llama como metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")    

persona1 = Persona("Ariel", "Betancud", 40) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Nicolas", "Sini", 23)
print(f"Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}")

persona1.nombre = "Matias"
persona1.apellido = "Sini"
persona1.edad = 34
print(f"Nombre {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}")


# Los atributos son : Caracteristicas
# Los metodos son : El comportamiento que van a tenerl os objetos(acciones)
      
persona1.mostrar_detalle()
persona2.mostrar_detalle()