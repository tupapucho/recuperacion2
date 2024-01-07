'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: Chicharronera
'''
import math

a, b, c = map(int, input().split())

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(round(x1, 2), round(x2, 2))
