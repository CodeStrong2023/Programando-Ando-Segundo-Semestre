#Ejercicio 10: No repetir caracteres
#Hacer un programa que pida una cadena por teclado, luego
#meter los caracteres a una lista sin repetir caracteres
cadena = input('Digite una cadena\n')
lista = []
for i in cadena:
    if i not in lista: #Si el caracter no esta en la lista
        lista.append(i) #Agregamos el valor de i a la lista
print(f'\nLista de caracteres sin repetir ninguno:\n{lista}')

