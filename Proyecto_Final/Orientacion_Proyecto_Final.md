
# Pandas & Data Visualization Project
- Nicolás Stambolsky
- Datos de entrega:
14 may, 
100 puntos,
Fecha de entrega: 21 may

# INSTRUCCIONES (Proyecto entregable)
- Este es el proyecto entregable del Máster en Data Science & AI.
- La entrega final será un repo/zip que presentaréis en clase el jueves 14 de mayo.
- Si no puedes asistir a la sesión de presentaciones, puedes subir el proyecto igualmente a la plataforma dentro del plazo indicado para que pueda corregirse.

# Qué es este ZIP
- El ZIP adjunto contiene una plantilla de proyecto para que trabajes con un dataset real en formato CSV y entregues un EDA reproducible.
- Tu tarea es:
  - Colocar tu CSV en data/raw/
  - Adaptar notebooks/eda.ipynb a las columnas de tu dataset
  - Aplicar limpiezas y transformaciones (tipos, nulos, categorías, duplicados)
  - Crear 2–3 features
  - Generar 4–6 visualizaciones con intención y buena presentación.
  - Además, completa README.md (objetivo, link del dataset, preguntas, pipeline y hallazgos) y modulariza parte del código en src/ (mínimo 3 funciones).
# Resumen
## Objetivo: 
- Usar esta plantilla para escoger tu propio dataset (.csv)
- Hacer un EDA reproducible
- Limpiar/transformar datos
- Añadir 2–3 features
- Crear visualizaciones y entregar un repo/zip con README
- Notebook ejecutable y código modular en src/.

# Qué debes modificar (mínimo)
Notebook notebooks/eda.ipynb:
- Cambiar la variable file_path en la sección “2.
- Cargar el archivo CSV” por la ruta a tu archivo (ej: data/raw/raw_dataset.csv)
- Revisar y descomentar/añadir líneas de ejemplo que usan columnas concretas (histogramas, boxplots, value_counts, scatter, crosstab) y adaptar nombres de columnas a tu CSV.
- src/config.py: actualizar RAW_PATH y OUT_PATH si usas nombres distintos (ej: raw_dataset.csv)
- requirements.txt: añadir librerías con versiones (automático con pip freeze > requirements.txt)
- data/processed/: comprobar que existe; main.py escribe aquí clean_dataset.csv por defecto

# Estructura esperada del proyecto (no cambiar salvo que sepas lo que haces)
main.py 
— entrypoint reproducible: load → clean → features → export → visualize
notebooks/eda.ipynb 
— orquesta el análisis y contiene la narración
src/ 
— funciones reutilizables: io.py, cleaning.py, features.py, viz.py, utils.py
data/raw/ 
— pon tu CSV aquí
data/processed/
— outputs exportables (no se suele commitear; puedes incluirlo en .gitignore)

## Pasos recomendados para ponerlo en uso
- Descomprimir y entrar en la carpeta del proyecto: cd project_demo
- Inicializar Git: git init
- Crear y activar entorno virtual:
Windows (PowerShell):python -m venv .venv
.venv\Scripts\activate
macOS / Linux:python3 -m venv .venv
source .venv/bin/activate
Instalar dependencias:
pip install -r requirements.txt
Actualizar dependencias si añades paquetes:
pip freeze > requirements.txt
(Opcional) usar .venv como kernel:
pip install ipykernel
python -m ipykernel install --user --name=project_demo_venv --display-name "Python (.venv)"
(Opcional) Ejecutar pipeline reproducible:
python main.py
Abrir el notebook:
jupyter notebook notebooks/eda.ipynb

Antes de entregar (revisa)
notebooks/eda.ipynb corre de principio a fin con tu CSV (rutas relativas)
src/ tiene al menos 3 funciones reales (ej: load_csv, clean, build_features, plot_*)
README.md completado (objetivo, link dataset, preguntas, pipeline, hallazgos)
requirements.txt contiene todas las dependencias necesarias
data/raw/mi_dataset.csv incluido o documentado en el README
data/processed/ outputs opcionales (recomendado en .gitignore)

Checklist de entrega mínima
README.md con objetivo, dataset, preguntas, pasos y conclusiones
notebooks/eda.ipynb ejecutable (rutas relativas)
src/ con al menos 3 funciones reales
4–6 gráficos con intención y buena presentación (título, ejes, interpretación)
3 conclusiones basadas en evidencia (referencia a gráfico/tabla)
Cosas que suman nota
Notebook orquestando + main.py ejecutable fuera del notebook
Validaciones simples en src/utils.py (ej: assert_columns)
Transformaciones no triviales (fechas robustas, normalización de categorías, outliers, pivots/agrupaciones)
Tests básicos o scripts de comprobación rápida
Guion orientativo para la presentación (4 minutos)
30s — Objetivo + dataset (link y por qué lo elegiste)
90s — Limpieza/transformaciones clave (problemas y solución; 1–2 snippets de Pandas)
90s — Visualizaciones (2–3) + lectura (2–3 insights)
30s — Conclusiones + siguientes pasos
Consejos prácticos
Usa rutas relativas (data/raw/mi_dataset.csv)
Evita rutas absolutas en el notebook
Activa .venv antes de instalar/ejecutar
Documenta cambios de columnas (rename/drop) con Markdown en el notebook
Si el CSV es enorme, desarrolla con muestra y deja instrucciones en el README para ejecutar completo
