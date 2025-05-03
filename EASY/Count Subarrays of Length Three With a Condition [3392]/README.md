# Count Subarrays of Length Three With a Condition

## Descripción

El ejercicio **"Count Subarrays of Length Three With a Condition"** consiste en recorrer un array de números enteros y contar cuántos subarrays de longitud 3 cumplen una condición específica: la suma del primer y tercer elemento del subarray debe ser exactamente igual a la mitad del valor del elemento central.

Este tipo de ejercicio está diseñado para evaluar habilidades en la manipulación de arrays, análisis de condiciones matemáticas dentro de estructuras secuenciales y la capacidad para implementar soluciones eficientes usando bucles y condicionales.

## Implementación

La solución está implementada en Python mediante una clase llamada `Solution` que contiene el método `countSubarrays`. Este método recorre el array original evaluando subarrays de tres elementos consecutivos, y verifica si cumplen con la condición mencionada.

## Detalles de la implementación

- **Recorrido del array:** Se utiliza un bucle `for` que comienza desde el índice 1 hasta `len(nums) - 2`, permitiendo verificar todos los subarrays posibles de longitud 3 sin salirse del rango del array.
- **Evaluación de la condición:** Para cada subarray `[a, b, c]`, se verifica si la suma de `a + c` es igual a `b / 2`.
- **Contador de subarrays válidos:** Cada vez que se cumple la condición, se incrementa un contador que finalmente se retorna como resultado del método.

## Uso

Para utilizar este código, simplemente hay que definir el array de números enteros `nums`, crear una instancia de la clase `Solution`, y llamar al método `countSubarrays` pasando dicho array como argumento. El método devolverá el número de subarrays válidos de longitud 3 que cumplan la condición establecida.

```python
if __name__ == "__main__":
    nums = [1, 2, 1, 4, 1]

    sol = Solution()
    count = sol.countSubarrays(nums)
    print(count)  # Output: 1
```

## Conclusión

El ejercicio "Count Subarrays of Length Three With a Condition" es una excelente práctica para reforzar la lógica de programación y el análisis matemático aplicado a estructuras de datos secuenciales. La solución implementada es simple, legible y eficiente, cumpliendo con las restricciones de tamaño del array. Además, permite familiarizarse con conceptos como subarrays, evaluación de condiciones personalizadas y buenas prácticas de programación orientada a objetos en Python.
