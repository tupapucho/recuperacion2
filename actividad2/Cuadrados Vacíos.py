'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: cuadros vacios
'''
n = int(input())

print("*" * n)

for i in range(n - 2):
    print("*" + " " * (n - 2) + "*")

if n > 1:
    print("*" * n)
