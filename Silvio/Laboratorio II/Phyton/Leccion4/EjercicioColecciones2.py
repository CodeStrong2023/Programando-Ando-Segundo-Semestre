# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (sin repeticion de elementos)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

curso1 = ['Carlitos', 'Josesito', 'Pascual', 'Mirando', 'Paco']
curso2 = ['Ayaya', 'Paca', 'Irma', 'Sandrita', 'Teresa', 'Carlitos']

# 1
lista1 = list(set(curso1 + curso2))
print(lista1)

# 2
lista2 = [nombre for nombre in curso1 if nombre not in curso2]
print(lista2)

# 3
lista3 = [nombre for nombre in curso2 if nombre not in curso1]
print(lista3)

# 4
lista4 = [nombre for nombre in curso1 if nombre in curso2]
print(lista4)
