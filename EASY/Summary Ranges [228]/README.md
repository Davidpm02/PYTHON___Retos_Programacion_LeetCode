# Summary Ranges

## Descripción

El ejercicio "Summary Ranges" consiste en tomar un array de enteros únicos y ordenados, y devolver una lista de rangos que cubran todos los números del array de manera exacta. Cada rango se debe representar de forma que, si el rango abarca más de un número, se mostrará como "a->b"; si solo abarca un número, se mostrará simplemente como "a". Este ejercicio es útil para el manejo de intervalos y resúmenes de datos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `summaryRanges`. Este método recorre el array de enteros, identifica los rangos y los almacena en una lista que se devuelve al final.

## Detalles de la implementación

- **Inicialización de rangos:** Se inicia una lista vacía para almacenar los rangos y se verifica si el array está vacío.
- **Recorrido del array:** Se recorre el array comenzando desde el segundo elemento, comparando cada número con el anterior para determinar si son consecutivos.
- **Formación de rangos:** Cuando se encuentra un número que no es consecutivo, se agrega el rango correspondiente a la lista de rangos. También se maneja la inclusión del último rango después de finalizar el bucle.

## Uso

Para utilizar este código, simplemente se debe definir un array de enteros únicos y ordenados, y luego crear una instancia de la clase `Solution`. Se llama al método `summaryRanges` con el array como argumento para obtener la lista de rangos.

```python
if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]

    sol = Solution()
    ranges = sol.summaryRanges(nums)
    print(ranges)  # Output: ["0->2","4->5","7"]
```

## Conclusión

El ejercicio "Summary Ranges" proporciona un enfoque efectivo para resumir intervalos de números enteros de un array. Este tipo de operación es común en problemas de programación que requieren un análisis de datos o simplificación de rangos. La implementación es directa y aprovecha la estructura ordenada del array para identificar rangos de manera eficiente, lo que refuerza conceptos clave sobre la manipulación de listas y el control de flujo en Python.
