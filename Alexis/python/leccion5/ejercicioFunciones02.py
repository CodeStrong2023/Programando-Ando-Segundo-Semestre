# ejercicio 2: funcion con *args para multiplicar
# crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumento

# definimos la funcion para multiplicar
def multiplicar_valores(*numeros): # el mas utilizado es *args
    resultado = 1 # el cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

# llamamos a la funcion
print(multiplicar_valores(3, 5, 15, 3)) # le pasamos los argumentos






