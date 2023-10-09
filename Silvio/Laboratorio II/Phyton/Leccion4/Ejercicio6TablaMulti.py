# Guardar en una lista la tabla de multiplicar del 1 al 10 de un numero dado

lista = []

amulti = int(input('Digite el numero para mostrar su tabla de multiplicacion: '))

for i in range(1, 11):
    lista.append(amulti*i)

print(lista)