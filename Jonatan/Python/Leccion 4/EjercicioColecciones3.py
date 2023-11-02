#Ejercicio 3 : agregar Personajes a una Lista
#Escriba un programa donde cree una lista con los siguientes personajes del senior de los anillos
#nombre: Aragon
#clase: gerrero
#raza: Dunadan del norte

#nombre: gandalf
#clase: mago
#raza: istar

#nombre: Legolas
#clase: arquero
#Raza: elfo sindar

personajes = [] #creamos una lista vacia
#creamos diccionarios
P1 = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza':'Dunadan del Norte'}
personajes.append(P1) #con .append agregamos un dicc a una lista
P2 = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza':'Istar'}
personajes.append(P2)
P3 = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza':'Elfo Sindar'}
personajes.append(P3)
P4 = {'Nombre': 'Sauron', 'Clase': 'Senior Oscuro', 'Raza':'Maia Corrompido'}
personajes.append(P4)
P5 = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza':'Enano'}
personajes.append(P5)
P6 = {'Nombre': 'Boromir', 'Clase': 'Guerrero', 'Raza':'Humano'}
personajes.append(P6)

print(personajes)