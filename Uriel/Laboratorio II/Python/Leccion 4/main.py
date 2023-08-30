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
'''
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
print(diccionario)
