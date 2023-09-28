#Ejercicio 04:
#Sumar los numeros pares dentro de un rango
#Ejemplo:
# rango 0 a 30
# suma: 240
suma = 0
rango = int(input('Digite el numero final del rango iniciado en 0\n'))
numeros = range(0, rango+1)
for numero in numeros:
    if numero % 2 == 0:
        suma += numero
print(f'La suma de los pares dentro del rago es {suma}')
