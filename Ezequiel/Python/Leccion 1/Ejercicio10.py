# Ejercicio 10: No repetir caracteres
# hacer un programa que ida una cadena por eclado, luego
# meter os caracteres en una lista sin repetir carateres.

cadena = input("Digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')

