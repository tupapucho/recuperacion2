'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: pago de pasaje
'''
precio_primera_caseta = float(input())
total_pagado = 0
precios_casetas = [precio_primera_caseta]

for _ in range(4):
    precio_primera_caseta *= 0.955
    total_pagado += precio_primera_caseta
    precios_casetas.append(precio_primera_caseta)

print(round(total_pagado, 4))
print(precios_casetas)
