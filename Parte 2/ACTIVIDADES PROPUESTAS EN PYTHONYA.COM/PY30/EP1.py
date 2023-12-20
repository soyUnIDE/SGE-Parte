# La funcion cantidad_mayores18 recibe como minimo un valor y como maximo casi infinitos y segun si el parametro numerico es mayor que 18 se suma 1 la variable cant que es la que despues se devuelve
def cantidad_mayores18(edad,*edades):
    cant=0
    if edad>18:
        cant+=1
    for i in range(len(edades)):
        if edades[i]>18:
            cant+=1
    return cant

print(f"Cantidad de personas mayores a 18 años son: {cantidad_mayores18(23,28,67,44,2,5,6,77,88)}")