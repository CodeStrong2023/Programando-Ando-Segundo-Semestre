# Crear una funcion para sumar los valores recibidos de tipo numericos,
# utilizando argumente variables *args como parametrode la funcion
# y agregar como resultado la suma de todos los valores pasados como argumentos

def suma(*args): # Recibimos una cantidad de parametros indefinidos
    # 'pass' Se utiliza para dejar inconclusa la funcion para luego completarla
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

# Llamamos a la funcion
print(suma(3, 4, 5, 6, 7, 8, 9))
