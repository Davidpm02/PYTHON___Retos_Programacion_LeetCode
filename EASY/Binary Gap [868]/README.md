# Number of Lines To Write String

## Descripción

El ejercicio "Number of Lines To Write String" tiene como objetivo determinar la distancia máxima entre cualquier par de bits `1` adyacentes en la representación binaria de un número entero positivo dado. La distancia entre dos bits `1` es la diferencia absoluta de sus posiciones en la representación binaria. Si no existen dos bits `1` adyacentes, el resultado debe ser `0`. Este problema explora conceptos relacionados con la manipulación de datos binarios y el cálculo de posiciones en una secuencia.

## Implementación

La solución se desarrolla en Python mediante una clase `Solution` que implementa el método `binaryGap`. Este método analiza la representación binaria de un número entero para encontrar la máxima distancia entre bits `1` adyacentes.

### Detalles de la implementación

- **Conversión a binario:** Se obtiene la representación binaria del número usando la función `bin()`, eliminando el prefijo `0b` que indica números binarios.
- **Comprobación inicial:** Si no hay suficientes bits `1` para formar pares, se retorna directamente `0`.
- **Cálculo de la distancia máxima:** Se recorre la representación binaria del número, calculando la distancia entre bits `1` y actualizando el valor máximo encontrado.
- **Estructuras de datos:** El método utiliza listas para manejar los bits y cálculos iterativos para determinar las distancias.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `binaryGap` con un número entero como argumento.

## Conclusión

El ejercicio "Number of Lines To Write String" presenta una solución eficiente para calcular distancias en representaciones binarias, destacando el uso de estructuras de control iterativas y el manejo de listas. La implementación propuesta es clara y efectiva, abordando de manera precisa los casos base y proporcionando un enfoque escalable para problemas similares. Este ejercicio resulta ideal para profundizar en técnicas de manipulación de datos binarios y optimización de recorridos en secuencias.
