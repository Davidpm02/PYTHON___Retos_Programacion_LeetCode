# Domino and Tromino Tiling

## Descripción

El ejercicio "Domino and Tromino Tiling" consiste en calcular el número total de formas posibles de cubrir completamente un tablero de tamaño 2×n utilizando dos tipos de fichas: el dominó (2×1) y el trominó en forma de L. Ambas fichas pueden rotarse en cualquier dirección, lo que permite múltiples configuraciones válidas de cobertura. Este problema pertenece a la categoría de programación dinámica y es un excelente ejemplo de cómo descomponer un problema complejo en subproblemas más pequeños.

El objetivo es determinar cuántas maneras distintas existen para embaldosar un tablero completo, asegurando que cada celda esté cubierta por exactamente una parte de alguna ficha. Dado que el número de soluciones puede ser muy grande, el resultado debe devolverse módulo 10⁹ + 7.

## Implementación

La solución está implementada en Python mediante una clase `Solution` que contiene el método `numTilings`. Este método aplica una estrategia de programación dinámica para calcular eficientemente la cantidad de formas de cubrir el tablero.

### Detalles de la implementación

- **Casos base:** Se inicializan los casos más simples (n = 1 y n = 2) de forma directa, ya que pueden evaluarse sin necesidad de recurrencia.
- **Estructura de DP:** Se utiliza una matriz `dp` donde `dp[i][j]` representa el número de formas de cubrir un tablero de tamaño 2×i con un estado específico en la última columna:
  - `dp[i][0]`: la columna i está completamente cubierta.
  - `dp[i][1]`: la columna i tiene únicamente la celda inferior sin cubrir.
  - `dp[i][2]`: la columna i tiene únicamente la celda superior sin cubrir.
- **Relaciones de recurrencia:** Para cada nuevo valor de `i`, se combinan los resultados anteriores con las posibles transiciones generadas por las fichas (dominó horizontal, vertical y trominó en sus variantes).
- **Modulo:** Todos los cálculos se realizan módulo 10⁹ + 7 para evitar desbordamientos y mantener la eficiencia.

## Uso

Para utilizar este código, basta con definir el valor de `n` (longitud del tablero), crear una instancia de la clase `Solution` y llamar al método `numTilings` para obtener el número de formas posibles de embaldosar el tablero.

```python
if __name__ == "__main__":
    n = 3

    sol = Solution()
    total_ways = sol.numTilings(n)
    print(total_ways)  # Output: 5
```

## Conclusión

El ejercicio "Domino and Tromino Tiling" es un caso clásico de programación dinámica que ilustra cómo modelar un problema espacial utilizando estados parciales y relaciones de recurrencia. La implementación aprovecha una estructura de matriz para registrar los posibles estados de cobertura de cada columna y, de ese modo, construir iterativamente la solución para valores crecientes de n. Esta técnica no solo es poderosa para este problema en particular, sino que también puede generalizarse a otros escenarios de embaldosado o cobertura parcial, lo cual la convierte en una herramienta esencial dentro del repertorio de cualquier desarrollador de algoritmos o ingeniero de Machine Learning.
