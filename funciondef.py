def puntuacion(clase):
    return sum(clase) / len(clase)

clase = [7, 8, 9]
media = puntuacion(clase)
print("La puntuación de esta clase es:", media)

clase = [5, 6, 4, 10]
media = puntuacion(clase)
print("La puntuación de esta clase es:", media)


