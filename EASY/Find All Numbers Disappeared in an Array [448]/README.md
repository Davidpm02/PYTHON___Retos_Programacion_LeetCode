# Find All Numbers Disappeared in an Array

## Descripción

El ejercicio "Find All Numbers Disappeared in an Array" se enfoca en encontrar los números que faltan en una secuencia de enteros consecutivos en el rango `[1, n]`, en un array dado `nums` de longitud `n`. La lista `nums` contiene enteros en el rango `[1, n]`, pero algunos de estos pueden estar ausentes. La tarea es devolver un array con todos los números en este rango que no aparecen en `nums`.

Este tipo de ejercicio es importante en escenarios de procesamiento de datos donde es necesario identificar elementos faltantes en secuencias o conjuntos ordenados.

## Implementación

La implementación en Python utiliza una clase `Solution` que contiene el método `findDisappearedNumbers`. Este método emplea el módulo `Counter` de la biblioteca `collections` para contar las ocurrencias de cada elemento en `nums`. Luego, se compara el conjunto de números presentes con el rango completo `[1, n]` para identificar los elementos ausentes.

### Detalles de la Implementación

- **Conteo de elementos**: Se crea un contador de los elementos en `nums` usando `Counter` para detectar rápidamente cuáles números están presentes en la lista.
- **Búsqueda de números faltantes**: Se utiliza una lista por compresión para iterar sobre el rango `[1, n]`, comprobando en cada paso si el número está presente en el `Counter`.
- **Retorno de la lista de faltantes**: Los números que no están presentes en `nums` se devuelven en una lista ordenada de menor a mayor.

## Uso

Para utilizar este código, basta con definir un array `nums` que contenga enteros en el rango `[1, n]` y crear una instancia de la clase `Solution`. Al llamar al método `findDisappearedNumbers`, se obtendrá una lista de todos los números que no están en `nums`.

```python
if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    sol = Solution()
    missing_numbers = sol.findDisappearedNumbers(nums)
    print(missing_numbers)  # Output: [5, 6]
```

## Conclusión

El ejercicio "Find All Numbers Disappeared in an Array" es una demostración de cómo trabajar con conjuntos y el módulo Counter para encontrar elementos ausentes de una secuencia dada. La solución implementada es eficiente y fácil de entender, y representa una técnica útil para problemas de búsqueda de elementos faltantes en secuencias o conjuntos. Este enfoque es particularmente útil en aplicaciones de procesamiento de datos donde es común trabajar con secuencias o listas incompletas.
