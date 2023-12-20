def factorial(num):
    # Verificar si el número está dentro del rango permitido (0 a 10)
    if 0 <= num <= 10:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado
    else:
        raise ValueError("El número debe estar entre 0 y 10")