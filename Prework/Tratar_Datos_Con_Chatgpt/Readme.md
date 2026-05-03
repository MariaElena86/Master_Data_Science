1. Preparar y tratar los datos

Para empezar, nos descargamos varios ficheros de datos en bruto desde la web del operador del mercado eléctrico. Estos ficheros contenían datos de energía comprada y vendida, organizados de manera poco estructurada, con cabeceras confusas, errores, horas duplicadas e incluso días faltantes. Aquí es donde ChatGPT entra en acción.

Le dimos a ChatGPT unas instrucciones claras (a esto lo llamamos “prompting”), explicándole qué queríamos hacer:





Leer los datos.



Corregir errores de formato.



Detectar problemas (días con horas incompletas, días ausentes o valores atípicos).



Crear una serie temporal diaria, organizada y limpia.

Con estas instrucciones, ChatGPT no solo entendió el problema, sino que empezó a generar las primeras soluciones. Por ejemplo, corrigió cabeceras, limpió datos incompletos y estandarizó formatos.

💡 Nota importante: Aunque ChatGPT hace gran parte del trabajo, debemos supervisar siempre lo que genera. En varios puntos encontramos pequeños errores que corrigimos ajustando nuestras instrucciones.

2. Automatizar el proceso: hacia un robot de datos

Uno de los puntos más interesantes fue cuando decidimos automatizar todo el flujo de trabajo. ChatGPT generó código en Python para:





Procesar nuevos datos: Es decir, añadir nuevos días de información al dataset existente.



Descargar ficheros automáticamente: Ya no era necesario descargar manualmente cada fichero. Creamos un script que se conectaba a la web, descargaba los datos y los incorporaba al archivo final.

Por ejemplo, para los días en los que faltaban datos, usamos una técnica muy útil: la interpolación. Esto significa rellenar los huecos estimando valores basados en los días anterior y posterior. ChatGPT incluso nos generó gráficas para visualizar cómo quedaban los datos interpolados, lo cual nos permitió verificar que todo tenía sentido.

3. Validar la calidad de los datos

Aquí hicimos varias comprobaciones:





Revisamos que no hubiera valores “extraños” como ceros o datos nulos.



Verificamos que todos los días del rango temporal estuvieran presentes.



Comprobamos que los datos estuvieran correctamente alineados por horas (por ejemplo, gestionando días con 23 o 25 horas debido a cambios de horario).

Cada vez que encontrábamos algo fuera de lo normal, volvíamos a ajustar nuestras instrucciones a ChatGPT. El resultado fue un dataset limpio, fiable y listo para ser usado.

4. El resultado: un robot que ahorra horas de trabajo

Finalmente, creamos un pequeño robot automatizado que:





Se conecta a la web, detecta los ficheros nuevos y los descarga.



Procesa estos datos siguiendo las mismas reglas de limpieza que habíamos diseñado.



Actualiza el dataset con los nuevos datos, sin que tengamos que intervenir más.

Todo este proceso, que podría habernos llevado días de trabajo manual, lo completamos en menos de una hora gracias a ChatGPT. Y lo mejor es que ahora está totalmente automatizado.