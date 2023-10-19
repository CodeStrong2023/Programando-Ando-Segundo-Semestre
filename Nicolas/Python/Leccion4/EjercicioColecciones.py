# Ejercicio 1 : Eliminar duplicados de una lista
# Escriba u nprograma donde tenga una lista y que a continuacion
# elimine los elekmentos repetidos, por ultimo mosrar la lista.

# Creamosuna lista
lista = [1, 2, 3, "Ariel" ,7 ,7 , 3, "Alberto", 1, "Ariel", 2, "Alberto"]
# conjunto = set(lista)  # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversion hecha en una sola linea de codigo
print(lista)

