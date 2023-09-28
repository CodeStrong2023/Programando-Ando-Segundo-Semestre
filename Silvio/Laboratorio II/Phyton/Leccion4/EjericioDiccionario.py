seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura' : 1.70, 'Precio': '50 Millones', 'Posicion': 'Externo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura' : 1.80, 'Precio': '12 Millones', 'Posicion': 'Externo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura' : 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura' : 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura' : 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Arquero'},
}

print('Valores Originales')
for key, value in seleccionArgentina.items():
    print(key, value)

nuevo_jugador = {
    'Nombre': 'Josesito Mirás',
    'Edad': 25,
    'Altura' : 1.75,
    'Precio': '20 Millones',
    'Posicion': 'Mediocampista',
}
numero_camiseta = 12

seleccionArgentina[numero_camiseta] = nuevo_jugador

nuevo_jugador = {
    'Nombre': 'Franco Augusto',
    'Edad': 42,
    'Altura': 1.73,
    'Precio': '4 Millones',
    'Posicion': "Externo Izquierdo",
}
numero_camiseta = 13

seleccionArgentina[numero_camiseta] = nuevo_jugador

nuevo_jugador = {
    'Nombre': 'Eusebio Monté',
    'Edad': 46,
    'Altura': 1.58,
    'Precio': '7 Millones',
    'Posicion': 'Defensor Izquierdo',
}
numero_camiseta = 14

seleccionArgentina[numero_camiseta] = nuevo_jugador

nuevo_jugador = {
    'Nombre': 'Jacinto Rios',
    'Edad': 38,
    'Altura': 1.40,
    'Precio': '14 Millones',
    'Posicion': 'Volante Central',
}
numero_camiseta = 15

seleccionArgentina[numero_camiseta] = nuevo_jugador

print('Nuevos Valores')

for key, value in seleccionArgentina.items():
    print(key, value)