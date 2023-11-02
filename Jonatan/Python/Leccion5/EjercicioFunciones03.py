#ejercicio3: Funcion Recursiva
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivos, por ejemplo si pasamos el
#calor de 5 debe imprimir 5 4 3 2 1 en casoi de ser 3 debe ser 3 2 1
# si se ingresa num negativo no se imprime nada

def imprimir_numeros_rescursivos(numero):
    if numero >= 1:#caso base
        print(numero)
        imprimir_numeros_rescursivos(numero -1)#caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')


num = int(input('Digite un numero: '))#pedimos al usuario el numero
imprimir_numeros_rescursivos(num)#asignamos la variable con el dato ingresado por el usuario