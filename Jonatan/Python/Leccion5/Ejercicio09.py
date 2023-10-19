#ejercicio 09: mostrar una frase sin espacios y contar su longitud
# hacer un programa donde el usuario ingrese una frase
#s ele devolvera la misma frase peros in espacios en blanco, y ademas un contador
#de cuantos caracteres tiene la frase
#(sin contar los espacios en blanco)
#ejemplo: frase = vivir por siempre en paz
#         frase final = vivirporsiempreenpaz
#         N` de caracteres = 21


contador = 0#iniciamos el contador en 0
frase1 = input('Digite una frase: ')#pedimos la frase al usuario
frase2 = " "#iniciamos un variable vacia
for i in frase1:#recorremos la frase ingresada por el usuario
    if i != " ":#si la palabra recorrida es diferente a un espacio " "
        frase2 += #entonces se la palabra se pasa a la variable vacia
frase1 = frase2#luego usamos la variable vacia para pasarla a la variable principal
print(f'\n Frase final: {frase1}')#mostramos al usuario la frase sin espacios
print(f'Numero de Caracteres: {len(frase1)}')#mostramos la cantidad de caracteres con la funcion "LEN" en la concatenacion
