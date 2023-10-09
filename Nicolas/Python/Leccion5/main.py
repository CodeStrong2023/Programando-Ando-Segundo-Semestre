# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir una funcion
# Definimos una funcion
def mi_funcion():
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces


# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+""+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con el la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #  Esta es la unica manera para que no se ejecute el else
else: 
    print("Esto se termina")
    
    
# List comprension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)    

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona",  "country": "Mx"},
           {"name": "Stella Arcois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")    
mi_funcion2("Nicolas", "Sini")
mi_funcion2("Sabrina", "Gutierrez")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
#print(f" El resltado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")


def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)

listarNombres("Lucas", "Jose", "Rosa", "Claudia", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

        



