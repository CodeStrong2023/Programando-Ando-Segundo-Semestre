#ejercicio 05: Factorial de un numero positivo
#hacer un programa para calcular el factoriald e un numero positrivo

num = int(input('Digite un numero positivo: '))
factorial = 1

while num < 0: #mientras el numero sea negativo
    print('Error, el numero debe ser positivo')
    num = int(input('Digite un numero positivo: '))

for i in range(1,num+1):
    factorial *= i

print(f'\nEl factorial del numero {num} positivo ingresado es: {factorial}')

"""El factorial de un número entero no negativo, denotado por "n!" (pronunciado "n factorial"),
es el producto de todos los números enteros positivos desde 1 hasta n. En otras palabras,
el factorial de un número n se calcula multiplicando todos los enteros positivos desde 1 hasta n. Aquí tienes la notación:

n! = 1 * 2 * 3 * ... * (n-2) * (n-1) * n

Por ejemplo:

    5! = 1 * 2 * 3 * 4 * 5 = 120
    3! = 1 * 2 * 3 = 6
    1! = 1 (por definición)

Los factoriales se utilizan en matemáticas y en programación para resolver una variedad de problemas,
como cálculos combinatorios, probabilidades, permutaciones y más. También son útiles en algoritmos y
ecuaciones que involucran secuencias numéricas.
"""
