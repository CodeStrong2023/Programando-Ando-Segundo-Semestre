# ejercicio 6: tabla de multiplicar
# hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. por ejemplo:
# si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

numero = int(input("digite un numero: "))
lista = [] # creamos una lista vacia
for i in range(1, 11):
    lista.append(i*numero)

print(f"\n tabla de multiplicar de {numero}: \n {lista}")

for indice,i in enumerate(lista):
    print(f"{numero} x {i} = {lista[indice]}") # este ciclo es para ver el formato de una tabla de multiplicar
