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
Utilizar print para mostrar los datos del data frame con la nueva columna 

#### Paso 8: Guardar resultados (CSV)
Guardar los resultados en el fichero resultados.csv


## Convertir el agente en un agente predictivo usando la libreria scikit-learn
Hacer que el modelo aprenda con estos patrones: "Conviene promocionar un producto o no."

#### 1. Crear lo que el modelo debe aprender a predecir.
df["decision"] = df["total_sale"].apply(lambda x: 1 if x > 100 else 0)
Donde 1 = “buena venta” y 0 = “mala venta”

#### 2. Preparar los datos para entrenar el modelo: X e y (lo más importante de todo ML)
  Donde: 
    - X: son las variables de entrada (features, o sea los datos que el modelo usa para aprender) 
    - y: es lo que quieres predecir(o sea es la “respuesta correcta”)

#### 3. Usar la funcion "train_test_split" para  dividir los datos en entrenamiento y prueba
  - TRAIN (los datos de entrenamiento, representa el 80% ) es con lo que aprende el modelo.
  - TEST (los datos de prueba, representa el 20%) es donde se evalua el modelo

 Ejemplo Si tienes 100 filas: 
 80 filas → se usan para entrenamiento y 20 → prueba

#### 4- Preparar datos para IA
  X = df[["price", "stock", "total_sale"]]
  y = df["decision"]

 - Salida de la funcion train_test_split
   X_train  # datos de entrada para entrenar
   X_test   # datos de entrada para probar
   y_train  # resultados correctos para entrenar
   y_test   # resultados correctos para evaluar

#### 5. Crear el modelo
 Usar el modelo RandomForestClassifier de scikit-learn,

#### 6- Entrenar el modelo
   - Decirle al modelo que aprenda con  modelo.fit(X_train, y_train)
     
#### 7- Evaluar el modelo
   - Calcular  usando accuracy = aciertos / total, para medir el rendimiento del modelo
   - La funcion accuracy_score mide cuantas predicciones fueron correctas, accuracy_score(y_test, predicciones))
   - Ejemplo:
     Es como un examen donde:predicciones → son tus respuestas, y_test → son las respuestas correctas y accuracy → es la nota del examen

#### 8- Usar el agente predictivo
  - Usar la funcion predict() que te dice qué tan bueno es el agente, df["prediccion"] = modelo.predict(X)
  - Si el resultado Accuracy = 0.85, significa que el modelo acierta el 85% de las veces 

