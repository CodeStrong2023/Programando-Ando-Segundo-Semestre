# Sumar números pares dentro de un rango

lista = []
suma = 0

print('Determinemos el rango')
start = int(input('Ingrese el valor en el que comenzará el rango: '))
end = int(input('Ingrese el valor en el que terminará el rango: '))

while end <= start:
    print('ERROR --> Ingrese un valor final mayor que el valor inicial')
    start = int(input('Ingrese el valor en el que comenzará el rango: '))
    end = int(input('Ingrese el valor en el que terminará el rango: '))

for numero in range(start, end + 1):
    if numero % 2 == 0:
        lista.append(numero)

for numero in lista:
    suma += numero

print('La suma de los números pares dentro del rango es:', suma)
