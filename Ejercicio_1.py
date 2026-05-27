


sesiones = [
    [1, 111, 10],
    [2, 171, 6],
    [3, 40, 20],
    [4, 100, 16],
    [5, 200, 18],
    [6, 34, 11],
    [7, 326, 12],
    [8, 39, 18],
    [9, 274, 14],
    [10, 279, 9],
]


def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"



for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    nivel = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente, "- Compromiso:", nivel)
