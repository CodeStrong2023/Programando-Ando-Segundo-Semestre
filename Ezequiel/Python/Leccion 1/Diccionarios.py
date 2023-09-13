#coleccion de datos organizada de una manera muy particular

#'Maradona':10 Un diccionario esta compuesto por dos elements
#UNA LLAVE Y UN VALOR
#dict(key,value)

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'POO' : 'Programacion Orintada a Objetos'
}
print(diccionario)
#verificar la cantidad de elementos del diccionario
print(len(diccionario))

#acceder a una diccionario con la key
print(diccionario['IDE'])

#otra forma de recuperar un elemtneo
print(diccionario.get('POO'))

#modificaion de los elementos del diccionario
diccionario['IDE'] = ' Entorno de Desarrollo Integrado'
print(diccionario)

#recorrer elementos del diccionario
#solo mmostrando la llave
for termino in diccionario:
    print(termino)

#para recorrer la llave y el valor, debemos usar una funcion item()
for termino, valor in diccionario.items():
    print(termino,valor)

#accediendo usando la funcion keys() que nos da las llaves
for termino in diccionario.keys():
    print(termino)

#accediendo usando la funcion values() que nos da los valores
for valor in diccionario.values():
    print(valor)

#comprobar la existencia de algun elemtneo devuelve un bool
print('IDE' in diccionario)

#agregar un elemtno
diccionario['PK'] = 'Primary key'

#eliminar un elemento
diccionario.pop('POO')
print(diccionario)

#vaciar un diccionario
diccionario.clear()


##REPASO DE DICCIONARIO
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)

seleccionArgentina = {
    10: {'Nombre' : 'Lionel Messi', 'Edad' : 35, "Altura" : 1.70, "Precio" : '50 Millones', 'Posicion' : 'Extremo Derecho'},
11: {'Nombre' : 'Angel Di Maria', 'Edad' : 34, "Altura" : 1.80, "Precio" : '12 Millones', 'Posicion' : 'Extremo Derecho'},
24: {'Nombre' : 'Paulo Dybala', 'Edad' : 28, "Altura" : 1.77, "Precio" : '35 Millones', 'Posicion' : 'Media Punta'},
19: {'Nombre' : 'Nicolas Otamendi', 'Edad' : 34, "Altura" : 1.83, "Precio" : '3.5 Millones', 'Posicion' : 'Defensa Central'},
}

print(seleccionArgentina.values())

#recorrer el arreglo
for valor in seleccionArgentina:
    print(valor)

##recorrer la llave y el valor
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

##TAREA AGREGAR 4 JUGADORES MAS A LA SELECCIONARGENTINA

# Jugadores a agregar
jugadores_nuevos = {
    7: {'Nombre': 'Gonzalo Higuain', 'Edad': 34, 'Altura': 1.85, 'Precio': '15 Millones', 'Posicion': 'Delantero'},
    8: {'Nombre': 'Ezequiel Garay', 'Edad': 35, 'Altura': 1.88, 'Precio': '5 Millones', 'Posicion': 'Defensa Central'},
    9: {'Nombre': 'Leandro Paredes', 'Edad': 27, 'Altura': 1.82, 'Precio': '25 Millones', 'Posicion': 'Centrocampista'},
    21: {'Nombre': 'Lucas Ocampos', 'Edad': 27, 'Altura': 1.78, 'Precio': '20 Millones', 'Posicion': 'Extremo Izquierdo'}
}

# Agregar los jugadores nuevos al diccionario utilizando el método update
seleccionArgentina.update(jugadores_nuevos)

print(seleccionArgentina)

# Seguimos mostrando como recorrer un diccionario con el ciclo for

for i in seleccionArgentina:
    print(f'{i} => {seleccionArgentina}')
