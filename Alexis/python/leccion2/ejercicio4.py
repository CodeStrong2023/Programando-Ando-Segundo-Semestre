# ejercicio etapas de la vida segun la edad
edad = int(input("digite su edad: "))
mensaje = None
if 0 <= edad < 10: #sintaxis simplificada
    mensaje = "la infancia es increible y bella"
elif 10 <= edad < 20:
    mensaje = "tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "amor y comienza el trabajo"
else:
    mensaje = "error, etapa de vida no reconocida"
print(f"tu edad es: {edad}, {mensaje}")












