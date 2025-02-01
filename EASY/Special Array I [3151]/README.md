# Special Array I

## Descripción

El ejercicio "Special Array I" consiste en determinar si un arreglo de enteros es "especial". Un arreglo es considerado especial si todos sus pares de elementos adyacentes contienen dos números con paridad diferente (es decir, uno es par y el otro es impar). El objetivo es verificar si cada par consecutivo en el arreglo cumple con esta condición.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `isArraySpecial`. Este método recorre el arreglo y verifica, para cada par de elementos adyacentes, si uno es par y el otro es impar. Si en algún momento se encuentra un par de elementos con la misma paridad (ambos pares o ambos impares), el método devuelve `False`. Si todos los pares cumplen con la condición de tener diferentes paridades, el método devuelve `True`.

## Detalles de la implementación

- **Recorrido del arreglo:** Se recorre el arreglo de enteros `nums` de manera secuencial, comparando cada par de elementos adyacentes.
- **Verificación de la paridad:** Para cada par de elementos consecutivos, se comprueba si uno es par y el otro impar usando la operación módulo.
- **Manejo de errores:** Si se detecta que dos elementos adyacentes tienen la misma paridad, se lanza una excepción `AssertionError`, que es capturada para devolver `False`.

## Uso

Para utilizar este código, simplemente se debe definir el arreglo de enteros `nums` y luego crear una instancia de la clase `Solution`. Se llama al método `isArraySpecial` con el arreglo como parámetro y se obtiene un valor booleano que indica si el arreglo es especial.

```python
if __name__ == "__main__":
    nums = [2, 1, 4]

    sol = Solution()
    result = sol.isArraySpecial(nums)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Special Array I" permite verificar si un arreglo de enteros cumple con la condición de ser especial, es decir, si todos sus pares consecutivos de elementos tienen diferente paridad. Este tipo de verificación es útil en diversas aplicaciones de programación que involucren arreglos y condiciones sobre sus elementos. La implementación es simple y eficiente, utilizando operaciones aritméticas básicas para determinar la paridad de los números y compararlos. Este enfoque refuerza conceptos importantes de manipulación de arreglos y condiciones lógicas en programación.
