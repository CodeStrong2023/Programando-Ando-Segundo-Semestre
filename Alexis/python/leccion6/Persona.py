class Persona: # creamos una clase
    def __int__(self, nombre, apellido, dni, edad, *args, **kwargs): # se lo llama metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta encapsulado de una manera segerida
        self.edad = edad
        self.args = args
        self.wkargs = kwargs
    def mostrar_detalle(self): # self es igual a this
        print(f"la clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.wkargs}")

persona1 = Persona("ariel", "betancut",32456987, 40) # necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f"el objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}")
persona2 = Persona("osvaldo", "giordanini", 30321456, 45)
print(f"el objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}")

persona1.nombre = "liliana"
persona1.apellido = "buccela"
persona1.edad = 40
print(f"el objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}")

# los atributos son: caracteristicas
# los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) debemos pasarle una referencia para el self o dara error
persona1.telefono = "12345678"
print(f"este es el telefono de {persona1.nombre} {persona1.telefono}") # hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona("rogelio", "romero", 35789456,  22, "telefono", "87654321", "calle lopez", 823, "manzana", 77, "casa", 18, Altura=1.83, Peso=105, CFavorito="azul", Auto="citroen", Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) # esto no se debe utilizar(esta encapsulado), esto dice que lo desconocemos python
# persona3.__nombre # esta totalmente encapsulado




