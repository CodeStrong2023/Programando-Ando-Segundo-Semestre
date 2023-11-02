class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrarDetalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre}, {self.apellido}, {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Juan', 'Zalazar', 42505230,22)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Uriel', 'Pardo', 40003049,27)
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

persona1.telefono  = "2604121212"
print(f'Este es el telefono de {persona1.nombre} = {persona1.telefono}')

persona3 = Persona('Rogelio', 'Romero', 25151989, 22, 'Telefono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura = 1.83, Peso = 105, CFavorito = 'Azul', Auto = 'Citroen', Modelo = 2021)
persona3.mostrarDetalle()

persona4 = Persona('Federico', 'Sossa', 38456963, 28, 'Telefono', '2991212126', 'Calle Brasil', 711, 'Uva', 16, 'Departamento', 21, Altura = 1.79, Peso = 82.5, CFavorito = 'Naranja', Auto = 'Renault', Modelo = 2022)
persona4.mostrarDetalle()
#print(persona3._dni) #Esto no se debe utilizar en python,  esta encapsulado. Es una maera clara de demostrar que desconocemos python
#persona3.__nombre #Esta totalmente encapsulado
