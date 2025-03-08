# Find Missing and Repeated Values

## Descripción

El ejercicio "Find Missing and Repeated Values" consiste en identificar un número que se repite dos veces y otro número que falta en una matriz cuadrada de tamaño n x n. La matriz contiene valores en el rango [1, n²], asegurando que todos los números aparecen exactamente una vez, excepto uno que se repite y otro que está ausente.

Se debe devolver un arreglo de dos elementos donde:

* ans[0] es el número repetido.

* ans[1] es el número faltante.

Este problema es importante en la detección de errores en datos y puede aplicarse en sistemas que requieren validaciones de integridad en conjuntos de datos numéricos.

## Implementación

La solución se implementa en Python dentro de una clase Solution, que contiene el método findMissingAndRepeatedValues. La estrategia utilizada es recorrer la matriz y emplear un diccionario para contar las ocurrencias de cada número dentro del rango esperado.

## Detalles de la implementación

1. Inicialización de un diccionario de conteo: Se crea un diccionario donde cada número en el rango [1, n²] tiene inicialmente un valor de 0.

2. Recorrido de la matriz: Se cuentan las apariciones de cada número en la matriz.

3. Identificación del número repetido y del número faltante: Se recorren las frecuencias para encontrar el número que aparece dos veces y el que no aparece.

## Uso

Para ejecutar el código, se debe instanciar la clase Solution y llamar al método findMissingAndRepeatedValues, proporcionando la matriz grid.

```python
if __name__ == "__main__":
    grid = [[1,3],[2,2]]

    sol = Solution()
    result = sol.findMissingAndRepeatedValues(grid)
    print(result)  # Output: [2, 4]
```

## Conclusión

El ejercicio "Find Missing and Repeated Values" permite aplicar técnicas de conteo eficiente para detectar errores en conjuntos de datos estructurados. La solución propuesta emplea una estructura de datos adecuada (diccionario) para optimizar la búsqueda de los valores deseados. Este enfoque es aplicable en situaciones donde se requiere verificar la integridad de datos en sistemas de almacenamiento y transmisión.
