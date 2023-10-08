#dada la siguiente TUPLA
tupla = (13, 1, 8, 3, 2, 5, 8)#$definimos la tupla
#crear una Lista que solo incluyan los numeros menores a 5
#e imprima por consola [1, 3 , 2]

lista = []#definimos la lsita
#filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)