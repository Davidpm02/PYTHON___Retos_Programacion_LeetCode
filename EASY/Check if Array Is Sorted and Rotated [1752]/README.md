# Check if Array Is Sorted and Rotated

## Descripción

El ejercicio "Check if Array Is Sorted and Rotated" consiste en determinar si un arreglo de enteros fue originalmente ordenado en orden no decreciente y luego rotado un número arbitrario de posiciones. En caso afirmativo, la función debe devolver `True`; en caso contrario, `False`.

Una rotación de `x` posiciones implica que el elemento en la posición `i` de la lista original pasa a la posición `(i + x) % n` en la nueva lista, donde `n` es la longitud del arreglo.

El problema permite la presencia de números duplicados en la lista original.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `check`. Este método evalúa la cantidad de discontinuidades en el orden no decreciente del arreglo.

### Detalles de la implementación

- **Recorrido del arreglo**: Se itera sobre el arreglo verificando si hay más de una discontinuidad en el orden no decreciente.
- **Comparación cíclica**: Se utiliza la operación módulo (`%`) para considerar la conexión entre el último y el primer elemento del arreglo.
- **Condición de validación**: Si hay más de una discontinuidad en la secuencia, la lista no pudo haber sido obtenida a partir de una rotación de una lista ordenada.

## Uso

Para utilizar este código, se debe definir un arreglo de enteros y luego crear una instancia de la clase `Solution`. Posteriormente, se llama al método `check` con el arreglo como parámetro para determinar si es un arreglo ordenado y rotado.

```python
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    sol = Solution()
    result = sol.check(nums)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Check if Array Is Sorted and Rotated" permite evaluar una propiedad fundamental de los arreglos ordenados y rotados mediante una técnica eficiente de recorrido lineal. La solución presentada es óptima en términos de complejidad temporal, ejecutándose en **O(n)**, donde `n` es el tamaño del arreglo. Su implementación es concisa y aprovecha el uso de la aritmética modular para la comparación de los elementos en un entorno cíclico. Este problema es útil para comprender la manipulación de estructuras de datos y la detección de patrones en secuencias numéricas.
