# ejercicio 4: sumar numeros pares dentro de un rango
# hacer un programa para sumar numeros pares dentro
# de un rango, por ejemplo:
#                           suma de numeros pares del 2 al 30
#                           suma = 240
a = int(input("digite de donde va a comenzar la suma: "))
b = int(input("digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0: # esto es si el numero es par
        suma += 1
print(f"\nla suma de numeros pares del rango es: {suma}")

