# Ejercicio 5: Convertidor de temperaturas, de F a C y viceversa

def convertir_temperatura():
    opcion = input("¿Qué conversión deseas hacer? \n 1. Fahrenheit a Celsius \n 2. Celsius a Fahrenheit \n")
    if opcion == "1":
        fahrenheit = float(input("Introduce los grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    elif opcion == "2":
        celsius = float(input("Introduce los grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    else:
        print("Opción no válida.")

convertir_temperatura()
