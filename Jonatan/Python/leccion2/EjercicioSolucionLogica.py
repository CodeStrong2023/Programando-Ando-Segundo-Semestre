'''
Ejercicio 2 determinar la solucion logica de la siguiente exprecion:
((3 + 5 x 8 ) < 3 and (( - 6 /3 x 4) + 2 < 2)) or ( a > b)
'''

a = float(input("Digite el calor de a\n"))
b = float(input("Digite el valor de b\n"))

resultado = ((3 + 5 * 8) < 3 and ((-6/3 * 4 ) + 2 < 2)) or ( a > b)

print(f'La Solucion logica de la exprecion es: {resultado}')