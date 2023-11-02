# Ejercicio: 3 Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cualquier valor positico, por ejemplo, si pasamos el calor de 5 debe imprimir:
# 5 4 3 2 1

def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor Ingresado Inconrrecto')

cuentaRegresiva = int(input('Digite el numero para la cuenta regresiva: '))
imprimir_numeros_recursivos(cuentaRegresiva)
