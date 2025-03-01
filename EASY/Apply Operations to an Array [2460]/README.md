# Apply Operations to an Array

## Descripción

El ejercicio "Apply Operations to an Array" consiste en aplicar una serie de operaciones secuenciales a un array de enteros no negativos. En cada operación, si dos elementos consecutivos del array son iguales, el primer elemento se multiplica por 2 y el segundo se establece en 0. Posteriormente, se realiza un desplazamiento de los ceros en el array, moviéndolos hacia el final.

Este tipo de operaciones es común en problemas de manipulación de arrays donde se requiere optimizar el procesamiento de datos y gestionar elementos en función de sus relaciones.

## Implementación

La implementación se realiza en Python utilizando la clase `Solution` y el método `applyOperations`. Este método toma como entrada un array de enteros, realiza las operaciones sobre los elementos según las condiciones especificadas, y finalmente reordena el array para mover todos los ceros al final.

### Detalles de la implementación

1. **Operación de multiplicación:** Se recorren los elementos del array de izquierda a derecha. Si dos elementos consecutivos son iguales, se multiplica el primer elemento por 2 y se asigna 0 al segundo.
2. **Desplazamiento de ceros:** Después de aplicar las operaciones, los ceros del array se mueven al final, manteniendo el orden relativo de los otros elementos.

## Uso

Para utilizar este código, se debe definir el array de enteros `nums` y luego crear una instancia de la clase `Solution`. Después, se llama al método `applyOperations` con el array como parámetro, y el método devolverá el array modificado.

```python
if __name__ == "__main__":
    nums = [1, 2, 2, 1, 1, 0]

    sol = Solution()
    result = sol.applyOperations(nums)
    print(result)  # Output: [1, 4, 2, 0, 0, 0]
```

## Conclusión

El ejercicio "Apply Operations to an Array" proporciona una forma eficiente de aplicar transformaciones específicas a un array de enteros, como la multiplicación de elementos consecutivos y el desplazamiento de ceros. La solución implementada maneja estas operaciones de manera secuencial y optimiza el movimiento de los ceros al final del array. Este tipo de problemas es útil para entender cómo manipular y procesar arrays de forma eficaz, y puede ser adaptado a diversas aplicaciones en programación y análisis de datos.
