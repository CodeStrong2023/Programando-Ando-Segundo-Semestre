#Comenzamos con Funciones

# Definimos una funcion
def mi_funcion():
    print('Saludos alumnos de la Tecnicatura')

mi_funcion()
mi_funcion()

# Desempaquetado de lista o List Unpacking
def show(name, lastName):
    print(name+ lastName)

person = ["Ezequiel", "Lorenz"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person) # es lo mismo que lo anterior pero le pasamos todo junto

person2 = ["Ariel", "Betancud"]
show(*person2)
person3 = {"lastName" : "Lucero", "name" : "Natalia"}
show(**person3)

## Repaso de ciclo for

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break ## esto hace que no se ejecute el siguiente else
else:
    print('Esto se termino')

## List Comprehension, lista de compresion

names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P']
print(alongP)

bottleC = [ {'name': "Quilmes", "country": "Arg"},
            {'name': "Corona", "country": "Mx"},
            {'name': "Stella Artois", "country": "Belgium"}
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

## Paso de argumentos

def mi_funcion2(name, lastName):
    print('Saludo a todos los profes de la tecnicatura')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Natalia', 'Lucero')

## palabra return en funciones

def sumar(a,b):
    return a + b

resultado = sumar(78 + 22)
# print(f'El resultado  de la suma es: {resultado}')
print(f'El resultado  de la suma es: {sumar(78 + 22)}')

## Valores por default en argumentos

def sumar2(a =0, b = 0):
    return a+b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22,66)}')


## argumentos, variables en funciones

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres('Lucas','Jose','Claudia','Rosa','Maria')
listarNombres('Marcos','Daniel','Romina','Pepe','Marcela','Carlos')