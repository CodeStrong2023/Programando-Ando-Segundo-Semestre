# año bisiesto
"""año = int(input("ingrese el año: "))
if (año / 4 == 0) and (año / 100 != 0) or (año / 400 == 0):
    print("el año no es bisiseto")
else:
    print("el año es bisiesto")"""


"""# calcular la suma de "N" primeros numeros
num = int(input("dijite la cantidad de numeros a sumarse: "))
suma = 0
for i in range(num):
    suma = suma + i
print("la suma es: ",suma)"""


"""# leer 10 numero e imprimir cuantos son prsitivos, negativos y neutros
positivos = 0
negativos = 0
neutros = 0
for i in range(10):
    num = int(input("digite un numero: "))
    if num == 0:
        neutros = neutros + 1
    elif num > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
print(f"el conteo de positivos es: ",positivos)
print(f"el conteo de negativos es: ",negativos)
print(f"el conteo de neutros es: ",neutros)"""


"""# calificaciones
suma = 0
calificacionBaja = 99999
for i in range(10):
    calificacion = int(input("dijite una calificacion: "))
    suma = suma + calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
promedio = suma / 10
print(f"la calificacion promedio es: ",promedio)
print(f"la calificacion mas baja es: ",calificacionBaja)"""


# ejercicio 6
i = 1
sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0
N = int(input("dijite la cantidad de elementos a ingresar: "))
while i <= N:
    num = int(input("dijite un numero: "))
    if num / 2 == 0:
        sumaPares = sumaPares + num
        conteoPares = conteoPares + 1
    else:
        sumaImpares = sumaImpares + num
        conteoImpares = conteoImpares + 1
    i = i + 1
if conteoPares == 0:
    print("no se han dijitado numeros pares")
else:
    print(f"la suma de los pares es: ",sumaPares)
    print(f"el conteo de los pares es: ",conteoPares)
if conteoImpares == 0:
    print("no se han dijitado numeros impares")
else:
    promedioImpares = sumaImpares / conteoImpares
    print(f"el promedio de impares es: ",promedioImpares)


# ejercicio 7
"""contador = 0
suma = 0
while contador < 5:
    horas = int(input("dijite las horas trabajadas: "))
    tarifa = int(input("dijite la tarifa por hora: "))
    salario = horas * tarifa
    print("el salario es: $",salario)
    suma = suma + salario
    contador += 1
print(f"el salario de todos los empleados es: $",suma)"""


