numero1 = int(input("Digite el numero a: "))
numero2 = int(input("Digite el numero b: "))

if numero1 != numero2:
    if numero1 > numero2:
     print(f"El mayor es el numero a: {numero1}")
    else:
     print(f"El mayor es el numero b: {numero2}")
else:
    print("Son iguales!")