# mi_funcion() --> no se puede llamar a una funcion antes de declararla
def mi_funcion():
    print('Saludos!')

mi_funcion() # llamo a la funcion

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los daron de la lista a la funcion
show(*person) # Esto es la mismo que lo anterior pero le pasamos todo junto

person2 = ("Osvaldo", "Giordanini") # desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName":"Lucero", "name": "Natalia"} # Ahora con diccionarios
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
# para que no se ejecute el else deberia haber un condicional con accion de break
else:
    print('Esto se termina')

# List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Comparo el primer elemento del
# String (primer caracter) y si es = a P sumo a la lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Bel"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argunmentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a travez de Youtube")
    print(f'Nombre: {name}, Apeliido: {lastName}')
mi_funcion2('Jorge', 'El Travieso')

# La palabra return en funciones
def sumar(a, b):
    return a + b
resultado = sumar(4, 6)
print(resultado)

def sumar2(a = 0, b = 0): # Asigno valores por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')

# Argunmentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Sarabino')
listarNombres('Marcos', 'Edilsberto')

def listarTerminos(**kwargs): # Se puede utilizar otro nombre pero **kwargs es lo mas comun
    for llave, valor in kwargs.items(): # kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi')

# Paso como argumento (nombre) -> Argumentos fijos
# Paso como argumento (*args) -> Tupla
# Paso como argumento (**kwargs) -> Diccionario

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla') # Itera por Caracter
# desplegarNombres(10, 11) No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos en una tupla. Para un solo elemento poner "," ((10, ))
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo

numeroFactorial = int(input('Digite un numero para calcular el factorial: '))
resultado = factorial(numeroFactorial) # Lo hacemos en codigo duro
print(f'El factorial del numero {numeroFactorial} es: {resultado}')

