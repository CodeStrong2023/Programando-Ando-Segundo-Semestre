#Ejercicio 04: Sumar numeros pares dentro de un rango
#hacer un programa para sumar numeros pares dentro
#de un rango, por ejemplo:
#                                   suma de numeros pares del 2 al 30
#                                   suma = 240

numero1=int(input('Digite de donde va a comenzar la suma: '))#pedimos al usuario donde comienza la suma
numero2=int(input('Difite hasta donde quiere llegar la suma: '))#pedimos al usuario donde termina la suma
suma = 0
for i in range(numero1,numero2+1):#para el iterador en el rango 1 y 2 (+1 por que comienza de 0 hasta -1
    if i % 2 == 0:#si es divisible por 2 significa que es par,
        suma += i#a la variable suma se le suma el mismo iterador
print(f'\nLa suma de los numeros pares dentro del rango es: {suma}')#mostramos al usuario el resultado
