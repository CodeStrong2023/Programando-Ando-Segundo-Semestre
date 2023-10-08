import math

# Ejercicio de matematicas para sacar la raiz cuadrada de un numero positivo

numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('Error => Tiene que ser un numero positivo')
    numero = int(input('Digite un numero positivo:'))

print(f' \nSu raiz cuadrada es: {math.sqrt(numero): .2f}')