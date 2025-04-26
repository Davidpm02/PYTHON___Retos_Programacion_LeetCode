# Count of Interesting Subarrays

## Descripción

El ejercicio "Count of Interesting Subarrays" consiste en encontrar el número total de subarrays "interesantes" en un array de enteros. Un subarray se define como interesante si, al contar los elementos que satisfacen la condición `nums[i] % modulo == k`, dicho conteo (`cnt`) cumple que `cnt % modulo == k`. Este problema es representativo de técnicas avanzadas de conteo basadas en prefijos y estructuras de datos eficientes como `defaultdict`, aplicadas en contextos donde las restricciones de tamaño del array requieren soluciones optimizadas.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `countInterestingSubarrays`. Este método emplea un enfoque basado en la utilización de conteo de prefijos (`prefix count`) y el uso de un diccionario para mantener la cantidad de prefijos con un cierto residuo módulo `modulo`, permitiendo calcular en tiempo eficiente el número de subarrays interesantes.

## Detalles de la implementación

- **Uso de prefix count:** Se lleva un conteo acumulativo de cuántos elementos cumplen `nums[i] % modulo == k` hasta la posición actual.
- **Manejo de residuos:** Se utiliza un diccionario `count_map` para registrar la frecuencia de residuos obtenidos al aplicar el operador módulo sobre el contador de prefijos.
- **Condición de interés:** Para cada posición, se calcula el residuo que debe haber aparecido anteriormente para formar un subarray interesante y se actualiza el resultado en consecuencia.
- **Inicialización especial:** Se inicializa `count_map[0] = 1` para considerar subarrays que comienzan desde el primer índice del array.

## Uso

Para utilizar este código, simplemente se deben definir el array `nums`, así como los valores de `modulo` y `k`, luego crear una instancia de la clase `Solution` y llamar al método `countInterestingSubarrays` pasando estos parámetros.

```python
if __name__ == "__main__":
    nums = [3, 1, 9, 6]
    modulo = 3
    k = 0

    sol = Solution()
    interesting_subarrays = sol.countInterestingSubarrays(nums, modulo, k)
    print(interesting_subarrays)  # Output: 2
```

## Conclusión

El ejercicio "Count of Interesting Subarrays" pone en práctica técnicas de conteo eficiente basadas en prefijos y modularidad, herramientas fundamentales en la optimización de problemas de subarrays. La implementación propuesta aprovecha la estructura de datos defaultdict para registrar ocurrencias y encontrar relaciones previas necesarias, asegurando así un tiempo de ejecución adecuado incluso para arrays de gran tamaño. Esta estrategia no solo resulta eficaz para este problema concreto, sino que también refuerza habilidades esenciales para abordar desafíos de programación que involucran análisis de secuencias y gestión de residuos.
