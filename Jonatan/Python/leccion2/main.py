"""
#CLASE 6 SENTENCIAS DE CONTROL (sentencia IF/ELSE
condicion = False
if condicion == True:
    print('Condicion es Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicion Sin especificar')

#ejecucion Debug en if/else
condicion = 10
if condicion == True:
    print('Condicion es Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicion Sin especificar')
"""
#ejercicio: Convercion de numero a Texto

# num = int(input('Digite un numero en el rango del 1 al 3: '))
# numTexto = ''
# if num == 1:
#     numTexto = 'Numero uno'
# elif num == 2:
#     numTexto = 'Numero dos'
# elif num == 3:
#     numTexto = 'Numero tres'
# else:
#     numTexto = 'Has ingresado un numero fuera de rango'
# print(f'El numero ingresado es: {num} - {numTexto}')

#Sintaxis simplificada(operador Ternario)
condicion = True
# if condicion :
#     print('Condicion Verdadera')
# else:
#     print('Condicion Falsa')

print('Condicion Verdadera') if condicion else print('Condicion Falsa') #Sintaxis simplificada (solo para codigos cortos