# Third Distinct Maximum Number

## Descripción

El ejercicio "Third Distinct Maximum Number" tiene como objetivo encontrar el tercer número máximo distinto en un array de enteros `nums`. Si el tercer número máximo no existe (por ejemplo, si hay menos de tres números distintos en el array), el ejercicio indica que se debe retornar el número máximo presente en el array. Este tipo de operación es útil en tareas de clasificación y filtrado de datos, donde se requieren los valores máximos o límites en un conjunto de datos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `thirdMax`. Este método convierte el array en un conjunto para eliminar duplicados y luego busca el tercer valor máximo, si existe, o el valor máximo en caso contrario.

### Detalles de la Implementación

- **Conversión a conjunto**: Utilizamos `set(nums)` para eliminar elementos duplicados en el array.
- **Manejo de excepciones**: Con `assert`, verificamos que el conjunto tenga al menos tres elementos distintos. Si no, el método devolverá el valor máximo de `nums`.
- **Búsqueda de valores máximos**: Se utiliza un bucle para encontrar y almacenar los tres valores máximos distintos en `nums`. En cada iteración, se encuentra el valor máximo, se guarda y luego se elimina del conjunto para buscar el siguiente valor máximo.
  
## Uso

Para utilizar este código, simplemente se debe definir un array `nums` y crear una instancia de la clase `Solution`. Llamando al método `thirdMax`, se obtiene el tercer número máximo distinto o el máximo en caso de no haber suficientes números únicos.

```python
if __name__ == "__main__":
    nums = [2, 2, 3, 1]

    sol = Solution()
    third_max_number = sol.thirdMax(nums)
    print(third_max_number)  # Output: 1
```

## Conclusión

El ejercicio "Third Distinct Maximum Number" proporciona una solución eficiente para encontrar el tercer valor máximo en un conjunto de datos, considerando solo valores distintos. La implementación aprovecha la estructura de conjuntos en Python para reducir la cantidad de comparaciones y garantiza que el valor máximo se devuelva correctamente cuando no hay suficientes números únicos. Este enfoque es adecuado para aplicaciones de clasificación y filtrado de datos en entornos de datos no duplicados.
