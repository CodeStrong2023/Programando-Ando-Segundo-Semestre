# Definir la cantidad de personas
cantidad_personas = 5

# Inicializar la variable para almacenar la sumatoria de salarios
sumatoria_salarios = 0

# Iterar para cada persona
for i in range(cantidad_personas):
    # Obtener las horas trabajadas y la tarifa de pago para la persona actual
    horas_trabajadas = int(input("Ingrese las horas trabajadas para la persona {}: ".format(i + 1)))
    tarifa_pago = float(input("Ingrese la tarifa de pago para la persona {}: ".format(i + 1)))

    # Calcular el salario para la persona actual
    salario = horas_trabajadas * tarifa_pago

    # Imprimir el salario para la persona actual
    print("El salario de la persona {} es: {}".format(i + 1, salario))

    # Agregar el salario al total
    sumatoria_salarios += salario

# Imprimir la sumatoria de los salarios
print("La sumatoria de todos los salarios es: {}".format(sumatoria_salarios))
