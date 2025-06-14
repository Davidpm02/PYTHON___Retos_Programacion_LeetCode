# Minimize the Maximum Difference of Pairs

## Descripción

El ejercicio "Minimize the Maximum Difference of Pairs" consiste en formar `p` pares de índices a partir de un array de enteros, de modo que la diferencia absoluta máxima entre los valores emparejados sea la menor posible. Además, cada índice del array solo puede utilizarse en un único par. El objetivo es devolver esta mínima diferencia máxima posible.

Este problema tiene aplicaciones relevantes en áreas donde se requiere agrupar elementos de forma balanceada o minimizar el desequilibrio entre pares, como en la asignación de recursos, emparejamiento de tareas o clustering básico con restricciones.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` que contiene el método `minimizeMax`. Este método sigue una estrategia basada en **búsqueda binaria** combinada con **técnicas greedy**, lo que permite una solución eficiente para grandes volúmenes de datos.

## Detalles de la implementación

- **Ordenación previa del array:** Comienzo ordenando el array `nums` para facilitar la formación de pares con diferencias mínimas entre elementos consecutivos.

- **Función auxiliar `can_form_pairs`:** Esta función evalúa si es posible formar al menos `p` pares cuya diferencia entre elementos no supere un umbral `max_diff`. Para ello:
  - Itero el array de izquierda a derecha.
  - Si la diferencia entre un par consecutivo es válida, lo cuento y avanzo dos posiciones para evitar solapamientos.
  - Si no lo es, simplemente avanzo una posición.

- **Búsqueda binaria:** Aplico búsqueda binaria sobre el rango de posibles diferencias (desde 0 hasta la diferencia máxima en el array ordenado), utilizando `can_form_pairs` como criterio de decisión para acotar el espacio de búsqueda. De esta forma:
  - Si es posible formar los pares con una diferencia `mid`, intento buscar una diferencia menor.
  - Si no es posible, aumento el rango de búsqueda.

Esta estrategia garantiza una complejidad eficiente en tiempo: **O(n log(max_diff))**, donde `n` es la longitud del array.

## Uso

Para utilizar este código, se debe definir un array de enteros `nums` y un entero `p` que representa la cantidad de pares requeridos. Luego, se instancia la clase `Solution` y se invoca el método `minimizeMax`, el cual devolverá la diferencia máxima mínima entre los pares seleccionados.

```python
if __name__ == "__main__":
    nums = [10, 1, 2, 7, 1, 3]
    p = 2

    sol = Solution()
    resultado = sol.minimizeMax(nums, p)
    print(resultado)
```

## Conclusión

El ejercicio "Minimize the Maximum Difference of Pairs" propone un desafío clásico de optimización combinatoria con restricciones, que puede resolverse eficientemente gracias a una combinación de búsqueda binaria y un enfoque greedy para validación. Esta solución no solo minimiza el coste computacional, sino que también ilustra cómo estructurar algoritmos eficientes en problemas de emparejamiento bajo restricciones. Es una excelente práctica para desarrollar habilidades en diseño algorítmico y análisis de complejidad.
