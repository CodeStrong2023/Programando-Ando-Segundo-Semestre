#clase
class Persona:  # creamos una clase
    #metodos
    def __init__(self,nombre, apellido, dni, edad, *args, **kwargs):# se lo llama metodo Init Dunder
        self.nombre = nombre#el doble __ evita ser modificado
        self.apellido = apellido
        self._dni = dni#este Atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args#tupla
        self.kwargs = kwargs#diccionario

    def mostrar_detalle(self):#self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad},la direccion es: {self.args}, los datos importantes son {self.kwargs}')

#objeto1
persona1 = Persona('Antonio','Rios',398764558, 45)#necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
#objeto2
persona2 = Persona('Osvaldo','Giordanini',40400400, 50)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

#MODIFICAR ATRIBUTOS
persona1.nombre = 'Vanesa'
persona1.apellido = 'Ferreyra'
persona1.edad = 40
print(f'El objeto 1 MODIFICADO de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')


#Los atributos son : Caracteristicas para nuestros objetos
#los metodos son el comportamientos que van a tener los objetos
persona1.mostrar_detalle() #La referencia se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) debemos pasarle una referencia para el self o dara error
persona1.telefono = '1234123412'
print(f' Este es el telefono de : {persona1.nombre} {persona1.telefono}')

#print(persona2.telefono) El objeto persona 2 no tiene este atributo, da error

persona3 = Persona('Rogelio','Romero', 3434987456,22, 'Telefono', '2605989898', 'Calle lopez', 'Manzana', 77,'Casa',18, Altura=1.83, Peso=105, cFavorito='Azul', Auto= 'Citroen', Modelo= 2021 )
persona3.mostrar_detalle()

persona4 = Persona('Manuel','Belgrano', 9876545,60, 'Telefono', '3764980054', 'Calle Antunez', 'Manzana', 12,'Casa',6, Altura=1.75, Peso=79, cFavorito='Negro', Auto= 'Toyota', Modelo= 2023 )
persona4.mostrar_detalle()
#print(persona4._dni) Esto no se debe UTILIZAR ( esta encapsulado), esto dice que lo desconocemos
#persona3.__nombre Esta total mente encapsulado