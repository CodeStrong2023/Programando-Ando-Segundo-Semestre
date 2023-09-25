suma = 0
calificacion_baja = 99999

for i in range(10):
    calificacion = int(input('Ingrese la calificaciones de los 10 alumnos: '))
    suma = suma + calificacion
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

calificacion_promedio = suma / 10
print('')
print(f'La calificacion Promedio es: {calificacion_promedio}')
print('')
print(f'La calificacion mas baja es: {calificacion_baja}')