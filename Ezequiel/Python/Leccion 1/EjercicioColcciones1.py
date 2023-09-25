#Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion elimine
# los elementos repetidos, por ultimo mostrar la lista.

# Creacion de la lista

lista = [1, 2, 3, "Ezequiel", 7, 8, 8, 9, "Ezequiel", 5, "Juan"]

#conjunto elimina los duplicados
conjunto = set(lista)

lista = list(conjunto) # convertimos el conjunto a una lista

print(lista)


# se puede resumir en una linea de codigo:

lista = list(set(lista))
print(lista)