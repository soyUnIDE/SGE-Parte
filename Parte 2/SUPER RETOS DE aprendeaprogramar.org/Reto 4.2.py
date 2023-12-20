def fibonacci(num):
    # Verificar si el número está dentro del rango permitido (0 a 20)
    if 0 <= num <= 30:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            fib = [0, 1]  # Inicializar lista con los primeros dos términos
            for i in range(2, num + 1):
                fib.append(fib[i - 1] + fib[i - 2])
            return fib[num]
    else:
        raise ValueError("El número debe estar entre 0 y 30")
