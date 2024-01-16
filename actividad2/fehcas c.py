'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: fechas
'''
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 29 if mes == 2 and es_bisiesto(anio) else dias_por_mes[mes]

def contar_dias(dia, mes, anio):
    return sum(dias_en_mes(i, anio) for i in range(1, mes)) + dia

def main():
    dia1, mes1, anio1 = map(int, input().split())
    dia2, mes2, anio2 = map(int, input().split())

    dias1 = contar_dias(dia1, mes1, anio1)
    dias2 = contar_dias(dia2, mes2, anio2)

    print(dias2 - dias1)

if __name__ == "__main__":
    main()
