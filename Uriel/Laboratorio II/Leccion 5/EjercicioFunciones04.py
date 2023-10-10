#Ejercicio 04: Calculadora de impuestos
#Crear una funcion para calcular e total de un pago incluyendo el IVA
#Formula de pago: pagoTotal = pagoSinImpuesto + pagoSinImpuesto *(impuesto/100)
#Proporcione el pago sin impuesto: 1000
#Proporcione el monto del impuesto: 21%
#Pago con impuesto: xxxxx

#Creamos la funcion que calcula el total del pago
def calcularPago(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto*(impuesto/100)
    return pagoTotal

#Ejecutamos la funcion
pagoSinImpuesto = float(input('Digite el monto del pago sin inpuesto\n'))
impuesto = float(input('Digite el monto del impuesto a aplicar\n'))
pagoConImpuesto = calcularPago(pagoSinImpuesto, impuesto)
print(f'El monto total es: {pagoConImpuesto}')