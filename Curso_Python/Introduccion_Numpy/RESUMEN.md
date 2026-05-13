# NumPy:
- Es la librería en Python fundamental para el cálculo numérico.
- Su estructura principal es el ndarray, un array multidimensional mucho más rápido y eficiente que las listas normales de Python.
- Hay que importar la libreria (import numpy as np)
### ndarray:
- Se introduce el array multidimensional (ndarray), que a diferencia de las listas de Python, contiene elementos de un solo tipo de dato para permitir cálculos ultrarrápidos.

## Crear tipos de ndarray 
````python
np.array() # Convierte listas en arreglos (arrays).
a = np.array([1, 2, 3, 4])
print(a) # [1 2 3 4]

np.zeros() # Crea un array lleno de ceros
z = np.zeros(5) # Con una sola dimencion
print(z) # [0. 0. 0. 0. 0.]
z2 = np.zeros((2, 3)) # Con dos dimenciones
print(z2) # [[0. 0. 0.] [0. 0. 0.]]

np.ones() # Crea un array lleno de unos, lo mismo que .zero() pero con 1

np.arange() # Crea una secuencia de números (como range, pero con NumPy)
r = np.arange(0, 10, 2) # (inicio, fin, paso)
print(r) # [0 2 4 6 8]

np.linspace() # Crea números equidistantes entre dos valores.
l = np.linspace(0, 10, 5) # (inicio, fin, cantidad de puntos)
print(l) # [ 0.   2.5  5.   7.5 10. ]

👉 .arange() = “cada cuánto salto”
👉 .linspace() = “cuántos puntos quiero”
````
# Atributos y Propiedades
````python
# Para conocer las dimensiones (filas y columnas).
np.shape()
# El tipo de dato almacenado (int, float, etc.)
np.dtype()
# El número total de elementos
np.size()
````
# Manipulación y Slicing (Rebanado)
## 1- Indexación: 
- El "GPS" de tus datos:
- La indexación permite acceder a un valor exacto indicando su posición (fila, columna).
````python
 import numpy as np
 # Creamos una matriz de 3x3
 matriz = np.array([[10, 20, 30], 
                    [40, 50, 60], 
                    [70, 80, 90]])
# Acceder al número 50 (Fila 1, Columna 1 -> recuerda que empieza en 0)
elemento = matriz[1, 1] 
print(elemento) # Resultado: 50
````
## 2- Slicing (Rebanado):
- "Cortar" trozos de información
- A diferencia de la indexación simple, el slicing te permite extraer subconjuntos completos de datos de manera eficiente.
````python
# Ejemplo: Extraer solo la primera columna de todas las filas:
# Usamos el operador ':' para decir "todas las filas"
# Y el '0' para la primera columna
primera_columna = matriz[:, 0] 

print(primera_columna) # Resultado: [10, 40, 70]

# Extraer un bloque (las primeras 2 filas y 2 columnas)
sub_matriz = matriz[0:2, 0:2]
print(sub_matriz)
# Resultado:
# [[10, 20],
#  [40, 50]]
````
## 3- Reshape:
- Cambiar la forma sin perder la esencia
- El reshape es fundamental en IA y Data Science para adaptar los datos a lo que espera un modelo (por ejemplo, convertir una lista plana en una matriz).
````python
# Ejemplo: De una lista de 6 elementos a una matriz de 2x3
# Creamos un array de una sola dimensión (1D)
datos = np.arange(1, 7) # [1, 2, 3, 4, 5, 6]

# Lo transformamos en una matriz de 2 filas y 3 columnas
matriz_nueva = datos.reshape(2, 3)

print(matriz_nueva)
# Resultado:
# [[1, 2, 3],
#  [4, 5, 6]]
# Diferencia clave:
# Al hacer reshape, el número total de elementos debe coincidir
# (no puedes convertir 6 elementos en una matriz de 4x2 porque te faltarían datos).
 ````

# Operaciones Matemáticas y Vectorización
- Una de las mayores ventajas de NumPy es que permite trabajar con arrays completos sin usar bucles for.
- Las operaciones se aplican posición por posición.
### Suma, Resta y Multiplicación
 ````python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Suma
print(a + b)   # Resultado: [5 7 9]
# Resta
print(a - b)   # Resultado: [-3 -3 -3]
# Multiplicación
print(a * b)   # Resultado: [4 10 18]
 ````
### División y potencias
 ````python
# Divicion
print(a / b) # Resultado: [0.25 0.4  0.5 ]
# Potencia
print(a ** 2) # Resultado: [1 4 9]
 ````
### Vectorización
- La vectorización significa aplicar operaciones sobre arrays completos de manera eficiente y rápida.
- #### Sin vectorización (más lento)
````python
lista = [1, 2, 3, 4]
resultado = []
for x in lista:
    resultado.append(x * 2)
print(resultado)
````
- #### Con vectorización (NumPy)
````python
arr = np.array([1, 2, 3, 4])
resultado = arr * 2
print(resultado)
````

# Funciones de Agregación:
- Métodos para obtener estadísticas rápidas como np.mean(), np.sum(), np.min(), np.max() y la desviación estándar.
- Permiten obtener estadísticas rápidas de un array.
### Ejemplo con array
````python
datos = np.array([10, 20, 30, 40, 50])

# Suma Total
np.sum(datos) # Resultado: 150

# Promedio
np.mean(datos) # Resultado: 30.0

# Minimo y Maximo
np.min(datos) # Resultado: 10
np.max(datos) # Resultado: 50
````
### Desviacion Estandar
- Mide cuánto se dispersan los datos respecto al promedio.
````python
np.std(datos)
# Resultado: 14.1421356237
````
### Ejemplo con matrices
````python
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Suma Total
np.sum(matriz) # Resultado: 21

# Suma por Filas
np.sum(matriz, axis=1) # Resultado: [ 6 15]

# Suma por Columnas
np.sum(matriz, axis=0) # Resultado: [5 7 9]
````

# Broadcasting: 
- El broadcasting permite operar arrays de diferentes tamaños sin copiarlos manualmente.
- NumPy “expande” automáticamente dimensiones compatibles.
- Reglas básicas del broadcasting, Dos dimensiones son compatibles si:
 1- Son iguales
 2- Una de ellas es 1
````python
# Ejmplo1: Sumar un número a un array
a = np.array([1, 2, 3])
print(a + 10) # El 10 se aplica a todos los elementos.
# Resultado: [11 12 13]

# Ejemplo 2: array + vector
# NumPy replica virtualmente el vector para cada fila.
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
vector = np.array([10, 20, 30])
print(matriz + vector)
# Resultado:
[[11 22 33]
 [14 25 36]]
````


## Principales funciones: 
- np.random.rand() : Genera números decimales aleatorios entre 0 y 1 con distribución uniforme	np.random.rand(2,3)
- np.random.randn(): Genera números aleatorios siguiendo una distribución normal (media 0, desviación 1)	np.random.randn(3,3)
- np.random.randint():	Genera números enteros aleatorios dentro de un rango	np.random.randint(0,10,(2,2))
- np.random.random():	Genera un array de decimales aleatorios entre 0 y 1	np.random.random((2,2))
- np.random.choice():	Selecciona elementos aleatorios de una lista o array	np.random.choice([1,2,3], size=2)
- np.random.shuffle():	Mezcla los elementos de un array modificando el original	np.random.shuffle(a)
- np.random.permutation():	Devuelve una copia mezclada del array sin modificar el original	np.random.permutation(a)
- np.random.seed():	Fija una semilla para obtener siempre los mismos números aleatorios	np.random.seed(42)
- np.random.uniform(): Genera números decimales aleatorios dentro de un intervalo específico	np.random.uniform(0,10,5)
- np.random.normal()	Genera números aleatorios con distribución normal personalizada	np.random.normal(0,1,5)
- np.random.binomial()	Simula resultados tipo éxito/error repetidos varias veces	np.random.binomial(10,0.5,5)
- np.random.poisson()	Genera eventos aleatorios que ocurren en intervalos de tiempo o espacio	np.random.poisson(5,10)
- np.random.default_rng()	Crea un generador aleatorio moderno recomendado por NumPy	rng = np.random.default_rng()
- rng.integers()	Genera enteros aleatorios usando el generador moderno	rng.integers(0,10,(3,3))


Evita bucles for cuando puedas vectorizar operaciones.
Usa dtype apropiados para ahorrar memoria.
Aprovecha broadcasting y slicing.
