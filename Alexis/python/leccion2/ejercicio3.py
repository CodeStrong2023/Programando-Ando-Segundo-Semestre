# ejercicio calcular la estacion del año
mes = int(input("digite un mes del año (1 -12): "))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = "verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "invierno"
elif mes == 10 or mes == 11 or mes == 12:
    estacion = "primavera"
else:
    estacion = "error, no hay numero para ese mes"
print(f"para el mes {mes} la estacion es: {estacion}")
















