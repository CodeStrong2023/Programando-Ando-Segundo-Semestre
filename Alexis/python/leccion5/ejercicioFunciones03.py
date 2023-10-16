# ejercicio 3: funcion recursiva
# imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# puede ser cuarquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# en caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# si se ingresan numeros negativos no imprime nada
def imprimir_numero_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("valor ingresado incorrecto...")

imprimir_numero_recursivos(5) # tarea: que el numero lo ingrese el usuario











