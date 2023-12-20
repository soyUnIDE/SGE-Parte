# La funcion tabla muestra por pantalla el numero pasado por parametro multimplicado por todos los numeros desde el 0 hasta el segundo numero pasado por parameto y si no pasa ningun numero es hasta el 10
def tabla(numero,terminos=10):
    for i in range(terminos+1):
        valor=numero*i
        print(valor,",",sep="   ",end="")

print("Tabla del 3")
tabla(3)
print("\nTabla del 3 con 5 terminos")
tabla(3,5)
print("\nTabla del 3 conm 20 terminos")
tabla(3,20)