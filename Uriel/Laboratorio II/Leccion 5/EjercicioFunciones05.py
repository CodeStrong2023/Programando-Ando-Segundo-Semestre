#Ejercicio 05: Convertidor de temperatura
#Realizar dos funciones para convertir de grados celcius a farenheit y viceversa
#Investigar las formulas
def convertir_a_Celcius(fahrenheit):
    return (fahrenheit - 32) *5 /9

def convertir_a_Fahrenheit(celsius):
    return celsius * 9 / 5 + 32

celsius = float(input('Digite la temperatura en celsius'))
print(f'{celsius}°C a F -> {convertir_a_Fahrenheit(celsius)} F')


fahrenheit = float(input('Digite la temperatura en fahrenheit'))
print(f'{fahrenheit} F a °C -> {convertir_a_Celcius(fahrenheit)}°C')