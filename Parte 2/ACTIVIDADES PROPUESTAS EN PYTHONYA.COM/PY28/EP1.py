# La funcion sumar recibe como minimo dos parametros de tipo numerico y como maximo 5 los tres ultimos como no son obligatorios se les pone el valor de 0
def sumar(v1,v2,v3=0,v4=0,v5=0):
    suma=v1+v2+v3+v4+v5
    return suma

print(f"La suma de 5+6 = {sumar(5,6)}")
print(f"La suma de 5+6+3 = {sumar(5,6,3)}")
print(f"La suma de 1+1+1+1 = {sumar(1,1,1,1)}")
print(f"La suma de 1+1+1+1+1 = {sumar(1,1,1,1,1)}")