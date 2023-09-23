
N = int(input("Ingrese el valor de N: "))# pedimos al usuario el valor de N

suma = 0# Inicializar la variable de suma

for i in range(1, N+1):# Calcular la suma de los N primeros números
    suma += i
print("La suma de los", N, "primeros números es:", suma)# mostramos la usuario el resultado
