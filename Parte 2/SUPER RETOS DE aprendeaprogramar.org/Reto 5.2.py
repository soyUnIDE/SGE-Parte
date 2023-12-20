import re

def numeroPatrones(texto):
    # Convertir la cadena a minúsculas para hacer la búsqueda sin distinguir mayúsculas y minúsculas
    texto = texto.lower()

    # Definir los patrones
    patrones = ["00", "101", "abc", "ho"]

    # Inicializar el contador de patrones
    contador_patrones = 0

    # Buscar cada patrón en la cadena
    for patron in patrones:
        # Utilizar una expresión regular para buscar todas las ocurrencias del patrón
        ocurrencias = re.finditer(f'(?=({patron}))', texto)

        # Incrementar el contador por cada ocurrencia encontrada
        contador_patrones += sum(1 for _ in ocurrencias)

    return contador_patrones