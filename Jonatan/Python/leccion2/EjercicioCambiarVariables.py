'''
Ejercicio 3 Intercambiar el valor de dos variables.
a = 10    ->  a=5
b = 5     ->  b=10
'''

a = int(input("Digite el valor de la Variable a\n"))
b = int(input("Digite el valor de la Variable b\n"))
aux = a
a = b
b = aux
print(f'El nuevo valor de a: {a}, y el nuevo valor de b: {b}')