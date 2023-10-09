# Ejerciio 4: Sumar numeros pares dentro de un rango
# Hacer un programa para smarr numros pares dentro de un rango, por ejemplo>

#                                       suma de numeros pares de 2 al 30
#                                       suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quire llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0:
        suma += i

print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
