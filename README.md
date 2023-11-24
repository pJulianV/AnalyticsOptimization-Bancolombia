# AnalyticsOptimization-Bancolombia


Objetivo: 
Generarás Informes personalizados para cada uno de los usuarios con sobre el consumo que hacen sobre la plataforma, su comparación con otros equipos y que impacto están generando a la 
plataforma. Para esto es necesario utilizar SQL, Python para consumir los querys ejecutados por los usuarios, la generación de estadísticas (SQL) y Python para la generación automatización y envió de los informes y reportes. Ademas se busca generar un modelo analitico que analice los querys lanzados por cada uno delos usuarios y genre un indicador de similitud con otros querys lanzados por el mismo usuario, para concluir por usuario si esta haciendo un mal uso de plataforma.


Para esto tenemos un repositorio muy util: https://github.com/Sven-Bo/PDF-Report-Generator-Using-Python-and-SQL
Su respectivo video: https://www.youtube.com/watch?v=LQywWpDoH9s&ab_channel=CodingIsFun
y su web: https://sqliteviewer.app/

En este proyecto se enfatiza Creacion de Reportes PDF con SQL + Python



1. Conectar a la base de datos: Utiliza una biblioteca como psycopg2 para conectarte a la base de datos PostgreSQL en Python

2. Ejecutar consultas: Ejecuta consultas SQL para obtener los datos necesarios, como el consumo de usuarios y las comparaciones con otros equipos

sql
SELECT user_id, query, date, consumption
FROM analytics_data;

3. Crear informes y reportes: Utiliza bibliotecas como ReportLab o PyPDF2 para crear informes y reportes en Python.
A continuación, se muestra un ejemplo de cómo crear un informe PDF utilizando "ReportLab":


4. Generar informes personalizados: Utiliza SQL y Python para generar informes personalizados para cada usuario, comparando su consumo en la plataforma con otros equipos y evaluando el impacto que generan

 
5. Modelo analítico: Desarrolla un modelo analítico que analice los queries lanzados por cada usuario y genere un indicador de similitud con otros queries lanzados por el mismo usuario, para determinar si están haciendo un mal uso de la plataforma


6. Automatizar y enviar informes y reportes: Utiliza Python y SQL para automatizar el proceso de generación e envío de informes y reportes, como en el ejemplo de automatizar la generación de informes desde una base de datos SQL utilizando Python

