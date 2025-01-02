# Binary Gap

## Descripción

El ejercicio "Binary Gap" consiste en encontrar y devolver la distancia más larga entre dos 1's adyacentes en la representación binaria de un número positivo `n`. Si no hay dos 1's adyacentes, el resultado debe ser 0.

Para este ejercicio, dos 1's se consideran adyacentes si están separados únicamente por 0's, es decir, sin ningún 1 entre ellos (o incluso sin 0's entre ellos). La distancia entre dos 1's se calcula como la diferencia absoluta entre sus posiciones en la representación binaria.

## Implementación

La implementación se lleva a cabo en Python mediante el método `binaryGap`, que recibe como parámetro un número entero `n` y devuelve la distancia máxima entre dos 1's adyacentes en su representación binaria.

### Detalles de la implementación

1. **Conversión binaria:** Primero, el número `n` se convierte a su representación binaria usando la función `bin(n)`. Posteriormente, se eliminan los primeros dos caracteres "0b" que indican la base binaria en Python.

2. **Verificación de 1's adyacentes:** La implementación recorre los bits de la representación binaria. Si encuentra un 1, comienza a contar la distancia hacia el siguiente 1. Cuando encuentra un 1 adyacente, actualiza el valor de la distancia máxima.

3. **Resultado final:** Si no se encuentran 1's adyacentes, el valor de la distancia máxima será 0, y se retorna ese valor.

## Conclusión

El ejercicio "Binary Gap" proporciona una forma eficiente de calcular la distancia máxima entre dos bits 1 adyacentes en la representación binaria de un número. Este tipo de operaciones es útil al trabajar con manipulación de bits en computación y optimización de operaciones numéricas. La implementación recursiva y el uso de una simple iteración sobre los bits del número hacen que la solución sea comprensible y eficiente en cuanto al tiempo de ejecución. Este tipo de problema refuerza conceptos sobre manipulación de bits, representaciones numéricas y la conversión entre diferentes bases.
