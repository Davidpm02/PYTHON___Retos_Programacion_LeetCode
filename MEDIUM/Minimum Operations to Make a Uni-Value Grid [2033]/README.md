# Minimum Operations to Make a Uni-Value Grid

## Descripción

El ejercicio "Minimum Operations to Make a Uni-Value Grid" consiste en transformar una cuadrícula bidimensional de números enteros en una cuadrícula donde todos los elementos sean iguales. Para ello, en cada operación se puede sumar o restar un valor específico `x` a cualquier elemento de la cuadrícula.

El objetivo es determinar el número mínimo de operaciones necesarias para lograr que todos los elementos sean iguales. Si no es posible, se debe devolver `-1`.

## Implementación

La solución se desarrolla en Python mediante una clase `Solution`, que contiene el método `minOperations`. Este método realiza los siguientes pasos:

- **Conversión de la cuadrícula a una lista unidimensional:** Se extraen todos los valores de la cuadrícula y se almacenan en una lista.
- **Verificación de viabilidad:** Se comprueba si todos los elementos de la lista tienen el mismo residuo al dividirlos por `x`. Si no es así, se devuelve `-1` porque no es posible igualar todos los valores.
- **Ordenación de valores:** La lista se ordena para encontrar la mediana.
- **Cálculo del número mínimo de operaciones:** Se determina la cantidad de operaciones necesarias para transformar cada valor en la mediana utilizando sumas y restas de `x`.

## Uso

Para utilizar este código, se debe definir la cuadrícula `grid` y el valor `x`. Luego, se crea una instancia de la clase `Solution` y se llama al método `minOperations` con estos parámetros.

```python
if __name__ == "__main__":
    grid = [[2,4],[6,8]]
    x = 2
    
    sol = Solution()
    result = sol.minOperations(grid, x)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Minimum Operations to Make a Uni-Value Grid" permite aplicar técnicas de manipulación de estructuras de datos y ordenación para encontrar soluciones óptimas. La estrategia basada en la mediana minimiza las operaciones necesarias, proporcionando una solución eficiente. Además, la verificación de viabilidad mediante el residuo asegura que no se realicen cálculos innecesarios en casos imposibles. Esta metodología es útil en problemas donde se requiere la unificación de valores con restricciones específicas de transformación.
