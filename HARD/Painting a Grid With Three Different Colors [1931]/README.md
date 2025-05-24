# Painting a Grid With Three Different Colors

## Descripción

El ejercicio **"Painting a Grid With Three Different Colors"** plantea el reto de contar el número total de formas en que se puede pintar una cuadrícula de tamaño `m x n` usando exactamente tres colores (rojo, verde y azul), cumpliendo la restricción de que **no haya celdas adyacentes con el mismo color**, ya sea en sentido horizontal o vertical.

Este problema se enmarca dentro del ámbito de la programación dinámica combinatoria y la teoría de grafos, y es representativo de problemas donde se deben explorar múltiples configuraciones posibles bajo restricciones estrictas de adyacencia.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `colorTheGrid(m: int, n: int) -> int`. La estrategia utilizada combina la **generación de patrones válidos de colores por columna** junto con **programación dinámica con memoización** para evitar cálculos repetidos.

### Detalles de la implementación

- **Colores y patrones válidos:** Se consideran 3 colores (rojo, verde y azul, representados por 0, 1 y 2). Se generan todos los patrones válidos posibles de altura `m` que no tengan colores adyacentes iguales en la misma columna.
- **Compatibilidad entre columnas:** Se preprocesan las combinaciones de columnas válidas que pueden estar una junto a otra, asegurando que las celdas correspondientes entre columnas adyacentes también tengan colores distintos.
- **Programación dinámica (DP):** Se define una función recursiva con memoización (`@lru_cache`) que evalúa todas las posibilidades de construir la cuadrícula columna por columna. El estado de la DP se define por el índice de la columna actual y el patrón utilizado en la columna anterior.
- **Caso base:** Para la primera columna se puede elegir libremente cualquier patrón válido. A partir de ahí, se calculan las formas posibles de expandir la cuadrícula respetando las restricciones de compatibilidad entre columnas.

## Uso

Para utilizar este código, simplemente se debe instanciar la clase `Solution` y llamar al método `colorTheGrid` con los valores deseados de `m` y `n`, que representan las dimensiones de la cuadrícula.

```python
if __name__ == "__main__":
    m = 3
    n = 4

    sol = Solution()
    total_ways = sol.colorTheGrid(m, n)
    print(total_ways)
```

## Conclusión

El ejercicio "Painting a Grid With Three Different Colors" representa un interesante desafío computacional donde se combinan técnicas de backtracking, preprocesamiento de estados válidos y programación dinámica optimizada. Este enfoque permite escalar eficientemente incluso cuando n es grande (hasta 1000), manteniendo la complejidad bajo control gracias al uso de memoización. El problema es útil para afianzar conceptos avanzados en resolución de problemas con restricciones, gestión eficiente de estados y técnicas de optimización en algoritmos.
