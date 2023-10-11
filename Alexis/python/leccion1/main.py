'''
miVariable = 3
print(miVariable)
miVariable = "hola"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# las literales se escriben x680, la variable y = x752 y la variable z = x072
print(id(y))
print(id(z))

# tipos Int, Float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "hola mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# manejo de cadenas (string)
miGrupoFavorito = "Rata Blanca"
caracteristicas = "the best band rock"
print("mi grupo favorito es ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# tipos booleano
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("el resultado es verdadero")
else:
    print("le resultado es falso")

# procesar la entrada del usuario
# funcion input
resultado = input("digite un numero: ") # regresa un dato tipo sting
print(resultado)

# consersacion de la entrada de datos
numero1 = int(input("escribe el primer numero: "))
numero2 = int(input("escribe el segundo numero: "))
resultado = numero2 + numero1
print("el resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoB + operandoA
#print("resultado de la suma: ",suma)
print(f'el resultado de la suma es: {suma}')
resta = operandoA - operandoB
print(f'el resultado de la resta es: {resta}')
multiplicacion = operandoB * operandoA
print(f'el resultado de la multiplicacion es: {multiplicacion}')
division = operandoA / operandoB
print(f'el resultado de la division es: {division}')
division = operandoA // operandoB
print(f'el resultado de la division(int) es: {division}')
modulo = operandoA % operandoB
print(f"el resultado de la division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"el resultado del exponente es: {exponente}")
"""
"""
alto = int(input("proporcione el alto del rectangulo: "))
ancho = int(input("proporcione el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("area: ", area)
print("perimetro: ", perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)

#operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable = miVariable - 2
miVariable3 -= 2

# miVariable = miVariable * 3
miVariable3 *= 3
print(miVariable3)

# miVariable = miVariable / 2
miVariable3 /= 2
print(miVariable3)

# operadores de comparacion

d = 4
b = 2
resultado = b == d # comprobamos sin son iguales
print(resultado)

# operador diferente
resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

# operador menor que
resultado = d < b
print(resultado)

# operador menor o igual que
resultado = d <= b

# operador mayor o igual que
resultado = d >= b
"""
"""
a = int(input("digite un numero: "))
print(f"el residuo de la division es:  {a % 2}")
if a % 2 == 0:
    print(f"el valor de a es: {a} es un numero PAR")
else:
    print(f"el valor de a es: {a} es un numero IMPAR")
"""
"""
edadAdulto = 18
edadPersona = int(input("digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"su edad es: {edadPersona} años, usted es menor de edad")
"""
"""
# operadores logicos

a = True
b = False
resultado = a and b
print(resultado)

# operador or
resultado = a or b
print(resultado)

#operador not
resultado = not a
print(resultado)
"""
"""
#ejecicio: valor dentro de un rango
valor = int(input("digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"el valor {valor} esta dentro del rango")
else:
    print(f"el valor {valor} no esta dentro del rango")
"""
"""
# ejercicio con el operador or
vacaciones = False
diaDescanzo = False
if vacaciones or diaDescanzo:
    print("tiene trabajo que hacer")
else:
    print("puede asistir al juego")
"""
"""
# ejercicio: rango entre 20 y 30 años
edad = int(input("digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# rinttreinta
# if veinte or treinta
if (20 <= edad < 30) or (30 <= edad < 40): # sintaxis simplificada del operador and
    print("estas dentro del rango de los (20'0) a (30'0) años")
#    if veinte:
#       print("estas dentro del rango de los (20\'0) años")
#    elif treinta:
#        print("estas dentro del rango de los (30\'0) años")
#    else:
#        print("no estas dentro del rango")
else:
    print(" no estas dentro del rango de los (20'0) a (30'0) años")
"""
"""
# ejercicio: el mayor de dos numeros
numero1 = int(input("dijite el valor para el numero 1. "))
numero2 = int(input("dijite el valor para el numero 2: "))
if numero1 > numero2:
    print("el numero 1 es mayor: ")
else:
    print("el numero 2 es mayor")
"""
"""
# ejercicio: tienda de libros
print("dijite los siguiente datos del libros")
nombre = input("dijite el nombre del libro: ")
id = int(input("dijite el ID del libro: "))
precio = float(input("dijite el precio del libro: "))
envioGratiuto = input("indicar si el envio es gratuito (True/False): ")
if envioGratiuto == "True":
    envioGratiuto = True
elif envioGratiuto == "False":
    envioGratiuto = False
else:
    envioGratiuto = "el valor es incorrecto, debe escribir"
print(f'''
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envio Gratuito: {envioGratiuto}
''')
"""
