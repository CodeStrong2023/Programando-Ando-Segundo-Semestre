# ejercicio 9: mostrar una frase sin espacios y contar su longitud
# hacer un programa donde el usuario ingrese una frase, se le devolvera la misma
# frase pero sin espacios en blanco, ademas un contandor de cuantos carateres
# tiene la frase (sin contar espacios en blanco)
# ejemplo:              frase = vivir por siempre en paz
#                       frse final = vivirporsiemprenepaz
#                       n° de caracteres = 20
frase1 = input("digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nfrase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")
