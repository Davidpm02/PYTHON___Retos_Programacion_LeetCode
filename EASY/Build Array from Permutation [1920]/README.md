# Build Array from Permutation

## Descripción

El ejercicio **"Build Array from Permutation"** consiste en construir un nuevo array a partir de una permutación dada de índices. El objetivo es generar un nuevo array `ans`, tal que para cada posición `i`, se cumpla la condición: `ans[i] = nums[nums[i]]`. Esta operación se basa en la composición de índices y es un buen ejemplo de acceso indirecto a estructuras de datos, un patrón común en problemas algorítmicos y manipulación de listas.

Una permutación basada en cero es una lista de enteros distintos que van desde 0 hasta `n - 1`, donde `n` es la longitud del array. Este tipo de problema ayuda a entender mejor el concepto de acceso posicional y la forma en la que los índices pueden ser utilizados como valores para redireccionar accesos dentro de una misma lista.

## Implementación

La solución se implementa en Python dentro de una clase `Solution` que contiene el método `buildArray`. Este método recibe una lista de enteros `nums` y construye el nuevo array `ans` conforme a la regla definida.

### Detalles de la implementación

- **Inicialización del array resultado:** Se crea una lista vacía `result` para almacenar el nuevo array.
- **Iteración sobre los índices:** Se recorre la lista `nums` utilizando `enumerate` para tener acceso a cada índice y valor.
- **Acceso indirecto:** Para cada posición `i`, se añade a `result` el valor en `nums[nums[i]]`, cumpliendo así la condición establecida.
- **Estrategia alternativa (comentada):** Se incluye también una línea con una posible solución usando *list comprehension*, aunque se opta por la versión explícita por mayor claridad en la trazabilidad de la operación.

## Uso

Para utilizar este código, simplemente se debe definir el array `nums` como una permutación de los números del 0 al `n - 1`, y luego crear una instancia de la clase `Solution`. Se llama al método `buildArray` con este array y se obtiene el nuevo array resultante.

```python
if __name__ == "__main__":
    nums = [0, 2, 1, 5, 3, 4]

    sol = Solution()
    result = sol.buildArray(nums)
    print(result)  # Output: [0, 1, 2, 4, 5, 3]
```

## Conclusión

El ejercicio "Build Array from Permutation" es una excelente práctica para comprender el uso de listas como estructuras de acceso indirecto, y para reforzar conceptos de permutaciones e índices en estructuras de datos. La solución propuesta es simple, clara y eficiente, aprovechando el acceso directo a memoria mediante índices, y es ideal para familiarizarse con patrones de transformación de arrays. Además, resulta útil como paso previo para entender técnicas más complejas de manipulación de datos y acceso jerárquico.
