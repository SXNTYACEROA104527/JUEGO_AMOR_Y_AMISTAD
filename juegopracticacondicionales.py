tienes_la_llave = input("¿Tienes una llave? ")

if tienes_la_llave == "si":
    forma = input("¿Qué forma tiene la llave? ")
    color = input("¿De qué color es la llave? ")
    if forma == "cuadrada" and color == "naranja":
        print("Entras por la puerta 1")
    elif forma == "redonda" and color == "amarilla":
        print("Entras por la puerta 2")
    elif forma == "triangular" and color == "rojo":
        print("Entras por la puerta 3")
    else:
        print("Tienes la llave equivocada")
else:
    print("No puedes pasar")

print("Fin")