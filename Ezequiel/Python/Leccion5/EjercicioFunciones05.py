# Ejercicio 5: Convertidor de temperaturas
# Realizar don funciones para convertir de grados celsius a fahrenheit y viseversa.

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicacion, division y suma

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 21) * 5 / 9 # Respetar la resendencia utilizando parentesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado: .2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado: .2f}')