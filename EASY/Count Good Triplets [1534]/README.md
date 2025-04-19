# Count Good Triplets

## Descripción

El ejercicio "Count Good Triplets" plantea la tarea de identificar cuántos tripletes en un array de enteros cumplen con ciertas condiciones específicas de valor absoluto entre sus elementos. Un triplete se considera "bueno" si se respetan tres condiciones:

1. Los índices cumplen `0 <= i < j < k < arr.length`.
2. Las diferencias absolutas entre los valores en las posiciones `i`, `j` y `k` están acotadas por tres parámetros `a`, `b` y `c`.

Este tipo de problema es útil para reforzar el manejo de estructuras anidadas, la comprensión de condiciones múltiples y el uso de valores absolutos, todos ellos conceptos fundamentales en la lógica algorítmica.

## Implementación

La solución está implementada en Python utilizando una clase `Solution`, que incluye un único método llamado `countGoodTriplets`. Este método toma como entrada un array de enteros `arr` y tres valores enteros `a`, `b` y `c`, que definen los umbrales de comparación entre los elementos del triplete.

## Detalles de la implementación

- **Recorrido exhaustivo:** Se utilizan tres bucles anidados para generar todas las combinaciones posibles de tripletes con `i < j < k`. Dado que el tamaño máximo del array es 100, esta aproximación es computacionalmente viable.
- **Verificación de condiciones:** Para cada triplete generado, se evalúan las siguientes condiciones:
  - `|arr[i] - arr[j]| <= a`
  - `|arr[j] - arr[k]| <= b`
  - `|arr[i] - arr[k]| <= c`
- **Contador acumulativo:** Cada vez que un triplete cumple todas las condiciones, se incrementa un contador que finalmente se retorna como resultado.

El método sigue un enfoque claro y directo, adecuado para conjuntos de datos relativamente pequeños donde se pueden explorar todas las combinaciones sin problemas de eficiencia significativos.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `countGoodTriplets` pasando el array de entrada junto con los tres parámetros de comparación. A continuación se muestra cómo hacerlo:

```python
if __name__ == "__main__":
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3

    sol = Solution()
    result = sol.countGoodTriplets(arr, a, b, c)
    print(result)  # Output esperado: 4
```

## Conclusión

El ejercicio "Count Good Triplets" proporciona una práctica efectiva para trabajar con estructuras anidadas, condiciones múltiples y comparaciones basadas en valor absoluto. Aunque el algoritmo sigue una estrategia de fuerza bruta, su claridad y simplicidad lo hacen ideal para aprender a manipular combinaciones de elementos e implementar filtros condicionales. Además, refuerza habilidades esenciales para problemas de búsqueda y evaluación de relaciones entre elementos en listas.
