# Remove Element

## Descripción

El ejercicio "Remove Element" se enfoca en modificar un array de enteros nums removiendo todas las ocurrencias de un valor entero específico val. El proceso debe realizarse "in-place", alterando el array original para contener, en sus primeros k elementos, todos los elementos distintos de val. La función debe retornar el número k de elementos en el array que no son igual a val. No es relevante el contenido del array más allá del k-ésimo elemento.

Este ejercicio permite practicar la manipulación de arrays en Python, especialmente la modificación in-place que es útil para optimizar el uso de memoria en problemas de mayor escala.

## Implementación

La implementación en Python se realiza en una clase llamada Solution que contiene el método removeElement. Este método toma dos parámetros: nums, que es un array de enteros, y val, el entero cuyas ocurrencias deben ser eliminadas del array.

El método emplea list comprehension para filtrar y conservar sólo aquellos elementos que no son iguales a val, asignando el resultado de nuevo a nums. La función retorna la longitud del array filtrado, lo cual es equivalente al número de elementos que no son igual a val.

## Uso

Para utilizar el método removeElement, es necesario primero instanciar la clase Solution y luego llamar al método con los parámetros necesarios. A continuación se muestra un ejemplo de cómo usar este método:

```python
# Crear una instancia de la clase Solution
solucion = Solution()

# Definir el array nums y el valor a eliminar val
nums = [0,1,2,2,3,0,4,2]
val = 2

# Llamar al método removeElement y capturar el resultado
k = solucion.removeElement(nums, val)

# Imprimir la cantidad de elementos válidos y el estado final del array
print(f"Elementos válidos: {k}, Estado del array: {nums[:k]}")
```

## Conclusión

El ejercicio "Remove Element" es una excelente práctica para entender cómo manipular y modificar arrays en Python de manera eficiente. Este tipo de habilidades son fundamentales en el desarrollo de soluciones más complejas en ciencia de datos y algoritmos, donde la optimización de recursos es crucial. Además, el patrón de diseño utilizado es ampliamente aplicable a diversos problemas de filtrado y transformación de datos.
