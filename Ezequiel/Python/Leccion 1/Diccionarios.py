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