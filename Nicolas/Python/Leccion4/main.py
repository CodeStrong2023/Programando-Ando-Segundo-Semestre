# Lista = Ariel , Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas es lo que se conocen en otros lenguajes como Arreglos y Vectores
nombres = ['Naty' , 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

# print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0 , 1 , 2 
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametros la lista

# Agregamos un elemento
nombres.append("Marcelo")
#nombres.append(1,2,3)
#nombres.append(True)
#nombres.append(10,45)
# Pueden haber elementos float, boolean, int, etc
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)

nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # "del" significa Delete
print(nombres)
# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) # Aqui nos mostrara error al estar borrado

# Definimos una tupla
cocina =('cuchara' , 'cuchillo' , 'tenedor')
print(cocina)

# Acceder a un elemento, para esto usamos corchetes no parentesis.
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea un elemento: una coma
# de lo contrario seria un tipo string cadena.

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando /n para saltos de linea
    print(cocinar, end=' ')  # Usamos End = para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print(cocina)

#  del cocina # esto es para elimiar una tupla

# Tipo set

planetas = {"Marte", "Jupiter", "Venus"}
print(len(planetas)) # Usamos la funcion len para mostrar la cantidad de elementos
print("Marte" in planetas)

# Agregar un elemento
planetas.add("Tierra") # Add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe

planetas.remove ("Jupiter") # Essta funcion ante un mal ingreso o inexistencia da error
print(planetas)
planetas.discard("Tierra") # Esta funcion no nos presente ningun tipo de error
print(planetas)


# Limpiar set
#planetas.clear()
#print(planetas)

# Eliminar set o conjunto
#del planetas
#print(planetas)

# "Maradona" :10  Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "POO":"Programacion Orientada a Objetos",
    "SABD":"Sistema de Administracion de Base de Datos"
}
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)    
# Necesitamos una funcion para recorrer un diccionario    
for termino, valor in diccionario.items():
    print(termino, valor)
    
# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves


for valor in diccionario.values():
    print(valor)



# Comprobar la existencia de algun elemento

print("IDE" in diccionario) # Devuelve un booleano


# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Elimiar diccionario
del diccionario # El diccionario se borra


# Concatenamos listas
lista1= [1, 2 ,3]
lista2= [4 ,5, 6]
lista3= lista1+lista2 # Concatenamos las listas
print(lista3)

lista3.extend([7,8, 9]) # Funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # Esto daria un error por no ser elemento de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de una lista

# Paraponer al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente la lista
print(lista3)

# Repaso de Tuplas
tupla = (4, "Hola", 6.78, [1, 2 , 50], 4, "Hola")
print(tupla)



print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye",}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Bye")
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

# Operaciones en conjuntos

conjunto3 = conjunto1 | conjunto2   # La linea une los dos conjuntos
print(conjunto3)


conjunto3 =  conjunto1 & conjunto2   # Que elemento tienen en comun
print(conjunto3)
conjunto3 = conjunto1 - conjunto2  # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2   # Elementos que no comparten o que son diferentes
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del cojunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es s ino comparten elementos en comun

print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun


# Convertir un conjunto totalmente inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se pude agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {"Azul" : "Blue", "Rojo" : "Red", "Verde" : "Green" , "Amarillo" : "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel": {"Edad": 40, "Altura": 1.83}, "Osvaldo": [45, 1.85], "Natalia" : [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre" : "Lionel Messi", "Edad": 35 , "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo"},
    11: {"Nombre" : "Angel Di Maria", "Edad": 35 , "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo"}
}

print(seleccionArgentina[10])


for llave,  valor in seleccionArgentina.items():
    print(llave, valor)


# Pilas usando listas

pila = [1, 2 , 3]

# Agregamos elementos a la pila por el final

pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()   # Funcion pop elimina el ultimo elemento de la pila
print(pila)


# Con variable
elementoBorrado = pila.pop() # Quita el elemento y lo guarda en la variable
print(f"Sacamos el el emento {elementoBorrado}")
print(f"La pila ahora quedo asi: {pila}")


# Colas con listas

# Estructura de datos de tipo fifo (first input / firstouput)

cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

# Agregamos elementos al final de la cola

cola.append("Natalia")
cola.append("Jose")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f" Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]} ")





    
    





    
    







    




      
      
      

