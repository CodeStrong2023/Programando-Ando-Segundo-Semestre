#EJERCICIO 4 ETAPAS DE LA VIDA
edad = int(input("Ingrese su edad 1 al 30: "))

if edad >= 0 and edad <= 10:
    print("La infancia es increible y bella")
elif edad >= 11 and edad <= 19:
    print("Tienes muchos cambios, mucho que estudiar")
elif edad >= 20 and edad <= 29:
    print("Amor y comienzo el trabajo")
else:
    print("No se encontró una categoría para tu edad")