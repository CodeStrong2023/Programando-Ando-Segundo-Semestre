#Ejercicio 06: Tabla de multiplicar
#Hacer un programa que pida un numero por teclado y guarde
#en una lista su tabla de multiplicar hasta el 10.
def multiplicar(numero):
    for i in range(1, 11):
        producto = numero*i
        print(f'{numero}*{i}= {producto}')
numero = int(input('Digite un numero entero\n\n'))
multiplicar(numero)