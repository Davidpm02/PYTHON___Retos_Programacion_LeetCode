# Single Number

## Descripción

El ejercicio "Single Number" consiste en encontrar un único elemento en un array de enteros donde cada elemento aparece dos veces, excepto uno. La tarea es identificar ese elemento único. Este tipo de problema es común en la manipulación de datos y estructuras de datos, y es útil para reforzar conceptos de conteo y algoritmos de búsqueda eficiente.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `singleNumber`. Este método recibe un array de enteros `nums` y devuelve el número que aparece una sola vez en el array.

### Detalles de la Implementación

- **Uso de Counter:**
  - Se utiliza la clase `Counter` de la biblioteca `collections` para contar la frecuencia de aparición de cada número en el array.
- **Identificación del elemento único:**
  - El método identifica el único elemento que tiene una frecuencia de aparición de uno.

Este enfoque permite resolver el problema con una complejidad temporal lineal y utilizando un espacio adicional constante, cumpliendo así con las restricciones del problema.

## Uso

Para utilizar este código, simplemente define un array de enteros `nums`, crea una instancia de la clase `Solution`, y llama al método `singleNumber`. El resultado será el entero que aparece una única vez en el array.

```python
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    
    sol = Solution()
    unique_number = sol.singleNumber(nums)
    print(unique_number)  # Output: 4
```

## Conclusión

El ejercicio "Single Number" ofrece una forma eficiente de identificar un elemento único en un array donde todos los demás elementos están duplicados. La solución presentada es directa y eficiente, haciendo uso de la estructura Counter para contar las apariciones de cada número. Este ejercicio es útil para reforzar conocimientos sobre el manejo de datos en arrays y la utilización de herramientas de conteo en Python. Además, la solución implementada se ajusta a las restricciones de tiempo y espacio, lo que la hace adecuada para aplicaciones en tiempo real y sistemas con recursos limitados.
