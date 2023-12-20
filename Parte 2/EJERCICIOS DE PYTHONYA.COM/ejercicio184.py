# Importamos desde el modulo math las funciones sqrt como raiz y la funcion pow como elevar
from math import sqrt as raiz, pow as elevar

# Pedimos al usuario un valor numerico entero
valor=int(input("Ingrese un valor entero:"))
# Almacenamos la raiz cuadrada del valor pedido
r1=raiz(valor)
# Almacenamos el cubo de la variable almacenada
r2=elevar(valor,3)
# Mostramos la raiz cuadrada del valor pedido
print("La raiz cuadrada es",r1)
# Mostramos el cubo de la variable almacenada
print("El cubo es",r2)