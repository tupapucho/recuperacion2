# Entrada de datos
num_pares = int(input())
max_velocidad = 0

# Calcular la velocidad máxima
for _ in range(num_pares):
    km_recorridos, horas_transcurridas = map(int, input().split())
    velocidad_actual = km_recorridos / horas_transcurridas
    max_velocidad = max(max_velocidad, velocidad_actual)

# Salida de datos
print(int(max_velocidad))
