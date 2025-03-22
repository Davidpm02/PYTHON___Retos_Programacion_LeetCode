# Longest Nice Subarray

## Descripción

El ejercicio "Longest Nice Subarray" consiste en encontrar la longitud del subarray más largo dentro de un array de enteros positivos que cumpla con una condición específica: el resultado de la operación AND bit a bit entre cualquier par de elementos distintos dentro del subarray debe ser igual a 0. En otras palabras, los elementos del subarray no deben compartir bits en común cuando se representan en binario.

Este problema está relacionado con la manipulación de bits y la optimización mediante estructuras de datos eficientes para verificar condiciones en tiempo real.

## Implementación

La solución implementa un enfoque de "ventana deslizante" (sliding window) para optimizar la búsqueda del subarray más largo que cumpla la condición dada. La estrategia utilizada es la siguiente:

- Se mantiene una máscara de bits (`bit_mask`) que representa los números actualmente incluidos en la ventana.
- Se usan dos punteros (`left` y `right`) para definir los límites de la ventana deslizante.
- A medida que se expande la ventana agregando elementos a la derecha, se verifica si el nuevo número agregado cumple con la condición del AND bit a bit.
- Si en algún momento la condición no se cumple, se mueve el puntero izquierdo (`left`) eliminando elementos hasta restaurar la validez de la ventana.
- Se mantiene un registro de la longitud máxima del subarray válido encontrado.

## Uso

Para utilizar este código, se debe instanciar la clase `Solution` y llamar al método `longestNiceSubarray`, proporcionando un array de enteros positivos como entrada.

```python
if __name__ == "__main__":
    nums = [1, 3, 8, 48, 10]
    
    sol = Solution()
    result = sol.longestNiceSubarray(nums)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Longest Nice Subarray" es un excelente ejemplo del uso de la técnica de "ventana deslizante" combinada con operaciones bit a bit para optimizar el cálculo en problemas de secuencias. La solución implementada logra un tiempo de ejecución eficiente, ya que cada elemento del array se procesa en promedio una vez, logrando una complejidad temporal cercana a O(n). Este problema es útil para mejorar la comprensión de operaciones bit a bit y estructuras de datos dinámicas aplicadas a la resolución de problemas algorítmicos.
