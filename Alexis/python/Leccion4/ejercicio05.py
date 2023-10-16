# ejercicio 5: factorial de un numero positivo
# hacer un programa para calcular el factorial de un numero positivo
numero = int(input("digite un numero: "))
while numero < 0: # mientras el numero sea negativo
    print("error -> el numero tiene que ser negativo")
    numero = int(input("digite un numero: "))
factorial = 0 # la variable para clacular el factorial
for i in range(1, numero+1):
    factorial *= 1
print(f"\nel factorial del numero {numero} positivo ingresado es: {factorial}")

