# La función menor_valor muestra por pantalla el menor valor introducido en los inputs mediante IFs
def menor_valor():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    elif valor2<valor3:
        print(valor2)
    else:
        print(valor3)

menor_valor()
menor_valor()