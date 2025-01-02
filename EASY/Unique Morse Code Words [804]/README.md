# Unique Morse Code Words

## Descripción

El ejercicio "Unique Morse Code Words" tiene como objetivo determinar el número de transformaciones únicas que pueden generarse al traducir una lista de palabras en sus representaciones correspondientes en código Morse. Cada letra del alfabeto inglés se asigna a una representación estándar de puntos y guiones, y la transformación de una palabra consiste en concatenar las representaciones Morse de todas sus letras. Este problema refuerza conceptos fundamentales de mapeo, conjuntos y manipulación de cadenas.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `uniqueMorseRepresentations`. Este método emplea estructuras de datos como diccionarios y conjuntos para mapear las letras a sus representaciones Morse y calcular las transformaciones únicas.

### Detalles de la implementación

- **Mapa de letras a código Morse:** Se utiliza un diccionario que relaciona cada letra del alfabeto inglés con su representación correspondiente en código Morse.
- **Cálculo de transformaciones únicas:** Para cada palabra en la lista dada, se genera su transformación Morse y se almacena en un conjunto, garantizando que las transformaciones repetidas no se cuenten varias veces.
- **Tamaño del conjunto:** El resultado final es el tamaño del conjunto, que representa el número de transformaciones únicas.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `uniqueMorseRepresentations` con una lista de palabras como argumento.

## Conclusión

El ejercicio "Unique Morse Code Words" proporciona una forma práctica de aplicar conceptos de programación como el mapeo de datos y el uso de estructuras de datos eficientes, como conjuntos, para resolver problemas de unicidad. La solución implementada es eficiente, clara y destaca por su utilización de las capacidades nativas de Python para trabajar con cadenas y colecciones. Este problema resulta particularmente útil para reforzar habilidades en manipulación de cadenas y estructuras de datos en Python.
