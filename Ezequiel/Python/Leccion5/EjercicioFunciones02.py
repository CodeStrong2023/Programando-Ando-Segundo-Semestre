# Ejerciio 2: Funcio con * args para multiplicar
# crear una funcion para multiplicar los valores recibidos de tipo numerico
# utiliando argumentos variables *args como parametro de la funcion y regresar ocmo resultado
# la multiplicacion de todos los valores asados como argumentos

# Definimos la funcion para multiplicar
def multiplicar_valores(*numeros): #El mas ultizado es * args
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

# llemamos a la funcion
print(multiplicar_valores(3,5,15)) # le pasamos los argumentos