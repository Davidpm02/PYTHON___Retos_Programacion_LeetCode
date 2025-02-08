# Tuple with Same Product

## Descripción

El ejercicio "Tuple with Same Product" consiste en encontrar la cantidad de tuplas \((a, b, c, d)\) en un arreglo de enteros distintos y positivos, tales que el producto de dos elementos sea igual al producto de otros dos elementos en la lista. Es decir, se deben contar todas las combinaciones donde se cumpla la condición:

\[ a \times b = c \times d \]

manteniendo la restricción de que los elementos sean distintos entre sí.

Este tipo de problema es relevante en el análisis de combinaciones y productos dentro de estructuras de datos numéricas, siendo útil en algoritmos de búsqueda y optimización.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con el método `tupleSameProduct`. La estrategia utilizada se basa en el almacenamiento de productos de pares en un diccionario para agilizar la búsqueda y conteo de combinaciones válidas.

### Detalles de la implementación

- **Uso de un diccionario:** Se emplea un `defaultdict` para almacenar la cantidad de veces que se ha encontrado cada producto de dos números dentro de la lista.
- **Generación de pares:** Se recorren todos los pares posibles dentro de la lista, calculando su producto y almacenándolo en el diccionario.
- **Cálculo de combinaciones:** Cada vez que se encuentra un producto previamente registrado, se suman las combinaciones posibles según el número de veces que ha aparecido dicho producto.
- **Factor de multiplicación:** Por cada coincidencia se suman 8 tuplas válidas, debido a las permutaciones posibles de los elementos en la ecuación \( a \times b = c \times d \).

## Uso

Para utilizar este código, se debe definir una lista de números enteros distintos y positivos, y luego crear una instancia de la clase `Solution`. Finalmente, se llama al método `tupleSameProduct` pasando la lista como argumento.

```python
if __name__ == "__main__":
    nums = [2, 3, 4, 6]
    
    sol = Solution()
    result = sol.tupleSameProduct(nums)
    print(result)  # Output: 8
```

## Conclusión

El ejercicio "Tuple with Same Product" es un problema de combinatoria que se puede resolver eficientemente utilizando estructuras de datos como diccionarios para almacenar productos previamente calculados. El enfoque basado en contar la frecuencia de productos y calcular las combinaciones evita el cálculo redundante y mejora la eficiencia del algoritmo. Esta solución es útil para problemas similares donde se necesita encontrar patrones en productos de pares dentro de una colección de números.
