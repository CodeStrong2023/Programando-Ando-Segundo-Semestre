#CICLO WHILE(mientras o durante)
"""
contador = 0
while contador < 100:
    print('Ejecutamos nuestro ciclo While ', contador)
    contador += 1
else:
    print('Fin del ciclo while')

#imprimir numeros del 0 al 5 con el ciclo while
#acsendente
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
#decreciente
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1#operador simplificado -=

#ciclo FOR #el ciclo FOR nos permite iterar o recorrer un objeto
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

#Funcion BEACK se sa para romper la estructura al encontrar el primer elemento que buscamos
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')

#PALABRA RESERVADA CONTINUE #ejecuta la siguiente iteracion, aunque haya mas codigo

for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
"""

