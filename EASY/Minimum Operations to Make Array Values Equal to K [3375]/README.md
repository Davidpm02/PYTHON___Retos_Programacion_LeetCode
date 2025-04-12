# Minimum Operations to Make Array Values Equal to K

## Descripción

El ejercicio **"Minimum Operations to Make Array Values Equal to K"** plantea el desafío de transformar todos los elementos de un array de enteros `nums` en un valor objetivo `k`, utilizando una operación específica. Esta operación consiste en seleccionar un entero `h` válido y reemplazar todos los valores mayores que `h` en el array por `h`.

Un entero `h` se considera válido si todos los valores mayores que `h` en el array son idénticos. El objetivo es encontrar el número mínimo de operaciones requeridas para lograr que todos los elementos del array sean iguales a `k`. Si esto no es posible, se debe retornar `-1`.

Este tipo de problema es útil para estudiar condiciones de validez en operaciones sobre arrays y para simular transformaciones controladas que llevan un conjunto de valores a un objetivo común.

## Implementación

La solución está implementada en Python mediante una clase `Solution`, que contiene el método `minOperations`. Este método analiza los valores del array `nums` y simula paso a paso las operaciones válidas necesarias para que todos los elementos terminen siendo iguales al valor objetivo `k`.

## Detalles de la implementación

- **Condición de terminación inmediata:** Si todos los elementos del array ya son iguales a `k`, el método retorna 0 directamente.

- **Comprobación de imposibilidad:** Si existe al menos un valor menor que `k`, no se puede transformar el array al valor `k` únicamente utilizando operaciones que reducen valores, por lo tanto se retorna `-1`.

- **Identificación de valores por encima de `k`:** Se construye un conjunto con los valores únicos que son mayores que `k`. Cada uno de estos valores necesitará una operación para ser reducido a un valor inferior, eventualmente igual a `k`.

- **Simulación de operaciones:** Se ordenan los valores mayores a `k` en orden descendente y se cuenta una operación por cada uno, ya que se necesita una operación válida para reducirlos en secuencia hasta alcanzar el valor deseado.

## Uso

Para utilizar este código, basta con crear una instancia de la clase `Solution` y llamar al método `minOperations`, pasando el array de enteros y el valor objetivo `k`.

```python
if __name__ == "__main__":
    nums = [5, 2, 5, 4, 5]
    k = 2

    sol = Solution()
    result = sol.minOperations(nums, k)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Minimum Operations to Make Array Values Equal to K" permite practicar la simulación de operaciones condicionadas sobre arrays, un concepto muy útil en problemas de optimización y transformación de datos. La solución presentada combina comprobaciones previas para descartar casos imposibles con una estrategia ordenada que reduce progresivamente los valores mayores a k, asegurando así un enfoque eficiente para encontrar la cantidad mínima de operaciones requeridas.
