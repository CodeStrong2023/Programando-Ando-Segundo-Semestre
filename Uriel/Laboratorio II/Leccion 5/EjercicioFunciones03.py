#Ejercicio 03: Funcion recursiva
#Imprimir numeros del 5 al 1 de maera descendente usando funciones recursivas
#Puede ser cualquier valor positivo, por ejemplo si pasamos eñ valor de 5 debe imprimir
#5
#4
#3
#2
#1
#Si se ingresan numeros negtivos no debe imprimir
def imprimirRecursivos(numero):
    if numero >= 1:
        print(numero)
        imprimirRecursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto')
numero = int(input('Digite el numero a imprimir de manera descendente\n'))
imprimirRecursivos(numero)