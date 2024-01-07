def es_capicua(numero):
    str_numero = str(numero)
    return str_numero == str_numero[::-1]

def generar_capicua(numero):
    while not es_capicua(numero):
        reverso = int(str(numero)[::-1])
        numero += reverso
    return numero

numero = int(input())

capicua = generar_capicua(numero)
print(capicua)
