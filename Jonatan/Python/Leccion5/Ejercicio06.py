#EJERCICIO 06: TABLA DE MULTIPLICAR
#HACER UIN PROGRAMA QUE PIDA UN NUMERO POR TECLADO Y GUARDE
#EN UNA LISTA SU TABLA DE MULTIPLICAR HASTA EL 10, POR EJMEMPLO:
#SI DIGITA EL 5 LA LISTA TENDRA: 5,10,15,20,25,30,35,40,45,50

num = int(input('Digite un numero: '))#pedimos al usuario el numero a multiplicar
tabla = []#iniciamos una tabla vacia

for i in range(1,11):#llenamos la tabla del 1 al 10 con el ciclo for
    tabla.append(i*num)
print(f'\nTabla de Multiplicar del {num} es: \n {tabla}')#mostramos el resultado al cliente

for indice,i in enumerate(tabla):#enumerate sirve para enumerar una tabla
    print(f'{num} x {i} = {tabla[indice]}')
"""
La funcion enumerate en python se utuliza para agregar un contador a un iterable, como una lista, tupla o cadena, y que permite
obtener tanto el valor como el indice(posicion) de cada elemento ene l iterable dorante el bucle for.
"""