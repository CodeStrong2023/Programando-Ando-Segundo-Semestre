# Listas: Una lista en Python es una estructura de datos que se utiliza para almacenar
# una colección ordenada de elementos. Estos elementos pueden ser de cualquier tipo,
# como números, cadenas de texto, otros objetos, e incluso otras listas. Las listas
# son mutables, lo que significa que puedes agregar, eliminar y modificar elementos
# después de crear la lista.
# .extend([]) agrega elementos a la lista
# .index(n) indica en que indice esta el elemento n
# .count(n) cuenta cuantos valores n hay dentro de la lsita
# .reverse() pone al revez una lista
# se puede multiplicar una lista
# Metodos de ordenamiento:
# .sort() ordena los elementos de la lista

mi_lista = [1, 2, 3, 4, 5]
lista_vacia = []
primer_elemento = mi_lista[0]  # Accede al primer elemento (1)
ultimo_elemento = mi_lista[-1]  # Accede al último elemento (5)
mi_lista[2] = 10  # Modifica el tercer elemento (índice 2) para que sea 10
mi_lista2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
mi_lista2.sort()  # Ordena la lista en orden ascendente
print("Lista: ")
print(mi_lista2)  # Resultado: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# Tuplas: Una tupla en Python es una estructura de datos similar a una lista, pero con
# una diferencia importante: las tuplas son inmutables, lo que significa que una vez que
# se crean, no puedes modificar su contenido. Se utilizan para almacenar una colección
# ordenada de elementos como números, cadenas de texto u otros objetos, de la misma
# manera que las listas.
# Ver si la tupla contiene el elemento n: n in tupla (respuesta tipo booleana)

print("Tupla: ")
mi_tupla = (1, 2, 3, 4, 5)
tupla_de_un_elemento = (42,)
primer_elementotupla = mi_tupla[0]  # Accede al primer elemento (1)
# mi_tupla[2] = 10  # Esto generará un error, ya que las tuplas son inmutables
mi_tupla2 = (1, 2, 3, 4, 5, 3)
cantidad_de_tres = mi_tupla2.count(3)  # Cuenta cuántas veces aparece el número 3 (2 veces)
indice_de_cuatro = mi_tupla2.index(4)  # Encuentra el índice del número 4 (índice 3)
ubicaciones = {(1, 2): 'Casa', (3, 4): 'Trabajo'}
print(ubicaciones)

# Set (Conjunto): Un conjunto en Python es una colección desordenada de elementos únicos.
# Los conjuntos se utilizan cuando deseas almacenar elementos sin duplicados y no te importa
# el orden en el que se almacenan. Los conjuntos son mutables, lo que significa que puedes
# agregar o eliminar elementos después de crearlos.

print("Set:")
mi_set = {1, 2, 3, 4, 5}
conjunto_vacio = set()
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)  # Agrega el elemento 4 al conjunto
mi_conjunto.remove(2)  # Elimina el elemento 2 del conjunto, si no esta el elemento, genera error
mi_conjunto.discard(5)  # Intenta eliminar el elemento 5, no genera error por no estar
mi_conjunto.clear() # Limpia los elementos del conjunto
del mi_conjunto # Elimina el Set

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

union = conjunto1 | conjunto2  # Unión de conjuntos
interseccion = conjunto1 & conjunto2  # Intersección de conjuntos
diferencia = conjunto1 - conjunto2  # Diferencia entre conjuntos

# Uso de conjuntos:
# Los conjuntos son útiles cuando necesitas almacenar una colección de elementos
# únicos y no te importa el orden. Se utilizan comúnmente para eliminar duplicados
# de una lista, verificar la existencia de elementos únicos o realizar operaciones de conjuntos.
# Por ejemplo, puedes utilizar un conjunto para eliminar duplicados de una lista:

mi_lista = [1, 2, 2, 3, 4, 4, 5]
mi_set = set(mi_lista) # Al copiar la lista a un set, elimino los duplicados de la lista
lista_sin_duplicados = list(mi_set)
print(mi_set)

# Diccionario: Un diccionario en Python es una estructura de datos que se utiliza
# para almacenar una colección de pares clave-valor. Cada elemento en un diccionario
# consiste en una clave única y su valor asociado. Los diccionarios son mutables,
# lo que significa que puedes agregar, modificar o eliminar elementos después de crearlos.

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
diccionario_vacio = {}
nombre = mi_diccionario["nombre"]  # Accede al valor asociado con la clave "nombre"
nombre1 = mi_diccionario.get("nombre") # Acceder a un valor de forma segura
mi_diccionario["edad"] = 31  # Modifica el valor asociado con la clave "edad"

mi_diccionario["profesion"] = "Ingeniero"  # Agrega un nuevo par clave-valor
del mi_diccionario["ciudad"]  # Elimina la clave "ciudad" y su valor asociado

claves = mi_diccionario.keys()  # Devuelve una lista de claves
valores = mi_diccionario.values()  # Devuelve una lista de valores
pares = mi_diccionario.items()  # Devuelve una lista de tuplas clave-valor

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print("Diccionario:")
print(persona)
