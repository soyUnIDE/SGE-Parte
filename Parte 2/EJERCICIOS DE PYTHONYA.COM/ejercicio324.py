# La funcion filtrar reecibe una cadena y una funcion lambda como parametro y segun la funcion hace una cosa o otra
def filtrar(cadena,fn):
    cad=""
    for caracter in cadena:
        if fn(caracter):
            cad=cad+caracter
    return cad


cadena="¿Esto es la prueba 1 o la prueba 2?"
print("String original")
print(cadena)
print("String solo con las vocales")
# En cadena2 se almacena la cadena principal pero solo las vocales en mayuscula o minuscula
cadena2=filtrar(cadena, lambda car: car == 'a' or car == 'e' or car == 'i' or car == 'o' or car == 'u' 
                                    or car == 'A' or car == 'E' or car == 'I' or car == 'O' or car == 'U')
print(cadena2)

print("String solo con los caracteres en minúscula")
# En cadena2 se almacena la cadena principal pero solo las letras en minusculas
cadena3=filtrar(cadena, lambda car: car >='a' and car <= 'z')
print(cadena3)

print("String solo con los caracteres no alfabéticos")
# En cadena2 se almacena la cadena principal pero solo lo que no son letras
cadena3=filtrar(cadena, lambda car: not(car >='a' and car <= 'z') and not(car >='A' and car <= 'Z'))
print(cadena3)