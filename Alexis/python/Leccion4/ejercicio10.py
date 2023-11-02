# ejercicio 10: no repetir caracteres
# hacer un programa quepida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres
cadena = input("digite una cadena: ")
lista = []
for i in cadena:
    if i not in lista: # si el caracter aun esta en la lista
        lista.append(i) # lo agregamos a la lista
print(f"\n lista de caracteres sin repetir ninguno: \n {lista}")


