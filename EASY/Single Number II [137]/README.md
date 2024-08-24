# Single Number II

## Descripción

El ejercicio "Single Number II" consiste en identificar un único elemento en un array de enteros donde cada elemento aparece exactamente tres veces, excepto uno que aparece una sola vez. La tarea es encontrar y devolver ese único elemento. Este problema es relevante en el manejo de grandes conjuntos de datos donde se requiere identificar excepciones o elementos únicos de manera eficiente.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `singleNumber`. Este método recibe un array de enteros `nums` y devuelve el número que aparece solo una vez en el array, mientras que todos los demás elementos aparecen tres veces.

### Detalles de la Implementación

- **Uso de Counter:**
  - Se utiliza la clase `Counter` de la biblioteca `collections` para contar la frecuencia de aparición de cada número en el array.
- **Identificación del elemento único:**
  - El método identifica el único elemento que tiene una frecuencia de aparición de uno, utilizando el método `most_common` de `Counter`, que retorna una lista de tuplas con los elementos y sus conteos, ordenada por la frecuencia.

Este enfoque garantiza que se cumple con la complejidad lineal y el uso de espacio constante, tal como lo exigen las restricciones del problema.

## Uso

Para utilizar este código, define un array de enteros `nums`, crea una instancia de la clase `Solution`, y llama al método `singleNumber`. El resultado será el entero que aparece una sola vez en el array.

```python
if __name__ == "__main__":
    nums = [2,2,3,2]
    
    sol = Solution()
    unique_number = sol.singleNumber(nums)
    print(unique_number)  # Output: 3
```

## Conclusión

El ejercicio "Single Number II" presenta un desafío interesante y práctico para identificar un elemento único en un array donde todos los demás elementos están triplicados. La solución implementada es eficiente y utiliza las capacidades de la clase Counter para simplificar la tarea de conteo. Este ejercicio es útil para reforzar conceptos sobre la manipulación de datos en arrays y el uso de herramientas de conteo en Python. Además, cumple con las restricciones de tiempo y espacio, lo que lo hace adecuado para aplicaciones en entornos con recursos limitados y grandes volúmenes de datos.
