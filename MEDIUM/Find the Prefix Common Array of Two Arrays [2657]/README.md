# Find the Prefix Common Array of Two Arrays

## Descripción

El ejercicio **"Find the Prefix Common Array of Two Arrays"** consiste en calcular, para dos permutaciones de enteros de tamaño `n`, un arreglo denominado "array común de prefijos" (Prefix Common Array). Este arreglo tiene las siguientes propiedades:

- Para cada índice `i`, el valor en la posición `C[i]` corresponde a la cantidad de números que están presentes en los prefijos de las dos permutaciones `A` y `B`, es decir, en las subsecuencias desde el índice 0 hasta `i`.

Una permutación de longitud `n` se define como una secuencia de números enteros que contiene exactamente una vez cada entero del 1 al `n`. Este ejercicio involucra el uso de conjuntos para calcular intersecciones en los prefijos de ambas permutaciones.

## Implementación

La solución utiliza Python y se encuentra dentro de una clase `Solution`, que incluye el método `findThePrefixCommonArray`. Este método realiza lo siguiente:

1. **Definición de variables:** Se inicializa la longitud de las listas y una lista vacía para almacenar el arreglo común de prefijos.
2. **Cálculo por índices:** Se itera a través de los índices de las listas `A` y `B`. En cada paso, se toma la intersección de los conjuntos formados por los elementos desde el índice 0 hasta el índice actual `i` y se almacena la longitud de dicha intersección en la lista resultado.
3. **Complejidad:** El método utiliza operaciones de intersección en conjuntos, lo que lo hace eficiente para manejar las restricciones del problema.

## Uso

Para ejecutar este código, define las listas de enteros `A` y `B`. Luego, crea una instancia de la clase `Solution` y llama al método `findThePrefixCommonArray` con dichas listas como argumentos:

```python
if __name__ == "__main__":
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]

    sol = Solution()
    result = sol.findThePrefixCommonArray(A, B)
    print(result)  # Debería imprimir el arreglo común de prefijos
```

## Conclusión

El ejercicio "Find the Prefix Common Array of Two Arrays" destaca por su énfasis en el cálculo eficiente de intersecciones entre prefijos de dos listas, lo que puede extrapolarse a problemas más complejos relacionados con datos ordenados o secuenciales. La implementación basada en conjuntos es clara y mantiene una complejidad manejable, siendo una herramienta útil para analizar relaciones entre subconjuntos de datos en distintas aplicaciones.
