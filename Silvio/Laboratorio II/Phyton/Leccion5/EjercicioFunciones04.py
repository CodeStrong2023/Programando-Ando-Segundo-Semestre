# Ejericio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado (IVA)
# Formula: pago_total = pago_sin_puestos + pago_sin_impuestos * (impuesto/100)

# Creamos la funcion que calcula el toal del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es_ {pago_con_impuesto}')
