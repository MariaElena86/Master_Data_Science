En esta clase aprenderemos a usar Power BI, una herramienta de Microsoft diseñada para transformar datos en información clara y visual. ¿Alguna vez has trabajado con Excel y has sentido que necesitabas algo más visual, dinámico o automatizado? Power BI es como un Excel mejorado, hecho para analizar y compartir datos de forma más eficiente.

¿Qué es Power BI y por qué es tan importante?

Power BI es una herramienta de análisis de datos que convierte datos crudos en información significativa a través de gráficos interactivos, dashboards y paneles visuales. Su objetivo es democratizar el análisis de datos, es decir, que incluso quienes no son expertos puedan entender y usar los datos para tomar decisiones.

Por ejemplo:





Si tienes datos de ventas, Power BI te permite crear un gráfico donde, de un vistazo, puedas ver qué producto se vende más y en qué región.



Si diriges una campaña publicitaria, podrías conectar los datos de visitas web y CRM para ver los resultados de forma clara y atractiva.

¿Por qué deberíamos aprender Power BI?





Facilidad de uso: Su interfaz es intuitiva y accesible para principiantes.



Conexión con múltiples fuentes: Desde bases de datos hasta archivos de Excel o servicios en la nube.



Análisis en tiempo real: Ideal para tomar decisiones basadas en datos que se actualizan constantemente.



Integración con Office: Si tu empresa usa Microsoft (Outlook, SharePoint), todo está conectado.



Precio accesible: Comparado con otras herramientas como Tableau o QlikView, Power BI es más económico.

Primeros pasos con Power BI

1. Instalación





Usuarios de Windows: Descarga Power BI Desktop desde el sitio oficial de Microsoft.



Usuarios de Mac: Necesitarás instalar una máquina virtual, como Parallels Desktop, para simular Windows dentro de tu Mac. Así podrás usar Power BI Desktop sin problemas.

💡 Pro tip: Si tienes dudas sobre cómo instalarlo en Mac, puedes buscar una guía o incluso preguntar en ChatGPT.

Componentes principales de Power BI

Cuando abras Power BI por primera vez, verás varias áreas importantes. Es como aprender a usar una nueva herramienta; primero exploraremos cada parte:





Vista de Informe: Es donde crearás gráficos y dashboards. Aquí plasmarás tus ideas visuales.



Vista de Tabla: Muestra los datos como si fuera Excel, con filas y columnas.



Vista de Modelo: Aquí defines relaciones entre las tablas, como si unieras piezas de un rompecabezas.



Panel de Visualizaciones: A la derecha, tendrás gráficos listos para usar, como barras, líneas, mapas, etc.



Cinta de opciones: Similar a Excel, aquí encontrarás funciones como "Insertar" o "Modelar".

Nuestro primer ejercicio práctico: Ganadores de la Champions League

Vamos a trabajar con un ejemplo real para hacerlo más divertido. Imagina que tienes datos sobre los ganadores de la Champions League de los últimos 20 años y quieres analizarlos en Power BI.

1. Carga de datos





Prepara un archivo Excel con columnas como:





Año.



Equipo ganador.



Goles en la final.



País de origen del equipo.



Estadio de la final.



En Power BI, ve a la pestaña Inicio y haz clic en Obtener datos. Selecciona Excel, carga el archivo y revisa las columnas.

2. Creación de tu primer gráfico





En la Vista de Informe, selecciona el gráfico de barras (horizontal o vertical) desde el Panel de Visualizaciones.



Arrastra Equipo ganador al eje Y (vertical) y Goles en la final al eje X (horizontal).



¡Listo! Ahora puedes ver cuántos goles ha marcado cada equipo ganador en la final.

💡 Tip: Si cambias los datos en el archivo original, Power BI puede actualizar automáticamente los gráficos.

3. Agregar un filtro interactivo

Queremos poder filtrar los resultados por año. Haz lo siguiente:





En el Panel de Visualizaciones, selecciona el icono de Segmentación de datos.



Arrastra la columna Año al filtro.



Aparecerá un control deslizante que te permitirá filtrar los datos de un rango de años específico.

Por ejemplo: filtra solo los últimos 10 años y observa cómo cambia el gráfico automáticamente.

4. Personalización de gráficos





Colores y etiquetas: En el panel de visualizaciones, cambia colores, títulos y fuentes para personalizar tu gráfico.



Tipos de gráficos: ¿Prefieres un gráfico de anillos o líneas? Cambia el tipo con un clic y experimenta.

¿Cómo conecta Power BI con los datos?

Power BI tiene dos modos principales de conexión:





Modo Importación: Trae los datos al archivo local, ideal para análisis pequeños y rápidos.



Direct Query: Consulta directamente en la base de datos original, perfecto para grandes volúmenes de datos o informes en tiempo real.

💡 Recuerda:





Si los datos cambian con frecuencia, usa Direct Query.



Si trabajas offline o necesitas un análisis exploratorio, usa Importación.

Transformaciones básicas con Power Query

Antes de analizar los datos, es fundamental limpiarlos. Imagina que Power Query es como un editor de datos:





Eliminar columnas no necesarias: Si una columna no aporta valor, elimínala.



Renombrar columnas: Dale nombres claros a las columnas.



Filtrar filas: ¿Quieres analizar solo los equipos españoles? Filtra los datos antes de visualizarlos.

Ejemplo práctico:





Filtra solo los años en los que ganó un equipo inglés.



Renombra la columna "Equipo ganador" a "Equipo campeón".



Elimina la columna "Estadio de la final" si no es relevante.

Cuando termines, haz clic en Cerrar y aplicar. Power BI guardará los cambios y podrás trabajar con el nuevo set de datos.