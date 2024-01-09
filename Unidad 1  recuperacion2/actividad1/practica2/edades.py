'''
Autor: Antonio Uribe Ramirez
fehca:01/01/2024
problema: edades 
'''
edades = list(map(int, input().split()))
edades_set = set(edades)
edades_ordenadas = sorted(edades_set, reverse=True)
print(edades_ordenadas)

'''
no funciona
'''
