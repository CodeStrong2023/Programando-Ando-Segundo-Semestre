# lista = Ariel, Liliana, Natalia, Osvaldo

'''
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)

print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

#Recorrido de lista
print(nombres[0:2])#Solo muestra desde el primer indice, hasta el anterior del ultimo
print(nombres[ :3])#Desde el inicio hasta el indice indicado(Sin icluirlo)
print(nombres[1: ])#Desde el indice indicado hasta el final

#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plurar
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
    
#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

#Insertamos un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminamos el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres)

#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))
#Accedemos a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

#Imprimimos de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:1])

#Recorrer los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end= ' ')

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print("\n",cocina)
del cocina
#print(cocina)

# Set, conjunto sin orden ni indice. Utilizan llaves para definirlas
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas))
print(planetas)

#Revisar si un elemento existe dentro de un set
print('Júpiter' in planetas) #Busca usando camelcase y acentos

#Agregar un elemento
planetas.add('Tierra')
planetas.add('Tierra')#Si existe un duplicado no se tiene en cuenta en los cambios
print(planetas)

#Eliminar elementos
planetas.remove('Jupiter')
print(planetas)
planetas.discard('tierra')
print(planetas) #Si se ingresa mal el nombre a borrar, con discard no rompe la ejecucion

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas
print(planetas)

#Diccionarios
# 'Maradona': 10 -> Un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
print(diccionario)
#Verificar la cantidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])
#Otro metodo
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer un diccionario
for termino in diccionario: #recorremos mostrando solo las llaves
    print(termino)
#Necesitamos una funcion para recorrer un diccinoario
for termino, valor in diccionario.items():
    print(termino, valor)
#Otras maneras
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves o keys

#Otra funcion
for valor in diccionario.values(): #Muestra solo el valor o value
    print(valor)

#Comprobamos la existencia de algun elemento
print('IDE' in diccionario) #Devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminamos un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un dicionario
diccionario.clear()
print(diccionario)

#Eliminar un diccionario
del diccionario
#print(diccionario)

#Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
#print(lista3)
lista3.extend([7, 8, 9])#Agrega elementos al final de la lista
#print(lista3)

#print(lista3.index(5))#indica el elemento y nos devuelve el indice donde se encuentra
#print(lista3.index(0))#Si el elemento no existe en la lista da error
#Como saber cuantos valores repetidos existen
#print(lista3.count(1))#Cuenta cuantos valores igual hay en la lista

#Para invertir la lista
#lista3.reverse()
#print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3]*2
print(lista)
#Metodo de ordenamientos
lista3.sort()#Ordena los elementos de forma ascendente
print(lista3)
lista3.sort(reverse=True)#Ordena de forma descendente
print(lista3)

tupla = (4, 'hola', 6.78, [4, 5, 6], 4, 'hola')
print(tupla)

#Conjunto es un grupo de elementos desordenados, donde no pueden haber duplicados
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)#verificamos la no existencia del elemento
print(conjunto2 == conjunto1)#verificamos igualdad entre conuntos

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #Une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Muestra los elementos que estan en los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))#verifica si c1 es subconjunto de c3
print(conjunto2.issubset(conjunto3))#verifica si c2 es subconjunto de c3
print(conjunto3.issubset(conjunto2))#verifica si c3 es subconjunto de c2
print(conjunto3.issubset(conjunto1))#verifica si c3 es subconjunto de c1
print()#Verifico los superconjuntos de manera similar
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

#Como saber si ambos conjuntos son disconexos, o sea no comparten elementos
print(conjunto1.isdisjoint(conjunto2))#No hay cosas en comun

#Convertitlo totalmente en inmutable
conjunto1 = frozenset #No se puede modificar ni eliminar

#Repaso dicionarios

diccionario = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionario)

#Como eliminar
del(diccionario['Azul'])
print(diccionario)

#Los diccionarios pueden almacenar distintos tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo':[45, 1.85], 'Natalia': [35, 1.67]}
for valor in diccionario2.items():
    print(valor)

seleccionArgentina= {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 25, 'Altura': 1.777, 'Precio': '35 millones', 'Posicion': 'Media punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 26, 'Altura': 1.75, 'Precio': '20 millones', 'Posicion': 'Lateral'},
    13: {'Nombre': 'Cristian Romero', 'Edad': 25, 'Altura': 1.85, 'Precio': '13 millones', 'Posicion': 'Defensa central'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Mediapunta'},
    9: {'Nombre': 'Julian Álvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '17 millones', 'Posicion': 'Delantero central'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print(seleccionArgentina[10])
print('Tenemos cargados en el diccionario la cantidad de jugadores:', end = ' ')
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1, 2, 3]
#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado= pila.pop()#Elimina el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora se ve asi: {pila}')

#Colas con listas
#Estructuras de datos del tipo FIFO(First Input, First Output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
seRetira = cola.pop(0)
print(f'Se retira {seRetira}')
print(cola)
'''