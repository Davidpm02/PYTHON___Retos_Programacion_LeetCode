# Find Pivot Index

## Descripción

El ejercicio "Find Pivot Index" consiste en determinar el índice de un arreglo `nums` de enteros donde la suma de todos los elementos a la izquierda del índice sea igual a la suma de todos los elementos a su derecha. 

Si el índice se encuentra al borde izquierdo del arreglo, se considera que la suma izquierda es `0`. Lo mismo ocurre si el índice está al borde derecho: en ese caso, la suma derecha es `0`. El objetivo es devolver el índice más a la izquierda que cumpla esta condición. Si no existe tal índice, se retorna `-1`.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `pivotIndex`. Este método recorre el arreglo `nums` para calcular las sumas izquierda y derecha en cada índice, verificando si satisfacen la condición del índice pivote.

### Detalles de la implementación

- **Iteración:** Se recorre el arreglo `nums` evaluando las sumas de los subarreglos a la izquierda y derecha del índice actual.
- **Cálculo de sumas:** Se utilizan operaciones de corte (`slice`) para calcular dinámicamente las sumas izquierda y derecha para cada índice.
- **Devolución del índice:** Se retorna el primer índice donde las sumas coinciden. Si ningún índice cumple la condición, se devuelve `-1`.

## Uso

Para utilizar este código, define una lista de números nums e instancia la clase Solution. Luego, llama al método pivotIndex pasando el arreglo como parámetro. La función devolverá el índice pivote más a la izquierda o -1 si no existe ningún índice que cumpla la condición.

```python
if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    print(solution.pivotIndex(nums))  # Devuelve: 3
```

## Conclusión

El ejercicio "Find Pivot Index" aborda un problema típico de equilibrio y optimización en arreglos unidimensionales. Esta implementación es clara y eficiente, evaluando dinámicamente las sumas izquierda y derecha mediante iteración. El ejercicio es útil para fortalecer habilidades en manipulación de datos, cortes de arreglos y lógica algorítmica, con aplicaciones prácticas en el procesamiento de datos y análisis estadístico.
