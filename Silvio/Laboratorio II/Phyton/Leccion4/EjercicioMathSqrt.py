import math

# Sacar la raiz cuadrada de una numero positivo

numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error --> Deberia ser una numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')
