class Persona # Creamosuna clase
    def __init__(self,nombre, apellido, edad): #se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Ezequiel', 'Lorenz', 28) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(type(Persona))