# Set Matrix Zeroes

## Descripción

El ejercicio "Set Matrix Zeroes" plantea el reto de modificar una matriz de enteros de tamaño `m x n` directamente en memoria (in-place), de manera que si un elemento es 0, toda su fila y columna se conviertan en ceros. Esta transformación debe aplicarse sin crear una copia auxiliar de la matriz, lo que añade un componente de optimización espacial significativo al problema.

Este tipo de operación tiene aplicaciones prácticas en el tratamiento de datos tabulares y matrices de adyacencia, donde ciertos valores (como los ceros) pueden representar condiciones especiales que invalidan filas o columnas enteras.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que incluye el método `setZeroes`. El objetivo es identificar las filas y columnas que deben convertirse completamente en ceros y aplicar esta transformación directamente sobre la matriz de entrada, todo en espacio constante (O(1)), más allá del propio espacio de la matriz.

## Detalles de la implementación

- **Marcado con la primera fila y columna:** Se utiliza la primera fila y la primera columna como espacio auxiliar para almacenar qué filas y columnas deben ser convertidas en ceros. Este enfoque evita el uso de estructuras adicionales y cumple con la restricción de espacio constante.

- **Detección previa de ceros en la primera fila y columna:** Se comprueba si originalmente la primera fila o columna contienen ceros, ya que se utilizarán como marcadores y podrían sobrescribirse. Esta verificación previa permite aplicar correctamente la transformación final.

- **Transformación basada en marcadores:** Recorremos el resto de la matriz para aplicar ceros en las posiciones correspondientes, según los marcadores definidos en la primera fila y columna.

- **Aplicación final a la primera fila y columna:** Si la primera fila o columna contenían ceros originalmente, se transforman completamente en ceros.

## Uso

Para utilizar este código, simplemente se debe definir la matriz de entrada, y luego crear una instancia de la clase `Solution`. Se llama al método `setZeroes` pasando la matriz como parámetro, y la transformación se aplica directamente sobre la misma.

```python
if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]

    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]
```

## Conclusión

El ejercicio "Set Matrix Zeroes" representa un excelente ejemplo de cómo optimizar algoritmos para trabajar directamente sobre la estructura de datos original. La solución implementada no solo es eficiente en términos de complejidad temporal (O(m*n)), sino que también destaca por su uso de espacio constante, evitando cualquier estructura adicional salvo las variables auxiliares necesarias para el control del flujo. Este enfoque resulta especialmente útil en contextos donde el uso de memoria debe ser mínimo, como sistemas embebidos o entornos con restricciones de hardware.
