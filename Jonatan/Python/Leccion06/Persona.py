#clase
class Persona:  # creamos una clase
    #metodos
    def __init__(self,nombre,apellido,edad):# se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

#objeto1
persona1 = Persona('Antonio','Rios',55)#necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
#objeto2
persona2 = Persona('Osvaldo','Giordanini',56)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

#MODIFICAR ATRIBUTOS
persona1.nombre = 'Vanesa'
persona1.apellido = 'Ferreyra'
persona1.edad = 40
print(f'El objeto 1 MODIFICADO de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')


#Los atributos son : Caracteristicas para nuestros objetos
#los metodos son el comportamientos que van a tener los objetos
persona1.mostrar_detalle()
persona2.mostrar_detalle()
