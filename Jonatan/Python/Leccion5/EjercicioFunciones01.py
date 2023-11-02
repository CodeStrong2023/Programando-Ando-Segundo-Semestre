# Ejercicio 01: Crear una Funcion poara sumar los valores recibidos de tipo
# numericos, utilizando argumentos, variables *arg como parametros de la
# funcion y agregar como resultado la suma de todoslos valores pasados
# como argumentos

def sumar_valor(*args):  # recibimos una cantidad de datos indefinidos
    resultado = 0  # pass  # se utiliza para no dejar vacia una funcion para no tener error, luego volvemos a modificarlo
    # iterar cada elemento
    for valor in args:
        resultado += valor
    return resultado


# llamamos a la funcion
print(sumar_valor(3, 5, 9))
