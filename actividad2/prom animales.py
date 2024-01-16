'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: prom animales
'''
# Entrada de datos
cadena = input()

# Contar la cantidad de animales y mesas
num_animales = cadena.count('@')
num_mesas = cadena.count('#')

# Calcular la cantidad de animales que se quedarán sin mesa
animales_sin_mesa = max(0, (num_mesas * 4) - num_animales)

# Salida de datos
print(animales_sin_mesa)

