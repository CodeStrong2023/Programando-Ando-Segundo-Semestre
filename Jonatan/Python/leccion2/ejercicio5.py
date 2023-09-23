#ejercicio 5: Sistema de Calificaciones

calificacion = int(input("Ingrese una calificación del 1 al 10: "))# Pedir al usuario una calificación del 1 al 10

# Mostrar el equivalente en pantalla según el número ingresado
if calificacion >= 9 and calificacion <= 10:
    calificacion = 'A'
elif calificacion >= 8 and calificacion < 9:
    calificacion = 'B'
elif calificacion >= 7 and calificacion < 8:
    calificacion = 'C'
elif calificacion >= 6 and calificacion < 7:
    calificacion = 'D'
elif calificacion >= 1 and calificacion < 6:
    calificacion = 'F'
else:
    print("Error: La calificación debe estar en el rango del 1 al 10")

print(f'Su Calificacion equivale a una: {calificacion}')