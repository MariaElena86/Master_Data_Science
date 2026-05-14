# Libreria Pandas:
- Es la librería fundamental de Python para la manipulación y el análisis de datos estructurados. 
- Permite trabajar con datos como si fueran tablas de Excel.
- El objetivo es aprender a transformar datos en crudo en información útil para la toma de decisiones.
````python
# Importar las librerias
import pandas as pd
import numpy as np
from IPython.display import display

np.random.seed(42)# esa configuracion es para que siempre genere los mismos datos cuando se cree un np.array()
````
# Estructuras de Datos Fundamentales
## Series: 
- Se explican como arreglos unidimensionales similares a una columna en una tabla o una lista de Python con etiquetas (índices). Es una columna con índices.

### Crear Series
````python
# Crear Serie a partir de una lista
list = [10,20,30]
s_list = pd.Series(list, index=['a','b','c'])

# Acceder a los valores
s_list['b'] # print 20
#Propiedades importantes
s_list.index # print ['a','b','c']
s_list.values # print [10,20,30]

# Crear Serie a partir de un diccionario
data_dict = {'Apple': 100, 'Banana': 200, 'Cherry': 150}
s_dict = pd.Series(data_dict) # aqui el index la clave del diccionario
````

## DataFrames:
- Se definen como estructuras bidimensionales (tablas) que contienen múltiples Series compartiendo un mismo índice.
- Resumen: es una tabla con filas y columnas.
### Operaciones y Manipulación de Datos
````python
# Crear el data frame desde un dataset local
dataset = {
    'Name':['Ana','Luis'],
    'Age':[20,30]
}
df = pd.DataFrame(dataset)

# Crear dataframe desde un fichero externo(csv, excel, json,etc)
# Cargar desde un fichero CSV
pd.read_csv("archivo.csv")
# Cargar desde un fichero JSON
pd.read_json("archivo.json")

#Cargar desde un fichero Excel:
#Se necesita instalar esta libreria pip install openpyxl
pd.read_excel("archivo.xlsx")

# Guardar los datos del dataframe a un fichero CSV
df.to_csv("resultado.csv")

#Ver dimensiones(filas → shape[0], columnas → shape[1])
df.shape
````
#### Nota:
Diferencia entre Dataset y DataFrame:
- Dataset: es la materia prima (el libro), Se refiere a la colección de datos(ejmplo .csv)
- DataFrame: es la mesa de trabajo donde lo abres para leerlo, subrayarlo y analizarlo (el objeto en Python). Es una estructura de datos específica dentro de un lenguaje de programación.

### Métodos de inspección rápida para entender la composición y estadísticas básicas del dataset:
````python
df = pd.DataFrame({
    'Name':['Ana','Luis'],
    'Age':[20,30]
})
# Mostrar las Primeras filas
df.head()
# Mostrar Últimas filas
df.tail()
# Mostra Información general
df.info()
# Mostrar Estadísticas
df.describe() 
````

## Selección de datos
````python
df =   A   B   C   D
    0  1   2   3   4
    1  5   6   7   8
    2  9  10  11  12
    3 13  14  15  16
    4 17  18  19  20
    5 21  22  23  24

# Seleccionar una columna
df['A']

# Seleccionar varias columnas
df[['A','B']]

# .loc[]
# selecciona por nombres (etiquetas), .loc INCLUYE el último valor
df.loc[0:2, ['A','D']] # “Dame las filas de la 0 a la 5 y las columnas A y D”
# print
   A   D
0  1   4
1  5   8
2  9  12

# .iloc[]
# selecciona por posiciones (índices numéricos) .iloc NO INCLUYE el último valor
df.iloc[0:2, 0:3] # “Dame las filas desde la posición 0 hasta 4 y las columnas desde posición 0 hasta 2”
# print()
   A   B
0  1   2
1  5   6
````
## Filtrar datos
- Filtrar: significa👉 quedarte solo con las filas que cumplen una condición.
- 👉 Luego Pandas usa eso como filtro:
True → se queda
False → se elimina
- Se usan comparaciones (>, <, ==) y Se combinan con los operadores &(AND), |(OR), ~(NOT)

````python
df =   A   B
    0  10  5
    1  60 15
    2  30 25
    3  80 10
# Condicion simple
df[df['A'] > 50] # 👉 “Dame las filas donde df['A'] sea mayor que 50”
# Como funciona: al aplicar esta condicion df['A'] > 50 en cada celda
# resulta en [False, True, False, True]
# y retorna solo los True
   A   B
1  60 15
3  80 10

# Varias condiciones
df[(df['A'] > 50) & (df['B'] < 20)] # Dame las 👉 “Filas donde A > 50 Y B < 20”
# retorna
   A   B
1  60 15
3  80 10
````

## Limpieza y Transformación
### 1- Gestión de valores nulos: 
Identificación y tratamiento de datos faltantes mediante .isnull(), .dropna() o .fillna().
````python
df =  Nombre   Edad   Salario
    0  Ana      25     2000
    1  Luis     NaN    2500
    2  Marta    30     NaN
    3  Juan     NaN    NaN

# df.isnull() 👉 Identificar valores nulos
# Devuelve una tabla de True(si hay valor nulo) / False(no hay null, el datos es correcto)
       Nombre   Edad   Salario
    0  False    False  False
    1  False    True   False
    2  False    False  True
    3  False    True   True

# .dropna() 👉 Elimina filas completas que tengan algún valor NaN
# OJO: Es agresivo: puedes perder muchos datos. Úsalo solo si tienes muchos datos
df_sin_nulos = df.dropna()
# print
 df_sin_nulos = Nombre   Edad   Salario
              0  Ana      25     2000  

# .fillna() 👉 Rellenar valores NaN
👉 Rellenar utilizando un valor
   df["Salario"] = df["Salario"].fillna(0) # rellena los valores Nan de la columna salario con 0
 # print
df =  Nombre   Edad   Salario
    0  Ana      25     2000
    1  Luis     0      2500
    2  Marta    30     0
    3  Juan     0      0

👉 Rellenar utilizando una condicion
condicion = df["Edad"].mean() # Calcula la media de Edad (sin contar NaN)
df["Edad"] = df["Edad"].fillna(condicion)  # Rellena los NaN de la columna Edad con ese valor de la media
# print
media_edad = (25+30)/2 = 27.5
df =  Nombre   Edad   Salario
    0  Ana      25     2000
    1  Luis     27.5   2500
    2  Marta    30     27.5
    3  Juan     27.5   27.5
````

### 2- Crear nuevas columnas:
Cómo realizar operaciones aritméticas entre columnas existentes para generar nuevos indicadores.
````python
# Crear nueva columna con el total de ventas
df["Total_Venta"] = df["Precio"] * df["Cantidad"]

# Crear columna con impuesto
df["Impuesto"] = df["Total_Venta"] * 0.21
````
### 3- Agrupar Columnas: (GroupBy): 
Uso de .groupby() junto con funciones de agregación (sum, mean, count) para realizar análisis segmentados.
````python
# Agrupar por departamento y calcular métricas
resumen = df.groupby("Departamento")["Salario"].agg([
    "sum",
    "mean",
    "count"
])
````

## Ordenar datos

````python
# Ascendente
df.sort_values(by='A')

# Descendente
df.sort_values(by='A', ascending=False)

# Varias columnas
df.sort_values(
    by=['A','B'],
    ascending=[False, True]
)
````



