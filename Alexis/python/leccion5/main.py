# comenamos con funiones
# mi_funcion() # mo se puede llamar ants de definir a una funcion
# definimos una funcion
def mi_funcion():
    print("saludos a todos los alumnos de la tecnicatura")

mi_funcion() # estamos llamando a la funcion
mi_funcion() # se puede llamar a una funcion N cantidad de veces

# desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["ariel", "betancut"]
show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la funcion
show(*person) # esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ("osvaldo", "giordanini") # desempaquetmos a traves de una tupla
show(*person2)
person3 = {"lastname": "lucero", "name": "natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # aun con la lista vacia se va a ejeccutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # esta es la unica manera para que no se ejecute el else
else:
    print("esto se termino")

# list comprehesion, lista de compresion
names = ["paolo", "rodrigo", "lupe", "pepe"]
alongP = [p for p in names if p[0] == "P"] # esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "quilmes", "country": "Arg"},
           {"name": "corona", "country": "mx"},
           {"name": "stella artois", "country": "belgium"},
           ]
arg = [b for b in bottleC if b["country"] == "Arg"]
print(arg)
print(bottleC)

# paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("saludos a todos lo que ven a traves del canal de youtube")
    print(f"nombre: {name}, apellido: {lastName}")
mi_funcion2("jorge","lucero")
mi_funcion2("ariel", "betancut")
mi_funcion2("analia", "pedrosa")

# la palabra return en funciones
# creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la duma es: {sumar(45, 55)}")

def sumar2(a = 0, b = 0): # le damos un valor por default
    return a + b
resultado = sumar2()
print(f"resultado de la suma: {resultado}")
print(f"resultado de la suma: {sumar2(22, 66)}")

# argumentos, variables e funciones
def listarNombres(*nombres): # normalmente se utiliza: *args
    for nombre in nombres: # se va a convertir en una tupla
        print(nombre)
listarNombres("lucas", "jose", "claudia", "rosa", "maria")
listarNombres("marcos", "daniel", "romina", "pepe", "marcela", "carlos")

def listarTerminos(**terminos): # lo mas utilizado es **kwars para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f"{llave} : {valor}")

listarTerminos() # no recibe nada, nada se va a mostrar
listarTerminos(IDE = "integrated develoment enviroment", PK = "primaruy key")
listarTerminos(nombre = "Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["tito", "pedro", "carlos"]
desplegarNombres(nombres2)
desplegarNombres("carla")
# desplegarNombres(10, 11) # no es un objeto iterable
desplegarNombres((10, 11)) # la convertimos en una tupla, enun solo elemento no olvidar la coma
desplegarNombres([22, 55]) #la convertimos en una lista

# funciones recursivas
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero-1) # caso recursivo

resultado = factorial(5) # lo hacemos en codigo duro
print(f"el factorial del numero 5 es: {resultado}") # tarea que el usuario ingrese el numero para calcular el factorial




