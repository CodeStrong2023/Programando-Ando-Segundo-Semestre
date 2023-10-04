# ejercicio 01: crear una funcion para sumar los valores recibidos de tipo
# numericos, utilizando argumentos variables *args como parametro de la
# funcion y aregar como resutado la suma de todos los valores pasados
# como argumentos.
# definimos una  funcion
def sumar_valor(*args):
    resultado = 0
    # iteramoscada elemento
    for valor in args:
        resultado += valor
    return resultado


# llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1))







