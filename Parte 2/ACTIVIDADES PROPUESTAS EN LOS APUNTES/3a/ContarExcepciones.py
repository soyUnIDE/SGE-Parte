import sys

try:
    if (len(sys.argv)==3):
        for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
            print(i)
    else:
        print("Error: No se han recibido 2 numeros como parámetro")
except:
    print("Datos incorrectos")