# Ejercicio 02:
#Funcion con *args para multiplicar
#Crear una funcion para multiplicar valores recibidos de tipo numerico, utilizando argumentos variables *args
#como parametro de la funcion y regresar como resultado
#La multimplicacion de todos los valores pasados como argumentos
def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

print(f'El resultado de la multiplicacion es: {multiplicar(8, 5, -2, 1, -1)}')