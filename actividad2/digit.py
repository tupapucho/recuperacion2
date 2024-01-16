'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: prom digit
'''
def es_palindromo(numero):
    str_numero = str(numero)
    return str_numero == str_numero[::-1]

def main():
    numero = int(input("Ingrese un número de 3 dígitos (000-999): "))
    resultado = es_palindromo(numero)
    print(resultado)

if __name__ == "__main__":
    main()
