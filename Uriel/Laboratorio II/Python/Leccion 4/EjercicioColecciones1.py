# Ejercicio1: Eliminar duplicados de una lista y que a continuacion
#elimine los elementos repetidos, por ultimo mostrar la lista

 #Creamos una lista
lista = [1, 2, 3, "Ariel", 7,7, 3, "Alberto", 5, "Ariel", 2, "Alberto"]
#conjunto = set(lista)#Convertimos la lista a un conjunto tipo set
#lista = list(conjunto)#Convertimos el conjunto a una lista
lista = list(set(lista))#Conversion en una sola linea
print(lista)