#EJERCICIO 06: TABLA DE MULTIPLICAR
#HACER UIN PROGRAMA QUE PIDA UN NUMERO POR TECLADO Y GUARDE
#EN UNA LISTA SU TABLA DE MULTIPLICAR HASTA EL 10, POR EJMEMPLO:
#SI DIGITA EL 5 LA LISTA TENDRA: 5,10,15,20,25,30,35,40,45,50

num = int(input('Digite un numero: '))
tabla = []

for i in range(1,11):
    tabla.append(i*num)
print(f'\nTabla de Multiplicar del {num} es: \n {tabla}')

for indice,i in enumerate(tabla):
    print(f'{num} x {i} = {tabla[indice]}')