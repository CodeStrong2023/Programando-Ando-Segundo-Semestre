# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
# numerics, utilizando argumentos variables *args como parametro de a funcion,
# y agregar como resultado la suma de todos los valores pasados como argumentos
def sumarValor(*args):  # recibimos una cantidad de parametros indefinidos
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


# llamamos a la funcion
print(sumarValor(3, 5, 9))
