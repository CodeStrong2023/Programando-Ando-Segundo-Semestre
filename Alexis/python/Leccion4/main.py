# lista = ariel, liliana, natalia, osvaldo
# colecciones en python

# las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ["naty","osvaldo","lily","ariel"]
print(nombres)
print(nombres[0:2]) # solo muestra el indice 0, 1 pero no el indice 2
# ir de inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # indice a mostrar 0, 1, 2
# desde el indice indicado al final
print(nombres[1: ])
# modificamos un valor
nombres[3] = "lilina"
# print[0] = "natalia"
print(nombres)
for nombre in nombres: # nombre es singlar, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# preguntamos cuntos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# agregamos un elemento
nombres.append("marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)
# insertar un elemnento en un indice especifico
nombres.insert(1, "alberto")
nombres.insert(3, "devora")

#eliminamos un elemento
nombres.remove("alberto")
print(nombres)

# eliminar el ultimo elemento
nombres.pop()
print(nombres)

# eliminar un indice especifico
del nombres[2] # del significa detele (eliminar)
print(nombres)

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# eliminar la lista
del nombres
# print(nombres) # aqui nos mostrara un error

# definimos una tupla
cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))

# acceder a un elemento, para esto untilizamos corchetes no parentesis
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])

# acceder a un rango
print(cocina[0:1])
# ejemplo
verduras = ("papa",) # una tupla necesita sea de un elemento: la coma
# de lo contrario solo seria un tipo str cadena

# recorremos los elementos de la tupla
for cocinar in cocina: # print esta usando \n para saltos de lineas
    print(cocinar, end=" ") # usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

# del cocina esto es para eliminar una tupla

# tipo set
planetas = {"marte", "jupiter", "venus"}
print(len(planetas)) # usamos la funcion len = length significa largo

# revisar si un elemento existe dentro de set
print("jupiter" in planetas)

# agregar un elemento
planetas.add("tierra") # add es una funcion
print(planetas)

# eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("jupiter") # esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra")# esta funcion no nos presenta ningun error

# limpiar set
planetas.clear()
print(planetas)

# eliminar set
del planetas
# print(planetas) # al eliminar nos muestra un error

# "Maradona":10 un diccionario esta compuesto por dos eleentos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE": "integrated developent enviroment",
    "POO": "programacion orientada a onjetos",
    "SABD": "sistema de administracion de base de datos",
}
# verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# modificamos elementos
diccionario["IDE"] = "entorno de dessarrollo integrado"
print(diccionario)

# como recorrer los elementos
for termino in diccionario: #recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # estamos usando una funcion
    print(termino) # muestra solo las llaves

for valor in diccionario.values(): # usamos una funcion paraacceder al valor
    print(valor)

# comprobar la existencia dealgun elemento
print("IDE" in diccionario) # devuelve un booleano

# agregar un elemento
diccionario["PK"] = "primary key"
print(diccionario)

# eliminar una llave
diccionario.pop("SABD")
print(diccionario)

# vaciar un diccionario
diccionario.clear()
print(diccionario)

# eliminar un diccionario
del diccionario # el diccionario se borro

# concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista2 + lista1 # concatenacion
print(lista3)

lista3.extend([7, 8, 9, 1]) #funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # esto daria un error por no ser el elemento parte de la lista

# como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # cuenta cuantos valores iguales dentro de la lista

# para poner al reves una lista
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitinedp sus elementos
lista = [1, 2, 3] * 2
print(lista)

# metodos de ordenamiento
lista3.sort() # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # ordena descendentemente
print(lista3)

# repaso de tuplas
tupla = (4, "hola", 6.78, [1, 2, 78], 4, "hola") # puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # accion booleana, su respuesta es de tipo booleana
# lo que podemos usar dentro de tuplas son: index, count, len
# en tuplas se pueden convertir de tupla a lista y de lista a tupla

# repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1) # preguntamos si el numero 3 NO esta en el conjunto1

# como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # nos devuelve como respuesta un booleano

# operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # que elemneto tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comprarten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # aqui prenguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # si es verdadero quiere decir el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# como saber si ambos conjuntos son disconexos, esto es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # no hay cosas en comun

# convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar, modificar ni eliminar elementos del conjunto

# repaso diccionario
diccionarioNuevo = {"azul": "blue", "rojo": "red", "verde": "green", "amarillo": "yellow" }

# como eliminar
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

# los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"ariel": {"edad": 40, "altura": 1.83}, "osvaldo": [45, 1.85], "natalia": [35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"nombre": "Lionel Messi", "edad": 35, "altura": 1.70, "precio": "50 millones", "posicion": "extremo derecho"},
    11: {"nombre": "Angel Di Maria", "edad": 34, "altura": 1.80, "precio": "12 millones", "posicion": "extremo derecho"},
    24: {"nombre": "Paulo Dybala", "edad": 28, "altura": 1.77, "precio": "35 millones", "posicion": "media punta"},
    19: {"nombre": "Nicolas Otamendi", "edad": 34, "altura": 1.83, "precio": "3.5 millones", "posicion": "defensa central"},
    1: {"nombre": "Franco Armani", "edad": 35, "altura": 1.89, "precio": "3.5 millones", "posicion": "arquero"},
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# como tarea agregar po rlo menos 4 jugadores mas al diccionario: seleccionArgentina
print("tenemos cargados en el diccionario la cantidad de jugadores: ", end= " ")
print(len(seleccionArgentina))

# pilas usando listas
pila = [1, 2, 3]

# agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos desde el final
elementoBorrado = pila.pop() # quita el ultimo elemento y lo guarda en la variable
print(pila)
print(f"sacamos el elemento: {elementoBorrado}")
print(f"la pila ahora queda asi: {pila}")

# colas con listas
# estructuras de datos de tipo fifo(first input / first output)
cola = ["ariel", "osvaldo", "liliana", "pilar"]

# agregamos elementosal final de la cola
cola.append("natalia")
cola.append("jose")
print(cola)

# sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"atendido el cliente: {seRetira}")
print(cola)

# seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina}")








