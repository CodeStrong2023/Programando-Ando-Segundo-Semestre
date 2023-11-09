edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'A mitad del camino'
elif 40 <= edad < 60:
    mensaje = 'La vida continua, aprovecha a hacer todo lo que sueñas'
elif 60 <= edad < 80:
    mensaje = 'Tiempo de abuelos'
elif 80 <= edad < 100:
    mensaje = 'Increible aguante viejo!'
else:
    mensaje = 'Error, etapa de vida no reconocida'
print(f'Tu edad es: {edad}, {mensaje}')
