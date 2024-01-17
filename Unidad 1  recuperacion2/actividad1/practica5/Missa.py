'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: missa
'''
def grado_numero_missa(numero):
    n = 1
    while True:
        suma_digitos = sum(int(digit) ** n for digit in str(numero))
        if suma_digitos == numero:
            return n
        elif suma_digitos > numero:
            return -1
        n += 1

numero = int(input())

resultado = grado_numero_missa(numero)
print(resultado)
