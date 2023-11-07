class Vehiculo():
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @property
    def rueda(self):
        return self._ruedas
    @rueda.setter
    def rueda(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return 'Color: '+self._color+' Ruedas: '+str(self._ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return super().__str__()+', Velocidad(km/hora): '+str(self._velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return super().__str__()+' Tipo: '+self._tipo