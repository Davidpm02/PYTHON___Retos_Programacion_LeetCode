# Minimum Number of Operations to Make Elements in Array Distinct

## Descripción

El ejercicio **"Minimum Number of Operations to Make Elements in Array Distinct"** plantea el reto de transformar un array de enteros en uno cuyos elementos sean completamente distintos, utilizando una operación específica: eliminar los tres primeros elementos del array (o todos si quedan menos de tres).

El objetivo es determinar el número mínimo de estas operaciones necesarias para lograr que todos los elementos restantes en el array sean únicos. Este tipo de problema es útil para explorar conceptos relacionados con manejo de arrays, control de duplicados y simulación de operaciones en estructuras de datos.

## Implementación

La solución se implementa en Python a través de una clase llamada `Solution`, que contiene el método `minimumOperations`. Este método se encarga de iterar sobre el array `nums`, eliminando elementos según la operación permitida, hasta que todos los elementos restantes sean distintos.

## Detalles de la implementación

- **Control de operaciones:** Se inicializa un contador `operations` que lleva el seguimiento del número de operaciones realizadas.

- **Verificación de unicidad:** Se compara la longitud del array con la longitud de un conjunto construido a partir de él (`set(nums)`). Si ambas longitudes coinciden, todos los elementos son únicos y se retorna el contador.

- **Aplicación de la operación:** Si hay duplicados, se eliminan los tres primeros elementos del array utilizando slicing (`nums = nums[3:]`), lo que reduce el array desde el cuarto elemento en adelante.

- **Condición de parada:** El bucle continúa hasta que el array esté vacío o todos los elementos sean distintos. En cualquiera de los casos, se retorna el número mínimo de operaciones realizadas.

## Uso

Para utilizar esta solución, basta con crear una instancia de la clase `Solution` y llamar al método `minimumOperations`, pasando como argumento un array de enteros.

```python
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]

    sol = Solution()
    min_ops = sol.minimumOperations(nums)
    print(min_ops)  # Output: 2
```

## Conclusión

El ejercicio "Minimum Number of Operations to Make Elements in Array Distinct" es una excelente práctica para trabajar con lógica de arrays, condiciones de parada y operaciones de eliminación controlada. El enfoque implementado permite resolver el problema de forma clara y eficiente, simulando paso a paso las operaciones requeridas hasta cumplir con la condición de unicidad en los elementos. Este tipo de ejercicios refuerza habilidades clave en estructuras de datos y algoritmos de simulación.
