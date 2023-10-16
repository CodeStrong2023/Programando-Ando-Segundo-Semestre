# ejercicio 5: convertidor de temperaturas
# realizar dos funciones para converir de grados celcius
# a fahrenheit y viseversa

# funcion que convierte de celcius a fahrenheit
def celcius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32 # la presedencia: multiplicacion y una suma

# funcion que convierte de fahrenheit a celcius
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # respetar la presedencia utilizando parentesis

celcius = float(input("digite el valor de celcius: "))
resultado = celcius_fahrenheit(celcius)
print(f"{celcius} C a F -> {resultado:.2f}")

fahrenheit = float(input("digite el valor de fahrenheit: "))
resultado = fahrenheit_celcius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2f}")

