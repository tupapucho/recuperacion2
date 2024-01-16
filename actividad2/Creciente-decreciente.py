# Entrada de datos
N = int(input())
conjunto = list(map(int, input().split()))

# Salida de datos
print(*sorted(conjunto))
print(*sorted(conjunto, reverse=True))
