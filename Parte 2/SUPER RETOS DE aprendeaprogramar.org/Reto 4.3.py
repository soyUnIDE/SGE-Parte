def esPalindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios
    texto_procesado = ''.join(texto.lower().split())
    
    # Verificar si el texto es igual a su inverso
    return texto_procesado == texto_procesado[::-1]
