class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, edad, dni, *args, **kwargs ): # Se lo llama como metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    
    def mostrar_detalle(self): # self es igual a this
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son : {self.kwargs}")  
          

persona1 = Persona("Ariel", "Betancud", 32456987,  40) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Nicolas", "Sini", 42266398,  23)
print(f"Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}")

persona1.nombre = "Matias"
persona1.apellido = "Sini"
persona1.edad = 34
print(f"Nombre {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}")


# Los atributos son : Caracteristicas
# Los metodos son : El comportamiento que van a tenerl os objetos(acciones)
      
persona1.mostrar_detalle()  # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle()  # Debemos pasarle una referencia para el self o dara error
persona1.telefono = "2604088892" # Hemos creado un atributo de un objeto
print(f"Este es el telefono: {persona1.telefono}")

# print(persona2.telefono) # el objeto persona2 no tiene este atributo, da error

persona3 = Persona("Sabrina", "Gutierrez", 24 , 41321456, "Telefono", "2604777777", "Calle Alberdi", 77, "Casa", 7, Altura=1.50, Peso= 50, CFavorito= "Rojo", Moto= "Motomel 110", Modelo= 2020)

persona3.mostrar_detalle()
#print(persona3._dni) # esto no se debe utilizar en python(esta encapsulado), esto dice que lo desconocemos python


