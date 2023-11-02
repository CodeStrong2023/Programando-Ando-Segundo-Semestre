# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funcones recursivas
# puede ser cualqueir positico, por ejemploo, se pasamos el valor 5 , debeimprimir:
# 5
# 4
# 3
# 2
# 1

# Em caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1

# Si se ingresan numeros negtivos no imprime nada


def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        raise ValueError('Valor ingresado incorrecto...')

# imprimir_numeros_recursivos(1)
# Solicitar al usuario que ingrese un número
try:
    numero = int(input("Ingresa un número para imprimir números recursivos: "))
    if numero >= 0:
        imprimir_numeros_recursivos(numero)
    else:
        print('Valor ingresado incorrecto...')
except ValueError as e:
    print(f'Error: {e}\nDebes ingresar un número entero válido.')
