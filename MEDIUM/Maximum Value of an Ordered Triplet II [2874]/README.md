# Maximum Value of an Ordered Triplet II

## Descripción

El ejercicio "Maximum Value of an Ordered Triplet II" plantea el reto de encontrar el mayor valor posible derivado de todos los tripletes ordenados de índices `(i, j, k)` dentro de una lista de enteros `nums`, cumpliendo la condición `i < j < k`. Para cada triplete, el valor se calcula con la fórmula `(nums[i] - nums[j]) * nums[k]`. Si todas las combinaciones posibles arrojan un valor negativo, se debe retornar `0`. Esta tarea resulta interesante por la necesidad de optimizar la búsqueda de la mejor combinación sin tener que evaluar todas las posibles en un enfoque de fuerza bruta, especialmente dado el tamaño permitido del array.

## Implementación

La implementación en Python utiliza una clase `Solution` con un método `maximumTripletValue` que evalúa eficientemente el valor máximo sin necesidad de emplear tres bucles anidados. La clave del algoritmo reside en mantener actualizados dos valores durante una única pasada por el array: el número máximo encontrado hasta cierto punto (`max_num`) y la diferencia máxima calculada hasta el momento entre ese número máximo y un valor posterior (`max_diff`). Estos se utilizan para calcular el valor del triplete de manera progresiva.

## Detalles de la implementación

- **Variable `max_num`:** Se mantiene el valor máximo encontrado hasta el índice actual, que representa posibles valores de `nums[i]` para futuras comparaciones.
- **Variable `max_diff`:** Se utiliza para almacenar la mejor diferencia encontrada hasta ahora entre un `nums[i]` anterior y el valor actual `nums[j]`, lo que permitirá calcular con eficiencia el valor de `(nums[i] - nums[j])`.
- **Valor del triplete:** En cada iteración, se evalúa el valor potencial del triplete utilizando la fórmula `max_diff * nums[k]`, siendo `nums[k]` el valor actual del array.
- **Eficiencia:** El algoritmo realiza una única pasada sobre el array (`O(n)`), lo que representa una mejora significativa frente al enfoque cúbico clásico, especialmente útil cuando el tamaño del array es elevado (hasta 10⁵ elementos).

## Uso

Para utilizar este código, simplemente hay que definir el array de enteros `nums`, instanciar un objeto de la clase `Solution` y llamar al método `maximumTripletValue` pasándole el array como argumento.

```python
if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]

    sol = Solution()
    max_triplet_value = sol.maximumTripletValue(nums)
    print(max_triplet_value)  # Output: 77
```

## Conclusión

El ejercicio "Maximum Value of an Ordered Triplet II" proporciona un ejemplo claro de cómo optimizar un problema que inicialmente podría parecer de complejidad cúbica, gracias al uso de estrategias como el almacenamiento de máximos parciales y diferencias acumuladas. Este enfoque no solo mejora el rendimiento, sino que también pone en práctica principios clave de optimización algorítmica. Esta solución es especialmente útil en contextos donde el tamaño de los datos puede ser grande y se requiere eficiencia sin sacrificar precisión en los resultados.
