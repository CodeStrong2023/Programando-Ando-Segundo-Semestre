#ejercicio numeros pares

# Pedir al usuario la cantidad de números a ingresar
n = int(input("Ingrese la cantidad de números a ingresar: "))

# Inicializar variables
numeros = []
suma_pares = 0
num_pares = 0
suma_impares = 0
num_impares = 0

# Pedir al usuario ingresar los números
for i in range(n):
    num = int(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(num)

    # Verificar si el número es par o impar y realizar los cálculos correspondientes
    if num % 2 == 0:
        suma_pares += num
        num_pares += 1
    else:
        suma_impares += num
        num_impares += 1

# Calcular promedio de los números impares
if num_impares > 0:
    promedio_impares = suma_impares / num_impares
else:
    promedio_impares = 0

# Mostrar resultados
print("Suma de los números pares:", suma_pares)
print("Cantidad de números pares:", num_pares)
print("Promedio de los números impares:", promedio_impares)
