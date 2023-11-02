# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguinetes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre : Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista vacia
# Creamos un diccionario

P = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del Norte"}
personajes.append(P) # Agregamos a la lista un personaje
P = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)
P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)

print(personajes)