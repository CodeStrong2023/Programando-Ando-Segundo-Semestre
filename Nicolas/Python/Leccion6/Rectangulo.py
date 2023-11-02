class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
        
    def calcularArea(self):
        return self.base * self.altura
    
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
area1= Rectangulo(base, altura)

print(f"El area del rectangulo es: {area1.calcularArea()}")

    
       
        
    