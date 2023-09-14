"""
#Clase 2
miVariable = 3
print(miVariable)
miVariable = "Hola a todos"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
print(id(y))
print(id(z))

#Clase 3
# Tipos de datos INT, FLOAT, STrING  y BOOLEAN

x = 10
print(x)
print(type(x))
x = 20.6
print(x)
print(type(x))
x = "Hola mundo mundial"
print(x)
print(type(x))
x = False  # True y False siempre se empiezan con Mayuscula
print(x)
print(type(x))

# Manejo de cadenas

miGrupoFavorito = "Linkin Park "
caracteristicas = "la mejor banda del mundo"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"

print(int(numero1) + int(
    numero2))  # convertimos el dato String de num1 y 2 y los pasamos a Enteros con la funcion int entre ()

# Tipos Booleanos (bool) Verdadero y Falso

miBooleano = 3 < 2
print(miBooleano)

if miBooleano:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

# Procesar la entrada del usuario

# la funcion input

#  resultado = input("Ingrese un dato: ")  # Regresa un dato tipo String
# print("El resultado es: ", resultado )

# convercion de la entrada de datos

#numero1 = int(input("Ecribe el primer numero: "))
#numero2 = int(input("Escribe el segundo numero: "))
#resultado = numero1 + numero2

#print("El resultado de la suma es: ", resultado)

Ejercicio 1: Califica tu día
¿Cómo estuvo tu día (1 al 10)?
Mi día estuvo de: 10
Hacer el código
Debes hacerlo en PyCharm y también en el celular y en la terminal de Python...

dia = int(input("Como estuvo tu dia? (1 al 10) :"))
print("Mi dia estuvo de ", dia)
print("")
Ejercicio 2:

Se solicita incluir la siguiente información acerca de un libro:
título
autor
Debes imprimir la información en el siguiente formato:
Proporciona el título:
Proporciona el autor:
<título> fue escrito por <autor>

titulo = input("Ingrese el Titulo del libro: ")
autor = input("ingrese el autor del libro: ")

print(titulo, "fue escrito por", autor)"""
"""
"Clase 4 OPERADORES "
"Operadores aritmeticos"
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma es:" , suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"EL resultado de la multiplicacion es : {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA //operandoB
print(f"El resultado de la division es (int): {division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

#Ejercicio Rectangulo

alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print ('Area: ' , area)
print('Perimetro: ', perimetro)

#operadores de asignacion y comparacion

miVariable3 = 10
print(miVariable3)
#operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
#operadores de reasignacion(incremento con reasignacion)
miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3/= 2
print(miVariable3)

#operadores aritmeticos sobre Cadenas
#operador de Comparacion parte 2

d = 4
b = 6
resultado = d == b #comprobamos si son iguales
print(resultado)

#operador diferente
resultado = d != b
print(resultado)

#operador mayor que
resultado = d > b
print(resultado)

#operador menor que
resultado = d < b
print(resultado)

#operador menor o igual que
resultado = d <= b
print(resultado)

#operador mayor o igual que
resultado = d >= b
print(resultado)

#ejercicio 1 y 2
a = int(input("digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero IMPAR")

#ejercicio: DEterminar si es MAyor de edaad

edadAdulto = 18
edadPersona = int(input('Digite su edad: '))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")

#Clase 5
#operadores parte 2
#Operadores Logicos
a = True
b = False
resultado = a and b
print(resultado)

#operador or
resultado = a or b
print(resultado)

#operador not
resultado = not a
print(resultado)

#ejercicio valor de un rango
valor = int(input("Digite un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor{valor} NO esta dentro del rango")
    
#operador or y not
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print("Puede asistir al partido")
else:
    print("Tiene trabajo que hacer")


#ejercicio rango entre 20 y 30 anios
edad = int(input("Digite su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad <40
#print(treinta)

#sintaxis simplificada del operador and
#if veinte or treinta:
if (20 <=edad <30) or (30 <= edad < 40):
    print('Estas dentro del rango de los(20\'0) anios')
#    if veinte:
#        print('Estas dentro del rango de los(20\'0) anios')
#    elif treinta:
#        print('Estas dentro del rango de los(30\'0) anios')
#    else:
#        print('No estas dentro del rango')
else:
    print('No estas dentro del rango de los (20\'0) a (30\'0) anios')

#Eejercicio Mayor de 2 numeros

numero1 = int(input("Digite el valor para el numero1: "))
numero2 = int(input("Digite el valor para el numero2: "))

if numero1 > numero2:
    print('El numero 1 es mayor.')
else:
    print('El numero 2 es mayor.')

#ejercicio general. TIENDA
print('Digite los siguientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar si el envio es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito =='False':
    envioGratuito = False
else:
    envioGratuito = 'El valor ingresado es incorrecto, debe escribir True/False'

print(f'''
         Nombre: {nombre}
         ID: {id}
         Precio: {precio}
         Envio Gratuito?: {envioGratuito}
''')
"""