# Count Complete Subarrays in an Array

## Descripción

El ejercicio "Count Complete Subarrays in an Array" consiste en determinar cuántos subarrays completos existen en un array dado de números enteros positivos. Un subarray se considera completo si el número de elementos distintos que contiene es igual al número total de elementos distintos del array original. Este tipo de problemas es muy común en el análisis de datos secuenciales y en el desarrollo de algoritmos de búsqueda y agrupamiento en estructuras de datos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `countCompleteSubarrays`. Este método explora todos los posibles subarrays, verifica su condición de completitud y mantiene un contador del número de subarrays que cumplen con esta propiedad.

## Detalles de la implementación

- **Detección de elementos distintos:** Inicialmente, se calcula el número total de elementos distintos en el array completo utilizando un conjunto (`set`).
- **Recorrido de subarrays:** Se iteran todos los posibles subarrays utilizando dos bucles anidados para definir los inicios y los finales de los subarrays.
- **Rastreo de elementos:** Se utiliza un conjunto temporal para almacenar los elementos distintos del subarray actual durante su expansión.
- **Verificación de condición:** Cada vez que el número de elementos distintos en el subarray iguala al número de elementos distintos del array original, se contabilizan todos los subarrays que comienzan en la posición actual y terminan a partir de este punto.
- **Optimización:** Una vez encontrada una coincidencia completa, se evita seguir expandiendo el subarray innecesariamente para ahorrar tiempo de ejecución.

## Uso

Para utilizar este código, simplemente se debe definir el array de números `nums`, crear una instancia de la clase `Solution`, y llamar al método `countCompleteSubarrays` pasando dicho array.

```python
if __name__ == "__main__":
    nums = [1, 3, 1, 2, 2]

    sol = Solution()
    result = sol.countCompleteSubarrays(nums)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Count Complete Subarrays in an Array" proporciona una excelente oportunidad para practicar técnicas de exploración de subarrays, manejo de estructuras de datos dinámicas como los conjuntos (set) y optimización de búsquedas en arrays. El enfoque implementado es eficiente considerando el tamaño de los datos y ofrece una solución clara y estructurada que refuerza habilidades fundamentales de programación orientadas al análisis de datos secuenciales.
