# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor  de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arqeuro
# Raza: Elfo Sindar

personajes = []

# Creamos diccionarios

P = {'Nombre': 'Aragon','Clase': 'Guerrero', 'Raza': 'Dunadan del norte'}

# Agregamos a la lista un personaje
personajes.append(P)
P = {'Nombre': 'Gandalf','Clase': 'Mago', 'Raza': 'Istar'}

# Agregamos a la lista un personaje
personajes.append(P)
P = {'Nombre': 'Legolas','Clase': 'Arqeuro', 'Raza': 'Elfo Sindar'}

# Agregamos a la lista un personaje
personajes.append(P)
print(personajes)

# Tarea agregar otros 3 personajes:

# Continuamos agregando más personajes
P = {'Nombre': 'Frodo', 'Clase': 'Hobbit', 'Raza': 'Hobbit'}
personajes.append(P)

P = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}
personajes.append(P)

P = {'Nombre': 'Galadriel', 'Clase': 'Elfa', 'Raza': 'Elfo Noldor'}
personajes.append(P)

print(personajes)

