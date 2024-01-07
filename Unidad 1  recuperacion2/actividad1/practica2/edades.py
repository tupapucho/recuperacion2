edades = list(map(int, input().split()))
edades_set = set(edades)
edades_ordenadas = sorted(edades_set, reverse=True)
print(edades_ordenadas)
