# Calcular el factorial de un numero positivo

numero = int(input('Digite un numero: '))
while numero < 0:
    print('ERROR --> El numero tiene que ser positivo')
    numero = int(input('Digite un numero: '))

factorial = 1

for i in range(1, numero+1):
    factorial *= i

print(f"\nEl factorial del numero {numero} es: {factorial}")
