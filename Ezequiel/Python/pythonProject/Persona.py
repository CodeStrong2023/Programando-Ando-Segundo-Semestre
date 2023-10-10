class Persona # Creamosuna clase
    def __init__(self): #se lo llama metodo Init Dunder
        self.nombre = 'Juan'
        self.apellido = 'Zalazar'
        self.edad = 22

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(type(Persona))