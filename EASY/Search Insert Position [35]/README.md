# Search Insert Position

## Descripción

El ejercicio "Search Insert Position" consiste en encontrar la posición en la que se debe insertar un valor objetivo (target) en un array ordenado de enteros distintos. Si el objetivo ya se encuentra en el array, se debe devolver su índice. Este algoritmo debe tener una complejidad temporal de O(log n), lo que sugiere el uso de búsqueda binaria.

**Ejemplos:**

1. **Input:** nums = [1,3,5,6], target = 5  
   **Output:** 2

2. **Input:** nums = [1,3,5,6], target = 2  
   **Output:** 1

3. **Input:** nums = [1,3,5,6], target = 7  
   **Output:** 4

**Restricciones:**

- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- `nums` contiene valores distintos ordenados en orden ascendente.
- -10⁴ <= target <= 10⁴

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `searchInsert`. Este método busca el índice del valor objetivo en el array `nums`. Si no se encuentra, devuelve el índice en el que debería insertarse para mantener el orden.

### Detalles de la implementación

- **Búsqueda en array:** Se utiliza un enfoque de búsqueda binaria para encontrar el índice del valor objetivo.
- **Manejo de excepciones:** Si el valor no se encuentra en el array, se determina la posición de inserción adecuada.

## Uso

Para utilizar este código, simplemente se debe definir el array nums y el valor target. Luego, se crea una instancia de la clase Solution y se llama al método searchInsert con el array y el valor objetivo. El método devolverá el índice en el que se encuentra el valor o el índice en el que debería ser insertado.

```python
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2

    sol = Solution()
    index = sol.searchInsert(nums, target)
    print(index)  # Output: 1
```

## Conclusión

El ejercicio "Search Insert Position" proporciona una manera eficiente de encontrar la posición de inserción adecuada para un valor en un array ordenado. Utilizando búsqueda binaria, se logra una complejidad temporal de O(log n), lo que hace que este método sea ideal para grandes conjuntos de datos. La implementación presentada es directa y aprovecha las capacidades de Python para manejar arrays y búsquedas de manera eficiente.
