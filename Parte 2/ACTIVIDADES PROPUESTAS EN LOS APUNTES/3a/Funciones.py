def mcd(a,b):
    tem1=a
    tem2=b
    temporal=0
    while b!=0:
        temporal=b
        b=a%temporal
        a=temporal
    print(a)

def esPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print(f"El máximo común divisor de 20 y 12 es {mcd(20,12)}")
for i in range(1,51):
    if (esPrimo(i)):
        print(i,"es primo.")