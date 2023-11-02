class Cubo:
    """
     Crear la clase cubo con los atributos, ancho, alto, profundidad, con
     un metodo clacular_volumen que tendra la formula:
     volumen = ancho * altura * profundidad
     que el usuario ingrese los valores.
    """
    def __init__(self , ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input('Digite el numero del Ancho del cubo: '))
alto = int(input('Digite el numero de la Altura del cubo: '))
profundidad = int(input('Digite el numero de la Profundidad del cubo: '))

cubo1 = Cubo(ancho,alto ,profundidad)#creamos un constructor y le asignamos la clase cubo con los parametros ancho, altura y profundidad
print(f'El Volumen del cubo es : {cubo1.calcular_volumen()}')#interpolamos el constructor con el metodo de calcular volumen. para mostrar el resultado