class Aritmetica:
    """
    DocString
    Documentacion para clases
    Vamos a hacer algunas operaciones: suma, resta, multiplicacion y mas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

artimetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operandos

print(f'La suma es: {artimetica1.sumar()}')
print(f'La resta es: {artimetica1.resta()}')
print(f'La multiplicacion es: {artimetica1.multiplicar()}')
print(f'La division es: {artimetica1.dividir():.2f}')
