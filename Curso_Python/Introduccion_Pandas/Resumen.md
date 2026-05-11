# Libreria Pandas:
- Es la librería fundamental de Python para la manipulación y el análisis de datos estructurados. 
- Permite trabajar con datos como si fueran tablas de Excel.
- El objetivo es aprender a transformar datos en crudo en información útil para la toma de decisiones.

## Estructuras de Datos Fundamentales
### Series: 
- Se explican como arreglos unidimensionales similares a una columna en una tabla o una lista de Python con etiquetas (índices).
- Resumen: es una columna con índices.
````python
#Crear una serie
s = pd.Series([10,20,30], index=['a','b','c'])
#Acceder a los valores
s['b']
#Propiedades importantes
s.index
s.values
````

### DataFrames:
- Se definen como estructuras bidimensionales (tablas) que contienen múltiples Series compartiendo un mismo índice.
- Resumen: es una tabla con filas y columnas.
````python

#Crear un DataFrame
df = pd.DataFrame({
    'Name':['Ana','Luis'],
    'Age':[20,30]
})
#Ver dimensiones(filas → shape[0], columnas → shape[1])
df.shape
````

### Diferencia entre Dataset y DataFrame:
- Dataset: es la materia prima (el libro), Se refiere a la colección de datos(ejmplo .csv)
- DataFrame: es la mesa de trabajo donde lo abres para leerlo, subrayarlo y analizarlo (el objeto en Python). Es una estructura de datos específica dentro de un lenguaje de programación.


## Operaciones y Manipulación de Datos
### Leer y guardar archivos: 
- Carga y Exploración Inicial
````python
#Leer CSV
pd.read_csv("archivo.csv")
#Leer JSON
pd.read_json("archivo.json")
#Leer Excel: se necesita instalar esta libreria pip install openpyxl
pd.read_excel("archivo.xlsx") 
# Guardar CSV
df.to_csv("resultado.csv")
````


- Métodos de inspección rápida para entender la composición y estadísticas básicas del dataset:
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

## Selección y Filtrado
- Selección de Datos
````python
# Seleccionar una columna
df['A']
# Seleccionar varias columnas
df[['A','B']]
# Seleccionar por nombres con .loc() (basado en etiquetas)
df.loc[0:5, ['A','D']]
# Seleccionar por indices con .iloc() (basado en posiciones enteras)
df.iloc[0:5, 0:3]
````

- Filtrado condicional: 
Técnicas para extraer subconjuntos de datos que cumplen criterios específicos.
Ejemplo: filtrar filas donde una columna sea mayor a cierto valor.

````python
# Operadores: &(AND) ~(NOT)

# Condicion simple
df[df['A'] > 50]
# Varias condiciones
df[(df['A'] > 50) & (df['B'] < 20)]

````

## Limpieza y Transformación
- Gestión de valores nulos: 
Identificación y tratamiento de datos faltantes mediante .isnull(), .dropna() o .fillna().
````python
#Identificar valores nulos
df.isnull()
# Eliminar filas con valores nulos
df_sin_nulos = df.dropna()
# Rellenar valores nulos
df["Edad"] = df["Edad"].fillna(df["Edad"].mean())
df["Salario"] = df["Salario"].fillna(0)#rellena con 0
````

- Creación de nuevas columnas:
Cómo realizar operaciones aritméticas entre columnas existentes para generar nuevos indicadores.
````python
# Crear nueva columna con el total de ventas
df["Total_Venta"] = df["Precio"] * df["Cantidad"]

# Crear columna con impuesto
df["Impuesto"] = df["Total_Venta"] * 0.21
````
- Agrupamiento (Grouping): 
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



