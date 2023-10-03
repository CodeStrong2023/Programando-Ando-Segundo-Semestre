#COMENZAMOS CON FUNCIONES

#DEFINIMOS UNA FUNCION

#mi_funcion()#no se puede llamar antes de definir la funcion
#el compilador viene de arriba hacia abajo

def mi_funcion():#nomenclatura Snake case
    print('Saludos para todos los que ven nuestro Trabajo')
    print('Respetando Identacion')
    #mientras se respete la identacion sigue siendo de la funcion

#en el instante que quitamos la tabulacion estamos fuera de la funcion

mi_funcion()#ahora llamamos a la funcion

mi_funcion()
mi_funcion()#podemos llamar "N" veces a la funcion


#DESEMPAQUETADO DE LISTAS O LIST UNPACKING

def show(name, lastName):#iniciamos la funcion (SHOW significa que va a mostrar
    print(name+ ' '+lastName)
person = ["Ariel", "Bentancud"]#se puede hacer en una lista
show(person[0],person[1])#mostrando por partes
show(*person)#o mostrando todo junto
person2 = ("Osvaldo","Giordanini")#se pueden hacer en una tupla
show(*person2)#mostrando todo junto
person3 = {"lastName": "Lucero", "name": "Natalia"}#y tambien se pueden hacer en diccionarios
show(**person3)#esta vez al tener una "CLAVE" y un "VALOR" debemos poner 2 ** para mostrar ambos valores


#cosa rara de PYTHON
#EL FOR ELSE
#el Else siempre se Ejecuta aunque no tengamos un IF
#la unica manera de que no se ejecute es ponerle un  break
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break#esta es la unicam manera de que no se ejecute el else
else:
    print('Esto se termino')



#LIST COMPREHENSION, lista de comprension
print('#LIST COMPREHENSION, lista de comprension')
names = ["Paola","Simba","Nuba","Paquito"]
alongP = [p for p in names if p[0] == 'P']
print(alongP)

bottleC = [{"Name":"Quilmes","country": "Arg"},
           {"Name": "Corona","country": "Mx"},
           {"Name": "Stella Artois","country":"Belgium"},]
Arg = [b for b in bottleC if b["country"] == "Arg"]#solo extraemos si en el valor "Country" esta el caracter "ARG"
print(Arg)
print(bottleC)

#6.6 FUNCIONES: PASO DE ARGUMENTOS
def mi_funcion2(name, lastName):#entre parentecis despues de la funciojn van los PARAMETROS
    print("Saludos a todos")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Manuel','Granados')#declaramos los argumentos
mi_funcion2('Analia','Parchiz')
mi_funcion2('Antonio','Banderas')
"""
Parámetro es el nombre que recibe una de las variables que aparecen en la declaración de la función.
Argumento es el nombre que recibe uno de los valores que es suministrado a la función cuando es invocada.
Parametro: nombre de la variable
Argumento: valor de la variable
"""
#6.7  LA PALABRA RETURN en FUNCIONES
#CREAMOS UNA FUNCION PARA SUMAR
def sumar(a,b):
    return a + b
#resultado = sumar(78 , 22)
#print (f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

#6.8 Funciones: Valores por Default en Argumentos
def sumar2(a = 0,b = 0): # le damos un valor por default,
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')#aca modificamos el valor por default

#6.9 Funciones: argumentos, variables en funciones

def listarNombres(*nombres):#si no sabemos cuantos datos va a recibir el parametro normalmente se utiliza *ars
    for nombre in nombres:#se va a convertir en una tupla
        print(nombre)
listarNombres('Antonio','MArcelo','Claudia','Lucas')#ponemos los argumentos fuera de la funcion
listarNombres('Manuel','Arturo','Pablito','Martin')
