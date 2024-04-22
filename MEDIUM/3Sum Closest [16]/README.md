# 3Sum Closest

## Descripción

El ejercicio "3Sum Closest" consiste en encontrar tres enteros dentro de un array nums tal que la suma de los tres enteros sea la más cercana posible a un valor entero target dado. Este problema se presenta con la restricción de que habrá una única solución para cada conjunto de entradas.

El objetivo es desarrollar una función dentro de la clase Solution que pueda resolver este problema de manera eficiente dadas las restricciones de tamaño y valores para nums y target.

## Implementación

La clase Solution contiene el método threeSumClosest, el cual acepta dos parámetros:

* nums: Lista de enteros de la que se seleccionarán tres números.
* target: El valor entero al que la suma de los tres números seleccionados debe aproximarse lo más posible.

El método emplea una técnica de punteros para evaluar sumas de tripletas posibles en un array ordenado. Para identificar la suma más cercana, se utiliza una función auxiliar closest_num, que determina el número más próximo al target de un conjunto de valores.

## Proceso de la función

* Ordenamiento inicial del array nums: Para facilitar la identificación de tripletas.
* Iteración a través de nums con dos punteros: Se inicializan dos punteros en los extremos del subarray que sigue al índice actual para explorar todas las posibles combinaciones de tripletas.
* Almacenamiento y comparación de sumas: Las sumas de tripletas se almacenan en un conjunto y se compara cada suma con el target para ajustar los punteros adecuadamente.
* Selección del valor más cercano: Una vez obtenidas todas las sumas posibles, se utiliza la función closest_num para seleccionar la suma más cercana al target.

## Uso

Para utilizar el código, se debe crear una instancia de la clase Solution y llamar al método threeSumClosest con los argumentos necesarios. Ejemplo de uso:

```python
if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    solution = Solution()
    result = solution.threeSumClosest(nums, target)
    print(f"La suma más cercana a {target} es {result}.")
```

Este fragmento ejecutará el código utilizando el array nums y el target especificados, e imprimirá el resultado en la consola.

## Conclusión

El problema "3Sum Closest" es un excelente ejercicio para entender y practicar el manejo de punteros y la optimización de algoritmos para problemas de búsqueda. El código proporcionado demuestra un enfoque efectivo para resolver este tipo de problemas, garantizando eficiencia y claridad en la solución. Este ejercicio es también útil para prepararse para entrevistas técnicas donde se evalúan habilidades en estructuras de datos y algoritmos.
