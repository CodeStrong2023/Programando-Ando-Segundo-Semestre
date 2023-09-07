#tipo set
planetas = {'Marte', 'Jupiter','Venus'}
print(len(planetas)) #Usamos la funcion len = len significa largo

#revisar si un elemnento existe dentro del set
print('Jupiter' in planetas)

#Agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') #Ante un mal ingreso o inexistencia da error
print(planetas)
planetas.discard('Tierra')# esta no da error
print(planetas)


#limpiar set
planetas.clear()
print(planetas)

#eliminar set o conjunto
del planetas
print(planetas)#al eliminar nos muestra un error


##REPASO DE  CONJUNTOS
#en los  conjuntos se puede agregar un solo ellemtno a la vez

conjunto = set()
conjunto1 = {'bye', }
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto1.add('hola')
print(conjunto1)

#preguntamos si el numero 3 no esta en el conjunto1
print(3 not in conjunto1)

#igualdad entre conjuntos, nos va a devolver un bool, true o false

print(conjunto1 == conjunto)

#operaciones en conjuntos


