# Move Zeroes

## Descripción

El ejercicio "Move Zeroes" consiste en modificar un arreglo de números enteros de tal forma que todos los valores que son iguales a 0 se muevan al final del arreglo, mientras se mantiene el orden relativo de los elementos no nulos. Es importante destacar que la operación debe realizarse in-place, es decir, sin crear una copia adicional del arreglo. Este tipo de problemas es común en la manipulación de arreglos y listas, y es crucial para optimizar el uso de memoria y eficiencia en algoritmos.

## Implementación

La implementación se realiza en Python, utilizando una clase Solution que contiene el método moveZeroes. Este método actualiza el arreglo nums en su lugar, moviendo todos los ceros al final y manteniendo el orden original de los elementos no nulos.

### Detalles de la implementación

* Iteración sobre el arreglo: Se recorre el arreglo y se identifica cada elemento que sea igual a 0.

* Reubicación de los ceros: Cada vez que se encuentra un 0, se elimina del arreglo y se agrega al final. Esto asegura que los ceros sean "movidos" al final sin alterar el orden relativo de los otros elementos.

* Restricción de copia: El ejercicio impone la restricción de no hacer una copia del arreglo, lo que significa que todas las operaciones deben hacerse directamente sobre el arreglo original.

## Uso

Para utilizar este código, es necesario crear una instancia de la clase Solution y llamar al método moveZeroes, pasando el arreglo de enteros que se desea procesar. A continuación se muestra un ejemplo del uso del método:

```python
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
```

## Conclusión

El ejercicio "Move Zeroes" proporciona una solución eficiente para reorganizar un arreglo manteniendo el orden de los elementos no nulos y moviendo todos los ceros al final. La implementación presentada es sencilla, pero podría optimizarse aún más en términos de tiempo de ejecución, ya que la actual realiza múltiples operaciones de eliminación y adición que podrían afectar el rendimiento para listas grandes. Este problema refuerza conceptos importantes como la manipulación in-place de listas y la optimización de algoritmos para trabajar con estructuras de datos grandes.
