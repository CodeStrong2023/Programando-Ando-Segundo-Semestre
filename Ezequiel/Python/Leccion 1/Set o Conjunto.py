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
