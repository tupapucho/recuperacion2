cadena = input().strip().split()
resultado = ' '.join([palabra.lower() if i % 2 == 0 else palabra.upper() for i, palabra in enumerate(cadena)])
print(resultado)
