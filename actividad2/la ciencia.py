'''
Autor: Antonio Uribe Ramirez
fehca:10/01/2024
problema: la ciencia
'''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def operacion_matematica(celsius):
    return (celsius_to_fahrenheit(celsius) + celsius_to_kelvin(celsius)) * (celsius + 100)

def main():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    resultado_fahrenheit = celsius_to_fahrenheit(celsius)
    resultado_kelvin = celsius_to_kelvin(celsius)
    resultado_operacion = operacion_matematica(celsius)

    # Salida con restricciones de formato
    print(f"{resultado_fahrenheit:.2f} {resultado_kelvin:.2f} {resultado_operacion:.2f}")

if __name__ == "__main__":
    main()


