def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combinaciones(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

nombres = input().split()
nombres = [nombre for nombre in nombres if nombre not in ["Ricardo", "Mirón"]]
num_personas = len(nombres)
num_squads = combinaciones(num_personas, 4)
print(num_squads)
