'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: dolares
'''
calificaciones = list(map(int, input().split()))
promedio = sum(calificaciones) / len(calificaciones)
print(round(promedio))
