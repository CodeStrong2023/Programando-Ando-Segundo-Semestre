# Iniciamos los contadores en 0
positivos = 0
negativos = 0
neutros = 0

# Pedimos 10 numeros al usuario
for i in range(10):
    numero = int(input("Ingrese un número: "))

    # Determinar si es positivo, negativo o neutro
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# mostramos al usuario el resultado
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números neutros:", neutros)