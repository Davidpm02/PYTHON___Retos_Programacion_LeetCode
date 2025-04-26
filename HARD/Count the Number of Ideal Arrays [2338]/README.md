# Count the Number of Ideal Arrays

## Descripción

El ejercicio "Count the Number of Ideal Arrays" consiste en calcular cuántos arrays ideales de longitud `n` se pueden formar, considerando valores entre 1 y `maxValue`. Un array se considera ideal si cumple dos condiciones: cada elemento está en el rango [1, maxValue] y cada elemento es divisible por el anterior. Dado que el número de arrays puede ser muy grande, el resultado se devuelve módulo 10⁹ + 7. Este tipo de problema combina técnicas de combinatoria, programación dinámica y teoría de números, resultando en una excelente práctica para optimizar soluciones sobre grandes dominios de datos.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `idealArrays`. La estrategia adoptada combina precálculo de combinaciones, programación dinámica para secuencias multiplicativas y una técnica de "estrellas y barras" para distribuir los valores a lo largo del array.

## Detalles de la implementación

- **Precálculo de factoriales e inversos:** Se calcula el factorial y su inverso modular para agilizar el cálculo de combinaciones \( C(a, b) \).
- **Programación dinámica (dp):** Se utiliza una tabla `dp[i][l]` para almacenar la cantidad de secuencias de longitud `l+1` que terminan en el valor `i`.
- **Construcción de secuencias:** A partir de cada número `i`, se propagan las posibilidades a sus múltiplos para construir las secuencias.
- **Combinaciones:** Se combina cada secuencia válida con el número de formas posibles de distribuir incrementos en el array utilizando la fórmula combinatoria de estrellas y barras.
- **Módulo:** Todas las operaciones se realizan módulo 10⁹ + 7 para evitar desbordamientos de enteros.

## Uso

Para utilizar este código, basta con crear una instancia de la clase `Solution` y llamar al método `idealArrays` pasando los valores deseados de `n` y `maxValue`.

```python
if __name__ == "__main__":
    n = 2
    maxValue = 5

    sol = Solution()
    result = sol.idealArrays(n, maxValue)
    print(result)  # Output: 10
```

## Conclusión

El ejercicio "Count the Number of Ideal Arrays" demuestra cómo la combinación de técnicas avanzadas de combinatoria y programación dinámica puede resolver problemas de conteo en espacios de búsqueda extremadamente grandes de manera eficiente. El uso de precálculo de factoriales y el aprovechamiento de propiedades divisibles permiten optimizar el proceso, evitando soluciones de fuerza bruta que serían computacionalmente inviables. Esta implementación refuerza habilidades esenciales para abordar desafíos algorítmicos de alto nivel, muy comunes en competencias y aplicaciones reales donde el rendimiento es crítico.
