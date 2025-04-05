# Maximum Value of an Ordered Triplet I

## Descripción

El ejercicio "Maximum Value of an Ordered Triplet I" consiste en encontrar el valor máximo posible de entre todos los tripletes ordenados de índices `(i, j, k)` de una lista de enteros `nums`, cumpliendo la condición `i < j < k`. El valor de cada triplete se calcula mediante la fórmula `(nums[i] - nums[j]) * nums[k]`. Si todos los posibles valores resultan ser negativos, el método debe devolver `0`. Este tipo de problema pone a prueba la capacidad para explorar combinaciones eficientes y comprender el impacto de operaciones aritméticas sobre subconjuntos ordenados.

## Implementación

La implementación está desarrollada en Python mediante una clase `Solution` que expone el método `maximumTripletValue`. Este método recorre todos los tripletes posibles dentro del array `nums`, calcula el valor correspondiente según la fórmula definida y mantiene actualizado el valor máximo encontrado hasta el momento.

## Detalles de la implementación

- **Recorrido por tripletes:** Se utilizan tres bucles anidados para recorrer todos los tripletes `(i, j, k)` posibles dentro del array, respetando la condición `i < j < k`.
- **Cálculo de valor del triplete:** Para cada combinación, se calcula el valor con la fórmula `(nums[i] - nums[j]) * nums[k]`.
- **Comparación y actualización:** Se compara el resultado obtenido con el valor máximo actual. Si es mayor, se actualiza.
- **Condición de retorno:** En caso de que todos los valores sean negativos, el valor por defecto de `max_value` permanece en `0`, tal como se especifica en el enunciado.

## Uso

Para utilizar este código, se debe definir un array de enteros `nums`, crear una instancia de la clase `Solution` y llamar al método `maximumTripletValue`, pasando dicho array como parámetro.

```python
if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]

    sol = Solution()
    max_triplet_value = sol.maximumTripletValue(nums)
    print(max_triplet_value)  # Output: 77
```

## Conclusión

El ejercicio "Maximum Value of an Ordered Triplet I" permite explorar todas las posibles combinaciones de tripletes en un array de enteros para encontrar el valor máximo bajo una fórmula definida. Aunque la implementación actual tiene una complejidad cúbica, es válida dado el límite de tamaño del array (hasta 100 elementos). Este tipo de ejercicios fortalece la capacidad de análisis y la manipulación de subíndices, así como el uso de estructuras de control para encontrar soluciones óptimas en espacios de búsqueda limitados.
