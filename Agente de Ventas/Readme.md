## Agente de Ventas
#### Paso 1: Crear los datos (CSV):
Crear un archivo ventas.csv con datos reales simulados.

#### Paso 2: Leer el CSV
Leer los datos del fichero ventas.csv
Convertir los datos leidos en estructura de datos(dataset) utilizando la libreria pandas.

#### Paso 3: Explorar los datos
Utilizar print() para mostrar los datos del dataset.

#### Paso 4: Definir una regla de decisión
Reglas:
1- Si vende menos que la media → promocionar
2- Si vende más que la media → mantener 

#### Paso 5: Crear la lógica del agente
Crear un fichero(src/testfunctions)
En el fichero crea una funcion(rule_promotion) que implemente las reglas definidas,
Llamar desde el agente(agent.ipynb) la funcion pasando como parametros el total_ventas y la media

#### Paso 6: Aplicar el agente a todos los datos
Add nueva columna al data frame llamada "decision", que se calcula a partir de la columna sales,
aplica a cada fila, coge el valor de sale y calcula si necesita promocion el producto
y el resultado lo va guardando en la nueva columna decision

#### Paso 7: Ver resultados
#### Paso 8: Guardar resultados (CSV)
Guardar los resultados en el fichero resultados.csv
