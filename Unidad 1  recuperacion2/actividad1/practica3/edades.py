'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: edades
'''
n = int(input())
edades = list(map(int, input().split()))
conteo_edades = {}

for edad in edades:
    if edad in conteo_edades:
        conteo_edades[edad] += 1
    else:
        conteo_edades[edad] = 1

for edad, cantidad in sorted(conteo_edades.items()):
    print(f"{edad} {cantidad}")
