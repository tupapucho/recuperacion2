'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: Creciente-decreciente
'''
# Entrada de datos
N = int(input())
conjunto = list(map(int, input().split()))

# Salida de datos
print(*sorted(conjunto))
print(*sorted(conjunto, reverse=True))
