'''
Ejercicio 4 hacer un programa para ingresar el radio de un circulo y reporte su area y longitud d ela circunferencia
area = pi * r2
long = 2 * pi * r

en este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de pi
se ecribe : inport math
'''

import math
radio = float(input("Digite el radio del circulo \n"))
area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f'El area del circulo es {area}')
print(f'La longitud del ciurculo es {longitud}')
