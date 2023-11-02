class Aritmetica:
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    #Metodo para sumar
    def sumar(self):
        return self.operandoA+self.operandoB

    def restar(self):
        return self.operandoA-self.operandoB

    def multiplicar(self):
        return self.operandoA*self.operandoB

    def dividir(self):
        return self.operandoA/self.operandoB

aritmetica = Aritmetica(7,9) #Le pasamos los argumentos
print(aritmetica.sumar())
print(f'La resta de los numeros es{aritmetica.restar()}')
print(f'La multiplicacion de los numeros es {aritmetica.multiplicar()}')
print(f'La division de los numeros es {aritmetica.dividir():.2f}')
