calificaciones = list(map(int, input().split()))
promedio = sum(calificaciones) / len(calificaciones)
print(round(promedio))
