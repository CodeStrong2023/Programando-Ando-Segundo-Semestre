print("Ingrese los siguientes datos del libro")
nomlib = input("Ingrese el nombre del libro: ")
idlib = input("Ingrese el ID del libro: ")
prelib = int(input("Ingrese el precio del libro: "))
envio = prelib<2000

print (f"Libro: {nomlib}\nID: {idlib}\nPrecio: {prelib}dolares\nEnvio Gratis: {envio}")
