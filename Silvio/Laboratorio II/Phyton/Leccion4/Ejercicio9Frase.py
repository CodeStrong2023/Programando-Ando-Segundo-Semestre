# Mostrar una frase sin espacios y contar sus caracteres

frase = input("Digite una frase: ")
frasefinal = " "

for caracter in frase:
    if caracter != " ":
        frasefinal += caracter

print(f'\nFrase final: {frasefinal}')
print(f'Nª de caracteres: {len(frasefinal)}')
