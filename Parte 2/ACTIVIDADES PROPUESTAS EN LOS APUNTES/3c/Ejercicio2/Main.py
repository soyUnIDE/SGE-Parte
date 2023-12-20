from PIL import Image
import os.path

nombreFichero=input("Introduce el nombre de una imagen con extension: ")

if (os.path.isfile(nombreFichero)):
    imagen= Image.open(nombreFichero)
    ancho=1
    alto=1
    while ancho!=0 and alto!=0:
        ancho=int(input("Introduce la cantidad de pixeles de ANCHO a la que quiere escalar: "))
        alto=int(input("Introduce la cantidad de pixeles de ALTO a la que quiere escalar: "))
        tamano = (ancho, alto)
        imagenNueva =imagen.resize(tamano)
        imagenNueva.save(f"{ancho}_{alto}{nombreFichero}")
else:
    print(f"La imagen {nombreFichero} no existe.")