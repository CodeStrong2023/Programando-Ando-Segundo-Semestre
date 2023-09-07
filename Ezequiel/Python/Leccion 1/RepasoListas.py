#una lista puede tenrer diferentes tipos de datos
nombres = ['Eze','Nati','Jona','Uriel','Silvio']
print(nombres)
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)

#concatenar listas

lista1 = [1,2,3]

lista2 = [6,5,4]

lista3 = lista1 + lista2

print(lista3)

lista3.extend([8,7,9])
print(lista3)


#ubicar en que indice esta el valor ingresado
print(lista3.index(5))

#como saber cunatos valores repetidos hay en la lsita dependiendo del numero que le ingresp
print(lista3.count(1))

#para que una lista se multiplique repitiendo sus eleemtnos

lista3 = lista3*2
print(lista3)

#ordenar de manera ascendente los elementos de la lista
lista3.sort()
print(lista3)
#ordenada de manera descendente
lista3.sort(reverse=True)
print(lista3)
