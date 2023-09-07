#Se crea una pila usando listas

pila = [1,2,3]
#se agrega elementos a la pila por el fiman

pila.append(4)

pila.append(5)
print(pila)

#Se elimina los elementoo desde el final
#se lo elimina y se lo guarda en una variable
elementoBorrado = pila.pop()

print(f'Sacamos el elemento {elementoBorrado}')
print(f'Asi nos quedo lo pila: {pila}')


#COLAS: datos de tipo fifo (first input / first output)

cola = ['Ariel','Osvaldo','Liliana','Pilar',]

#agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

#Agrego una linea para poder comiteargit status