#Ejercicio 5 calcular Factorial
num = int(input("Ingrese un número entero no negativo: ")) # pedimos un numero mayor o igual a 0

if num >= 0: #con el if comprobamos que el numero sea correcto
    i = 1#si es correcto iniciamos i y factorial en 1
    factorial = 1
    while i <= num:#ciclo while para calcular el factorial
        factorial *= i
        i += 1
    print(f'El factorial de {num} es: {factorial}')#mostramos al usuario el resultado
else:
    print('No se puede calcular el factorial')