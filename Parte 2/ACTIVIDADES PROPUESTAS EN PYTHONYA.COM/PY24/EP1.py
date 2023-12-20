# La función cantidad_vocales recibe un string como parametro
def cantidad_vocales(cadena):
    # Pasamos esta cadena a minusculas
    cadena2=cadena.lower()
    vocales=0
    # Por cada letra de la cadena si es una a,e,i,o o u el contador vocales se suma 1
    for i in range(len(cadena)):
        if cadena2[i]=="a" or cadena2[i]=="e" or cadena2[i]=="i" or cadena2[i]=="o" or cadena2[i]=="u":
            vocales+=1
    print(f"Cantidad de vocales de la palabra \"{cadena}\" es {vocales}.")

cantidad_vocales("hola")
cantidad_vocales("buenas")
cantidad_vocales("tardes")