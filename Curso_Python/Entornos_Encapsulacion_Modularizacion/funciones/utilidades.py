
# Este es un archivo externo que acabamos de crear
IMPUESTO = 0.21

def calcular_precio_final(precio):
    return precio * (1 + IMPUESTO)

def saludar(nombre):
    return f"Hola {nombre}, bienvenido al sistema."
