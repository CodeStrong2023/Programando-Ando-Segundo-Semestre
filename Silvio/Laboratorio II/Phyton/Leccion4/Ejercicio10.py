# Pedir una cadena por teclado
cadena = input("Introduce una cadena: ")

# Crear una lista vacía para almacenar los caracteres
lista = []

# Recorrer la cadena y añadir los caracteres a la lista si no están repetidos
for caracter in cadena:
  if caracter not in lista:
    lista.append(caracter)

# Mostrar la lista resultante
print(lista)
