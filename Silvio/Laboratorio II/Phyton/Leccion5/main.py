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
