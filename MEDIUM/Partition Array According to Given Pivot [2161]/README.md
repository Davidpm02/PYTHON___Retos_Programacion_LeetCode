# Partition Array According to Given Pivot

## Descripción

El ejercicio "Partition Array According to Given Pivot" consiste en reorganizar un array de enteros de manera que cumpla con las siguientes condiciones:

1. Todos los elementos menores que el pivote aparecen antes que aquellos mayores que el pivote.
2. Todos los elementos iguales al pivote aparecen entre los elementos menores y los mayores que el pivote.
3. Se mantiene el orden relativo de los elementos menores y mayores al pivote en su disposición original.

El objetivo es retornar el array reorganizado cumpliendo estas reglas, sin alterar el orden relativo de los elementos dentro de cada grupo.

## Implementación

La solución se desarrolla en Python mediante una clase `Solution` que contiene el método `pivotArray`. Este método toma una lista de números enteros y un valor de pivote, y devuelve una nueva lista reorganizada de acuerdo con las reglas establecidas.

### Detalles de la implementación

- **Uso de listas auxiliares**: Se emplean tres listas para separar los elementos en función de su relación con el pivote:
  - `lower_pivot`: Contiene los elementos menores que el pivote.
  - `pivot`: Contiene los elementos iguales al pivote.
  - `higher_pivot`: Contiene los elementos mayores que el pivote.
- **Recorrido del array**: Se itera sobre `nums`, clasificando cada número en la lista correspondiente.
- **Construcción del resultado**: Se concatenan las listas en el orden adecuado para formar el array final.

## Uso

Para utilizar este código, se debe definir un array de números enteros junto con un pivote, y luego crear una instancia de la clase `Solution`. Se llama al método `pivotArray` con estos valores y se obtiene el array reorganizado.

```python
if __name__ == "__main__":
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    
    sol = Solution()
    result = sol.pivotArray(nums, pivot)
    print(result)  # Output: [9, 5, 3, 10, 10, 12, 14]
```

## Conclusión

El ejercicio "Partition Array According to Given Pivot" es útil para comprender la manipulación y organización de estructuras de datos en listas manteniendo el orden relativo de los elementos. La solución propuesta es eficiente, aprovechando un único recorrido del array para clasificar los elementos y una operación de concatenación para ensamblar el resultado. Este enfoque permite resolver el problema de manera clara y óptima sin necesidad de ordenar el array de manera global.
