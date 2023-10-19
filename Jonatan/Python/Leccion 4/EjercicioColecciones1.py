#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos, por ultimo mostrar la lista

#creamos una lista
lista = [1,2,3,"Ariel",7,7,3,"Alberto",1,"Ariel",2,"Alberto"]
#conjunto = set(lista)#convertimos la lista en un conjunto de tipo set(el conjunto no permite datos repetidos)
#lista = list(conjunto)#volvemos a comvertir el conjunto a una lista
lista = list(set(lista))#la convercion hecha en una sola linea de codigo
#se resuelve de adentro hacia afuera, primero convertimos la lista en conjunto y el conjunto en una lista nuevamente
print(lista)
