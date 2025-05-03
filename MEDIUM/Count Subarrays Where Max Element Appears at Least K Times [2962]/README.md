# Count Subarrays Where Max Element Appears at Least K Times

## Descripción

El ejercicio **"Count Subarrays Where Max Element Appears at Least K Times"** consiste en contar todos los subarrays contiguos de una lista de enteros `nums` donde el elemento máximo del array aparece al menos `k` veces. Esta tarea está orientada a trabajar con estructuras de ventanas deslizantes (sliding window) para identificar patrones específicos dentro de segmentos del array, un enfoque muy común en algoritmos de análisis de secuencias.

Un subarray es una secuencia contigua de elementos dentro de un array, y el objetivo es identificar cuántos de estos contienen el valor máximo con una frecuencia mínima determinada.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que incluye un método llamado `countSubarrays`. Este método aplica la técnica de **ventana deslizante** para recorrer el array eficientemente y contar cuántos subarrays cumplen con la condición establecida.

## Detalles de la implementación

- **Identificación del valor máximo:** Primero se calcula el valor máximo del array, ya que solo este valor es relevante para determinar los subarrays válidos.
- **Ventana deslizante:** Se utilizan dos punteros (`left` y `right`) para definir una ventana dentro del array. Esta ventana se expande a la derecha y se contrae desde la izquierda cuando se cumple la condición de que el valor máximo aparece al menos `k` veces.
- **Contador de apariciones:** Se mantiene un contador de cuántas veces ha aparecido el valor máximo dentro de la ventana actual.
- **Cálculo de subarrays válidos:** Cada vez que se encuentra una ventana donde el valor máximo aparece al menos `k` veces, se suman todos los subarrays que comienzan dentro de la ventana y terminan en o después del índice `right`.

## Uso

Para utilizar este código, se debe definir una lista de enteros `nums` y un valor entero positivo `k`. Luego, se crea una instancia de la clase `Solution` y se llama al método `countSubarrays` con los argumentos correspondientes.

```python
if __name__ == "__main__":
    nums = [1, 3, 2, 3, 3]
    k = 2

    sol = Solution()
    result = sol.countSubarrays(nums, k)
    print(result)  # Output: 6
```

## Conclusión

El ejercicio "Count Subarrays Where Max Element Appears at Least K Times" pone en práctica el uso de la técnica de ventana deslizante para resolver eficientemente un problema que, de otra forma, requeriría una exploración de todos los subarrays posibles de forma ineficiente. La implementación aprovecha la estructura del problema para evitar cálculos redundantes y mejorar el rendimiento. Este enfoque resulta especialmente útil cuando se trabaja con grandes volúmenes de datos o cuando se requiere una solución en tiempo lineal o casi lineal. Además, refuerza habilidades importantes como la identificación de condiciones de parada y la gestión de contadores dentro de ventanas dinámicas.
