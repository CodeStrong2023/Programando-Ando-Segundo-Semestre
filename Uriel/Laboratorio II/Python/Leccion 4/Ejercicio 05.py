#Ejercicio 05: Calcular el factorial de un numero positivo
numero = int(input('Digite un numero positivo\n'))
factorial = 1
while  numero < 0:
    print("Error. EL numero debe ser positivo")
    numero = int(input("Digite un numero positivo\n"))
for i in range(1, numero+1):
    factorial*= i
print(f'El factorial del numero {numero} es: {factorial}')