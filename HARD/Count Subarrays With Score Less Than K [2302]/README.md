# Count Subarrays With Score Less Than K

## Descripción

El ejercicio "Count Subarrays With Score Less Than K" tiene como objetivo contar el número de subarrays no vacíos dentro de un array de enteros positivos, cuya puntuación (score) sea estrictamente menor que un valor dado `k`.

La puntuación de un subarray se define como el producto entre la suma de sus elementos y la longitud del subarray. Esta operación es útil en contextos donde se desea evaluar tanto la magnitud total como la densidad de los valores de una subsecuencia, lo cual es frecuente en análisis de datos, segmentación de señales y problemas de optimización.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que expone el método `countSubarrays`. Este método emplea la técnica de **ventana deslizante (sliding window)** para recorrer el array de forma eficiente, evitando una solución ingenua basada en fuerza bruta que sería demasiado costosa computacionalmente.

### Detalles de la implementación

- **Inicialización de variables:** Se definen dos punteros `left` y `right` para controlar los límites de la ventana actual, además de una variable `window_sum` para mantener la suma de los elementos dentro de esa ventana.
- **Expansión de la ventana:** Se itera con el puntero `right` a través del array, agregando elementos a la suma.
- **Contracción de la ventana:** Si el score de la ventana (suma × longitud) es mayor o igual que `k`, se ajusta el límite izquierdo (`left`) para reducir el score.
- **Cálculo de subarrays válidos:** Para cada posición del puntero `right`, se calcula cuántos subarrays terminan en esa posición y cumplen la condición impuesta por `k`.

Este enfoque permite garantizar un tiempo de ejecución lineal, `O(n)`, lo cual es esencial dadas las restricciones del problema (hasta 10^5 elementos).

## Uso

Para utilizar este código, se debe instanciar la clase `Solution`, definir el array `nums` y el entero `k`, y luego llamar al método `countSubarrays` con estos parámetros.

```python
if __name__ == "__main__":
    nums = [2, 1, 4, 3, 5]
    k = 10

    sol = Solution()
    count = sol.countSubarrays(nums, k)
    print(count)  # Output esperado: 6
```

## Conclusión

El ejercicio "Count Subarrays With Score Less Than K" plantea un reto interesante al combinar conceptos de subarrays, suma acumulativa y condiciones de umbral sobre una métrica compuesta. La implementación mediante una ventana deslizante ofrece una solución eficiente y elegante, evitando los costes computacionales de algoritmos de fuerza bruta. Esta técnica es ampliamente aplicable a otros problemas de optimización y análisis en tiempo real sobre secuencias de datos.
