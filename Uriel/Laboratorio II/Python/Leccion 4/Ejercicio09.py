#Ejercicio 09: Mostrar una frase sin espaions y contar su longitud
#Ejemplo:
#frase = vivir por siempre en paz
#fraseFinal = vivirporsiempreenpaz
#caracteres = 20
frase = input("Digite una frase a analizar\n")
fraseFinal=""
for i in frase:
    if i != " ":
        fraseFinal += i
print(f'La frase sin espacios en blanco es:\n{fraseFinal.strip()},\ny contiene {len(fraseFinal)} caracteres')
