# Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
#Nombre : Aragon
#Clase: Guerrero
#Raza: Dúnadan del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

personajes = []#Creamos la lista vacia
#Creamos  diccionarios
p= {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(p)
p = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)
p = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
p = personajes.append(p)
for personaje in personajes:
    print(personaje)