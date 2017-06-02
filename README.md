# Práctica: MongoDB + Pymongo #

- **Facilitador:** [Leonardo Kuffo](https://github.com/lkuffo/)
- **Fecha:** 6/02/2017

## Descripción ##

En este taller aprendimos como trabajar con MongoDB y utilizar MongoDB desde Python utilizando el Plugin Pymongo. Para afianzar los conocimientos aprendidos y aprender el manejo de Pymongo se propone la practica aqui expuesta.

## Dataset ##

[El Dataset](https://think.cs.vt.edu/corgis/json/airlines/airlines.json) que vamos a utilizar (**airlines.json**) tiene informacion correspondiente a reportes mensual de vuelos de aeropuertos de todos los Estados Unidos divididos por Aerolinea ocurridos entre 2003 y 2016. En este DataSet encontraremos informacion como:
- Aeropuerto del Reporte (Código y nombre completo)
- Estadisticas de Vuelos (Numero de vuelos cancelados, a tiempo, totales, atrasados, temperatura, tiempo de atraso)
- Fecha del Reporte (Year y mes)
- Aerolinea (Código y nombre completo)

## Práctica ##

Para la realización de la practica se le ha proporcionado un script incompleto (**practicamongo.py**) el cual usted tendra que completar respondiendo a las siguientes preguntas:

### ¿Cuántos documentos existen en total en la coleccion? ###
### ¿Cuántos aeropuertos hay entre todos los reportes? ###
### ¿Cuántos vuelos en los aeropuertos de Miami ("code": "MIA") estuvieron retrasados (delayed)? ###
### ¿En qué mes de todos los anios en todos los aeropuertos se cancelaron (canceled) mas vuelos? ###
### ¿Qué aerolinea tuvo más vuelos atrasados? (delayed) ###

**Tiempo Estimado: 30 minutos**

## Tips ##

- Recuerde que esta programando en Python. Las respuestas no necesariamente tienen que venir de una consulta de Mongo. Puede utilizar tecnicas de programacion para encontrar las respuestas.
- Suerte!

