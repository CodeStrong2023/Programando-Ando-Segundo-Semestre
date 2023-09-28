# LISTAS
# COLECCIONES EN PYTHON

# las listar es lo que se conoces en otros lenguajes como ARREGLOS O VECTORES

nombres = ['Jona', 'Nati', 'Aixa', 'Ariel']
"""
print(nombres)
print(nombres[0]) Imprimiendo indices seleccionados
print(nombres[1])
print(nombres[3])
print(nombres[-1])

print(nombres[0:2]) #imprimiendo desde el indice 0 hasta el 2
#para ir desde el inicio de la lista sin sin poner el 0
print(nombres[ :3])
#desde el indice seleccionado hast ael final
print(nombres[1: ])
#modificamos un valor
nombres[3] = 'Nahuel'
nombres[0] = 'Jorch'
print(nombres)

#iterar una lista

for nombre in nombres : #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#con la funcion LEN mostramos cuantos elementos tiene la lista
print(len(nombres)) #pasamos como parametros la lista llamad anbombres

#AGREGAR ELEMENTOS A UNA LISTA
#el elemento se agrega al final tiene como nombre el modo COLA o FILA
#UNA LISTA PUEDE TENER DIFERENTES TIPOS DE DATOS

nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,7])
nombres.append(7)
print(nombres)

#insertar un elemento en un indice especifico

nombres.insert(1,'Muricio')

nombres.insert(3,'Ancelmo')
print(nombres)

#ELIMINAR UN ELEMENTO DE UNA LISTA

nombres.remove('Ancelmo')#ponemos el nombre string de el elemento a eliminar
print(nombres)

#eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

#eliminar un elemento especifico de la lista
del nombres[2] #DEL significa delete (ELIMINAR)
print(nombres)

#ELIMINAR o LIMPIAR todos los elementos de la LISTA
nombres.clear()
print(nombres)

#ELIMINAR LA LISTA
del nombres
print(nombres)

#ejercicio 1 : Iterar un rango de 0 a 10 e imprimir Numeros divisibles entre 3
#ejemplo de ejecucion: 0,3,6,9

print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

#EJERCICIO 2Crear un rango de numeros de 2 a 6 e imprimirlos
#ejemplo de ejecucion 2,3,4,5,6
print('Rango con valor de inicio 2 y fin 6')
rango = range(2,7)
for i in rango:
    print(i)
#EJERCICIO 3 Crear un rango de 3 a 10 pero con incremento de 2 en 2 en lugar de 1 en 1
#ejemplo de ejecucucion 3,5,7,9

print('Rango con valores de inicio = 3, fin = 10 = 2')
for i in range(3, 11, 2):#va desde el 3 hasta la ultima posicion en 2 en dos
    print(i)

#TUPLAS
#LAS TUPLAS SON COMO LAS LISTAR PERO NO SE PUEDEN Modificar (constante)
cocina = ('Cuchara','Cuchillo','Tenedor')
print(cocina)
print(len(cocina))#como en las listas podemos saber el largo.

#las funciones de tuplas son similares a las listar

#como acceder a un elemento, para eso utilizamos corchetes no parentesis
print(cocina[1])
print(cocina[-1])#para ver el ultimo

#como acceder a un rango
print(cocina[0:2])

verduras = ('papa',)#una tupla necesita aunque sea una coma(elemento), deotra manera es una variable string


#como Recorrer elementos d ela tupla
for cocinar in cocina:#print esta usando \n para saltos de lineas
    print(cocinar, end=' ')#con end= ' ' ponemos algo al final de cada objeto

#cocina [0] = 'Plato'
#print(cocina)

#NO RECOMENDABLE
#la unica forma de modificar una tupla es pasarla a lista, modificarla y volverla a pasar a tupla
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n',cocina)#\n Salto de  linea

#si nuestro programa necesita una lista modificable usaremos una lista, si no se va a modificar usamos una tupla

#como eliminar una tupla
#del cocina
print(cocina)


#TIPO SET es mutable y tambien inmutable y se imprime de una manera aleatoria
planetas = {'Marte', 'Júpiter','Venus'}
print(len(planetas))#con len (length que significa largo)

#revisar si un elemento existe dentro de set
print('Jupiter' in planetas)

#Agregar un elemento

planetas.add('Tierra') #add es una funcion para agregar un elemento
print(planetas)#no se pueden duplicar datos

#eliminar elementos de un set(si no existe el elemento va a largar un error)
planetas.remove('Tierra')#esta funcion si tira error si no existe
print(planetas)

planetas.discard('tierra')#esta funcion no nos tira error

#LIMPIAR EL SETT
planetas.clear()
print(planetas)

#eliminar un set o conjunto
del (planetas)
print(planetas)


#DCICCIONARIO EN PYTHON(coeccion de datos)
#el diccionario esta compuesto por dos elementos
#ejemplo: 'Maradona':10
#dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#Verificamos cantidad de elementos
print(len(diccionario))
print(diccionario)
#Acceder a ujn Diciconario con la Llave KEY
print(diccionario['IDE'])#la key va entre llaves

#otra forma de recuperar un elemento
print(diccionario.get('POO'))#.get significa obtener
print(diccionario.get('SABD'))

#modificar los elementos
#entre llaves llamamos al key y los modificamos despues de =
diccionario['IDE'] = 'Entorno de Desarollo Integrado'
print(diccionario['IDE'])


#Como recorrer los elementos

for termino in diccionario:#Recorremos solo mostrando las llaves
    print(termino)

#necesitamos una fuincion para recorrer un DICCIONARIO(.ITEMS)
for termino,valor in diccionario.items():
    print(termino,valor)

#OTRA FORMA DE acceder a u diccionario
for termino in diccionario.keys():
    print(termino)#solo muestra las llaves

for valor in diccionario.values():#con value solo muestra los valores
    print(valor)

#comprobar la existencia de algun elemento(TRUE FALSE)

print('IDE' in diccionario)

#agregar un elemento
diccionario['PK'] = 'Primary Key'#si la key es la misma sobreescribe
print(diccionario)

#Como eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#vaciar un diccionario
diccionario.clear()
print(diccionario)

#como eliminar un diccionario
del diccionario #el diccionario se borra
print(diccionario) #nos va a tirar un error por que el diccionario no existe


#CONCATENAMOS LISTAS
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2
print(lista3)

#funccion extend sirve para agregar varios elementos

lista3.extend([7,8,9,1])
print(lista3)

#funcion index que sirve para ubicar en que indice esta el valor ingresado
print(lista3.index(5))
#print(lista3.index(0)) nos va a tirrar error

#como saber si cuantos valores repetidos tenemos en la lista
print(lista3.count(1))

#como poner al revez una lsita

lista3.reverse()
print(lista3)


#para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#MEtodos de ordenamiento, en python es una funcion
lista3.sort() #ordena los elementos de forma ascendentemente

lista3.sort(reverse = True)
print(lista3)#para ordenarlo de forma descendentemente
"""
tupla = (3, 'Michi', 5.12, [1, 5, 67], 5, 5, 'Hola')  # la tupla tambien puede tener difernetes tipos de datos dentro
print(tupla)
print(5 in tupla)  # nos devuelve un booleano (TRUE O FALSE)

# REPASO DE SET O CONJUNTO
# PARA DEFINIR UN CONJUNTO
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)  # Le preguntamos si el numero 3 NO ESTA EN EL CONJUNTO 1

# COMO HACER IGUALDAD DE DOS CONJUNTOS
print(conjunto1 == conjunto2)  # nos devuelve un valor booleano

# OPERACIONES EN CUNTUNTOS
# UNIONES DE CONJUNTOS

conjunto3 = conjunto1 | conjunto2
print(conjunto3)  # si los elementos del conjunto son iguales se superponen y se carga aleatoriamente los datos

# intercepcion
# nos demuestra si tienen algun elemento en comun
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #muestra elementos que estan en conj 1 y conj 2 excepto los que no estan compartidos
print(conjunto3)#elementos que no comparten y son diferente entre ambos

#como determinar si un conjunto es sub conjunto de otro

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))#con .issubset nos muestra con un booleano si esta dentro de otro conjuinto
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))


#como saber si no compartes algo en comun
print(conjunto3.issuperset(conjunto1))#preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))#si es verdadero quiere decir que el conjunto 3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun

print(conjunto1.isdisjoint(conjunto2))#preguntamos si hay cosas en comun en ambos conjuntos


#convertumos un conjunto totalmente inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totamente inmutable
#no se puede agregar, modificar ni eliminar elementos del conjunto


#repaso Diccionarios
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo':'Red', 'Verde':'Green', 'Amarillo':'Yelow'}

print(diccionarioNuevo)
#como eliminar un elemento
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#los didcionarios pueden almacenar diferentes tipos de datos

diccionario2 = {'Jonathan': {'Edad':40, 'Altura':1.83},'Emanuel': [45, 1.90], 'Patricia' : [35, 1.69]}
print(diccionario2)

seleccionArgentina = {
    10 : {'Nombre': 'Leonel Messi', 'Edad': 35, 'Altura': 1.70,'Precio' : '50 Millones', 'Posicion': 'Extremo Derecho'},
    11 : {'Nombre': 'Angel di Maria', 'Edad': 34, 'Altura': 1.80,'Precio' : '12 Millones', 'Posicion': 'Extremo Derecho'},
    21 : {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77,'Precio' : '35 Millones', 'Posicion': 'Media Punta'},
    19 : {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83,'Precio' : '3.5 Millones', 'Posicion': 'Defensa Central'},
    1 : {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89,'Precio' : '3.5 Millones', 'Posicion': 'Portero'},
    #agregar 4 jugadores mas
    9 : {'Nombre': 'Julian Alvarez', 'Edad': 23, 'Altura': 1.70,'Precio' : '30 Millones', 'Posicion': 'Delantero'},
    23 : {'Nombre': 'Emiliano Martinez', 'Edad': 31, 'Altura': 1.95,'Precio' : '10 Millones', 'Posicion': 'Portero'},
    7 : {'Nombre': 'Rodrigo De Poul', 'Edad': 29, 'Altura': 1.77,'Precio' : '26 Millones', 'Posicion': 'Centro Campista'},
    20 : {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.74,'Precio' : '17 Millones', 'Posicion': 'Mediocampista'},
}

for llave, valor in seleccionArgentina.items():
    print(llave,valor)

    print('Tenemos cargado en el diccionario la cantidad  de jugadores: ', end=' ')
    print( len(seleccionArgentina))
    print('')
    print('PILAS')
    #METODO PILAS
    #PILAS USANDO LISTAS
    pila = [1, 2, 3]
    #en pilas se trabaja siempre con el ultimo elemento
    #siempre se agregan elementos por el final

    pila.append(4)
    pila.append(5)
    print(pila)

    #como cacar un elemento desde el final de la pila
    #este metodo Saca y Retorna
    #pila.pop()
    #print(pila)#quitaria el numero "5"
    elementoBorrado = pila.pop()#el ultimo elemento borrado "5" se guarda en una variable
    print(f'Sacamos el elemento {elementoBorrado} de nuestra pila')
    print(f'La nueva pila  ahora quedo asi: {pila}')

    #colas con LISTAS
    #similar a una cola del banco
    #estructuras de datos de tipo FIJO (first input / first output) "primero en entrar y primero en salir"
    print('')
    print('COLAS')
    cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

    #agregar elementos al final de la cola
    cola.append('Natalia')
    cola.append('Jose')
    print(cola)
    #como sacar elementos d ela cola
    seRetira = cola.pop(0)#como un array se cuenta desde 0 en adelante
    print(f'Atendido el cliente: {seRetira}')
    print(f'Por atender: {cola}')
    seRetira = cola.pop(0)#como un array se cuenta desde 0 en adelante
    print(f'Atendido el cliente: {seRetira}')
    print(f'Por atender: {cola}')
    seRetira = cola.pop(0)#como un array se cuenta desde 0 en adelante
    print(f'Atendido el cliente: {seRetira}')
    print(f'Por atender: {cola}')
    seRetira = cola.pop(0)#como un array se cuenta desde 0 en adelante
    print(f'Atendido el cliente: {seRetira}')
    print(f'Por atender: {cola}')
    seRetira = cola.pop(0)#como un array se cuenta desde 0 en adelante
    print(f'Atendido el cliente: {seRetira}')
    print(f'Por atender: {cola}')

#4.5 RECORREMOS EL DICCIONARIO DE LA SELECCION ARGENTINA
for i in seleccionArgentina:
   print(f'{i} -> {seleccionArgentina [i]}')

