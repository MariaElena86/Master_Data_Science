#Determinar si un año es bisiesto o no

try:
    año = int(input("Ingrese un año: "))
    print(f"Residuo de dividir {año} entre 400 es {año % 400}")
    print(f"Residuo de dividir {año} entre 100 es {año % 100}")
    print(f"Residuo de dividir {año} entre 4 es {año % 4}")

    if (año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
except Exception as e:
    print(f"Error: {e}")