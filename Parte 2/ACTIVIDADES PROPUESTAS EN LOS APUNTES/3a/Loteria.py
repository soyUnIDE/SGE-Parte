numerosStr=input("Introduzca los 6 números que juega a la lotería (separados por espacios): ")
numeros=numerosStr.split(" ")
for i in range(len(numeros)):
    numeros[i]=int(numeros[i])
numeros.sort()
print(numeros)
rangErr=False
repeErr=False
cont=0
for i in range(len(numeros)):
    if numeros[i] not in range(1,50):
        rangErr=True
    for j in range(len(numeros)):
        if numeros[i] == numeros[j]:
            cont+=1
    if cont>1:
        repeErr=True
    cont=0
if (rangErr or repeErr):
    print("La lista NO es válida:")
    if repeErr:
        print("Hay números repetidos")
    if rangErr:
        print("Hay números menores que 1 o mayores que 49")
else:
    print("La lista es válida:")