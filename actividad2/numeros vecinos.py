'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: numeros vecinos
'''
# Entrada de datos
num_casos = int(input())

for _ in range(num_casos):
    a, b = map(int, input().split())

    # Verificar si los números son adyacentes
    if (a == 1 and b == 100) or (a == 100 and b == 1):
        print("SI")
    elif abs(a - b) == 1:
        print("SI")
    else:
        print("NO")

