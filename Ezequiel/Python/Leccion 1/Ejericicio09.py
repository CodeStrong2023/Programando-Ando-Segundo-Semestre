# Ejercicio 9: Mostrar una frase sin espacion y contar su longitud
# Hacer un programa dond el usuario ingrese una frase, se le
# devolvera la misma frase pero sin espacios en blanco, y
# ademas un contador de cuantos caracteres tiene la frase
# (sin contar los espacion en blanco)
#Ejemplo:           frase = vivir por siempre en paz
#                   fraseFinal = vivirpor siemprenepaz
#                   N de caracteres = 20

frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i

frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N de caracteres: {len(frase1)}')