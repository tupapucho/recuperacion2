'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: repartir par
'''
total_manzanas = int(input())
num_hermanas = int(input())

manzanas_por_hermana = total_manzanas // num_hermanas

if manzanas_por_hermana % 2 == 0:
    print(manzanas_por_hermana)
else:
    print("NO")
