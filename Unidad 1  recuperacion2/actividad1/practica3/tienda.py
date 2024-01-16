'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: tienda
'''
def calcular_descuento(monto):
    if monto < 500:
        return 0
    elif 500 <= monto <= 1000:
        return 0.05
    elif 1001 <= monto <= 7000:
        return 0.11
    elif 7001 <= monto <= 15000:
        return 0.18
    else:
        return 0.25

def calcular_monto_a_pagar(monto_compra):
    descuento = calcular_descuento(monto_compra)
    monto_a_pagar = monto_compra - (monto_compra * descuento)
    return monto_a_pagar

if __name__ == "__main__":
    montos_compra = []
    while True:
        try:
            monto = float(input())
            montos_compra.append(monto)
        except EOFError:
            break

    for monto in montos_compra:
        monto_a_pagar = calcular_monto_a_pagar(monto)
        print("{:.2f}".format(monto_a_pagar))
