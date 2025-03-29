# Minimum Index of a Valid Split

## Descripción

El ejercicio "Minimum Index of a Valid Split" consiste en encontrar el índice mínimo donde se pueda dividir un array de números enteros en dos partes, manteniendo el mismo elemento dominante en ambas. Un elemento es considerado dominante si aparece más veces que la mitad del tamaño del array.

La división del array debe cumplir con las siguientes condiciones:

- La partición debe dividir el array en dos partes no vacías.
- Ambas partes deben tener el mismo elemento dominante que el array original.
- Se debe retornar el índice mínimo donde la división es válida. Si no es posible dividir el array de esta manera, se retorna `-1`.

## Implementación

La implementación se realiza en Python utilizando la clase `Solution`, que contiene el método `minimumIndex`. Este método sigue los siguientes pasos:

- Se utiliza un contador para determinar el elemento dominante en el array.
- Se calcula la frecuencia total del elemento dominante en el array original.
- Se recorre el array manteniendo un conteo acumulativo del elemento dominante en la primera parte.
- En cada iteración, se verifica si ambas partes cumplen con la condición de dominancia.
- Si se encuentra un índice válido, se retorna. En caso contrario, se retorna `-1`.

## Uso

Para utilizar este código, se debe definir una lista de números enteros y luego crear una instancia de la clase `Solution`. Se llama al método `minimumIndex` con esta lista para obtener el índice mínimo donde la división es válida.

```python
if __name__ == "__main__":
    nums = [2,1,3,1,1,1,7,1,2,1]
    
    sol = Solution()
    index = sol.minimumIndex(nums)
    print(index)  # Output: 4
```

## Conclusión

El ejercicio "Minimum Index of a Valid Split" es un problema de manipulación de arrays que requiere encontrar un punto óptimo de división basado en la frecuencia de un elemento dominante. La solución implementada utiliza un enfoque eficiente basado en conteo y recorridos iterativos, logrando determinar la viabilidad de la división en tiempo lineal. Este tipo de problemas es útil para reforzar conceptos de algoritmos de conteo, estructuras de datos como diccionarios y optimización en recorridos de listas.
