'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: avion
'''
import math

def calcular_velocidad_promedio_aire(velocidad, angulo, direccion):
    if direccion == 0:  
        angulo = 180 - angulo

    angulo_radianes = math.radians(angulo)

    velocidad_promedio = velocidad * math.cos(angulo_radianes)

    velocidad_promedio = math.floor(velocidad_promedio)

    return velocidad_promedio

try:
    entrada = input().strip().split(",")
    velocidad = int(entrada[0])
    angulo = int(entrada[1])
    direccion = int(entrada[2])

    resultado = calcular_velocidad_promedio_aire(velocidad, angulo, direccion)
    print(resultado)
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números enteros.")
except IndexError:
    print("Entrada incompleta. Asegúrate de ingresar todos los valores necesarios.")
except Exception as e:
    print(f"Error inesperado: {e}")
