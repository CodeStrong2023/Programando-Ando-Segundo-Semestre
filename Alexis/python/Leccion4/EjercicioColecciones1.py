# ejercicio 1: eliminar duplicados de una lista
# escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, porultimos mostrar la lista

# creamos una lista
lista = [1, 2, 3, "ariel", 7, 7, 3, "alberto", 1, "ariel", 2, "alberto"]
# conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # convertimos el conjunto a una lista
lista = list(set(lista)) # comversion hecha en una sola linea de codigo (eficiente)
print(lista)








