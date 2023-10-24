class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es una documentacion de la clase en python
    Vamos a hacer en esat clase algunas operaciones de: suma, resta, multiplicacion y mas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    #MEtodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,9)
print(f'La suma de los numeros es: {aritmetica1.sumar()}')
print(f'La Resta de los numeros es: {aritmetica1.resta()}')
print(f'La multiplicacion de los numeros es: {aritmetica1.multiplicar()}')
print(f'La division de los numeros es: {aritmetica1.dividir():.2f}')