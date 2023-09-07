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
