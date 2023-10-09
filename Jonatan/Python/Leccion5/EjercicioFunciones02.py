#ejercicio2: funcion con *args para multiplicar
#Crear una Funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos variables *Args
#como parametros d ela funcion y regresar como resultado
#la funcion de todos los valores psados como argumentos

#7.1
#definimos la funcion para multiplicar
def multiplicar_valores(*numeros):#el mas utilizado es *args
    resultado = 1 #el cero no nos ayuda a pultiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

#llamamos a la funcion
print(multiplicar_valores(3,5,15,3))#pasamos los argumentos
