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