# Positions of Large Groups

## Descripción

El ejercicio "Positions of Large Groups" consiste en identificar y devolver los intervalos de los llamados "grupos grandes" dentro de una cadena de caracteres. En este contexto:

- Una **cadena** es un conjunto de caracteres en minúscula del alfabeto inglés.
- Un **grupo** se define como una secuencia consecutiva de caracteres idénticos.
- Un **grupo grande** es aquel cuya longitud es mayor o igual a 3.

El objetivo es encontrar los grupos grandes dentro de la cadena, devolver sus intervalos en forma de listas `[inicio, fin]`, y ordenarlos según el índice de inicio.

## Implementación

La implementación se realiza en Python, utilizando una clase llamada `Solution` que contiene el método `largeGroupPositions`. Este método aplica los pasos necesarios para analizar la cadena, identificar los grupos consecutivos, y filtrar aquellos que cumplen con el criterio de ser grupos grandes.

### Detalles de la implementación

1. **Identificación de puntos de inicio:** Se genera una lista que almacena los índices iniciales de cada grupo detectado dentro de la cadena.
2. **Creación de grupos consecutivos:** La lista de caracteres se procesa para fusionar los caracteres consecutivos idénticos en un único grupo.
3. **Identificación de grupos grandes:** Los grupos cuya longitud sea mayor o igual a 3 son transformados en un intervalo `[inicio, fin]`.
4. **Construcción del resultado:** El método devuelve la lista de intervalos ordenados según el índice de inicio.

## Conclusión

El ejercicio "Positions of Large Groups" ofrece una oportunidad de practicar el procesamiento y análisis de cadenas, además de conceptos como la creación y manipulación de listas en Python. Este tipo de problemas refuerza habilidades esenciales como la iteración, el manejo de condiciones y la segmentación de datos. La solución presentada es eficiente y funcional, diseñada específicamente para detectar intervalos de grupos grandes de manera ordenada.
