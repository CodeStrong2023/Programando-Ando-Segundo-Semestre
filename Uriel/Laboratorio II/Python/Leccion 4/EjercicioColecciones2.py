#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tengsa 2 listas y que a continuacion
#cree las siguientes listas (en las que no deben haber repeticiones)
#1 lista de palabras que aparecen en la lista
#2Lista de palabras que aparecen en la primera lista, pero no en la segunda
#Lista de palabras que aparecen en la segunda lista, pero no en la primera
#Lista de palabras que aparecen en las dos listas
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminar los elementos repetidos de ambas listas
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)#Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) #Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2)
print(f'Lista de palabras que aparecen en la lista {union}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda {solo1}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera {solo2}')
print(f'Lista de palabras que aparecen en las dos listas {interseccion}')