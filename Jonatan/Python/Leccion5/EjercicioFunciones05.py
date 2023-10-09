#Ejercicio05: Convertidos de Temperaturas
#realizar dos funciones para convertir grados celsius
#a fahrenheit y viseversa
#investigar las formulas

#funcion que convierte de celsius a fahrenheit

def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 #la presedencia: es multiplicacion, divicion y suma

#funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return  (fahrenheit - 32)* 5 / 9 #respeta la presedencia utilizando los parentesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')#el poner :.2f luego de la variable resultado es liminar el decimal a 2 "32.00"

fahrenheit = float(input('Digite el valor de Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')