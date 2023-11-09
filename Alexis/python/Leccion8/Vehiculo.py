class Vehiculo:
    '''
    definir una clase padre llamada vehiculo y dos clases hijas llamada
    auto y bicicleta, las cuales heredan de la clase padre vehiculo. la clase
    padre debe tener los siguiente atributos y metodos

    vehiculo(clase padre)
    -atributos (color, ruedas)
    -metodos (__init__(color, ruedas) y __str__())

    auto(clase hija de vehiculo)
    -atributos(velocidad (km/hr))
    -metodos(__init__(color, ruedas, velocidad) y __str__())

    bicicleta(clase hija de vehiculo)
    -atributo(tipo(urbana/montaña/etc.))
    -metodos(__init__(color, ruedas, tipo) y __str__())

    crear un objeto de cada clase
    '''

    def __int__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'color: ' + self.color + ' ruedas: ' + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', tipo: ' + self.tipo


# primer objeto de la clase padre vehiculo
vehiculo = Vehiculo('blanco', 4)
print(vehiculo)

# segundo objeto de la clase auto
auto = Auto('amarillo', 4, 120)
print(auto)

# tercer objeto, el ultimo de la clase bicicleta
bici = Bicicleta('azul', 2, 'urbana')
print(bici)
