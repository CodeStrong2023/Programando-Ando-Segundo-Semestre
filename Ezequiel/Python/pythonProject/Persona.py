class Persona: # Creamosuna clase
    def __init__(self,nombre, apellido,dni, edad, *args, **kwargs): #se lo llama metodo Init Dunder
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni # Atributo encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual al this
        print(f''
              f'a clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad},'
              f'la direccion es: {self.args}, los datos importantes son:  {self.kwargs}')

persona1 = Persona('Ezequiel', 'Lorenz',9878676, 28) #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(type(Persona))

persona2 = Persona('Osvaldo', 'Gioradani',343459276, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

#Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # lareferencia se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #de esta manera hay que pasar por parametros porque sino da error

#En python se puede crear un atributo de un ojeto en una misma linea y asignarlo, pero en este caso es para este unico objeto
persona1.telefono = '112453245234'
print(persona1.telefono)

persona3 = Persona('Rogelio', 'Romero',283459276, 22, 'Telefono', '12345891735', 'Calle lopez', 823, 'Manzana', 77, 'Casa', 17, Altura=1.83, Peso=105, CFavorito='Azul',Auto='Citroen', Modelo=2021)

persona3.mostrar_detalle()

persona4 = Persona('Romulo', 'Perez',28345926, 33, 'Telefono', '54765', 'Calle Lehmann', 999, 'Manzana', 88, 'Casa', 9, Altura=1.87, Peso=87, CFavorito='Verde',Auto='Peugeot', Modelo=2023)

persona4.mostrar_detalle()

# print(persona3._dni) esto no se debe utilizar en python, esto dice que desconocemos el uso de python

#persona3.__nombre => esta totalmente encapsulado, no se puede acceder a el