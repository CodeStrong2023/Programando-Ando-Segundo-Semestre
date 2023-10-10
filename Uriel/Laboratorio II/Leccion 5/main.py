#Comenzamos con funciones
#Definimos una funcion
'''
def mi_funcion():
    print('Saludos a todos los alumnos de la Tecnicatura')
mi_funcion()
mi_funcion()
mi_funcion()
#Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Uriel", "Pardo"]
show(person[0], person[1])#Pasamos uno por uno los datos de la lista o funcion
show(*person) #Esto es lo mismo que lo anterior pero mostramos todo junto
person2 = ("Gaston", "Castro") #Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)


numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
else:# Siempre se ejecuta el else, la unica manera es con break antes del mismo else
    print('Esto se termino')
#List cohompresion, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)


bottleC = [{"name": "Quilmes", "country": "Argentina"},
           {"name": "Corona", "country": "Mexico"},
           {"name": "Stella Artois", "country" : "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Argentina"]
print(Arg)
print(bottleC)

#Paso de argumentos(funciones)
def mi_funcion2(name, lastName):
     print(f'Nombre: {name}, Apellido: {lastName}')

mi_funcion2("Uriel", "Pardo")

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a+b
resultado = sumar(78, 28)
print(f'El resultado de la suma es {resultado}')
print(f'El resultado de la suma es {sumar(55, 45)}')

def sumar2(a = 0, b = 0):
    return a+b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 45)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #Pro lo general se utiliza la variable *args
     for nombre in nombres: #Se convierten en tuplas por lo que no pueden ser modificados
         print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")


def listarTerminos(**terminos): #Lo mas utilizado es  **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa key word arguments
        print(f'{llave}: {valor}')

listarTerminos() #No recibe nada, no se va  amostrar nada
listarTerminos(IDE= 'Integrated Developement Enviroment', PK = 'Primary Key')
listarTerminos(Nombre= 'Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10) #NO es un objeto iterable
desplegarNombres((10, 11)) #Lo convertimos a una tupla
desplegarNombres([22, 55]) #Lo convertimos en una lista
'''
#Funciones recursivas
def factorial(numero):
    if numero == 1:#Caso base
        return 1
    else:
        return numero * factorial(numero-1)

numero = int(input('Digite el numero a calcular el factorial\n'))
print(f'El factorial de {numero} es:\n{factorial(numero)}')
