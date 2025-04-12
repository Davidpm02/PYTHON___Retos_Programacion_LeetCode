# Largest Divisible Subset

## Descripción

El ejercicio **"Largest Divisible Subset"** tiene como objetivo encontrar el subconjunto más grande dentro de un conjunto de números enteros positivos, de forma que para cada par de elementos del subconjunto se cumpla una relación de divisibilidad: es decir, uno de los elementos debe ser divisible por el otro. Esta propiedad debe cumplirse para cualquier combinación de elementos en el subconjunto resultante.

Este tipo de problema es relevante en contextos donde se desea trabajar con relaciones de divisibilidad o estructuras jerárquicas basadas en factores, y es una excelente aplicación de algoritmos de programación dinámica.

## Implementación

La solución está desarrollada en Python mediante una clase llamada `Solution`, que implementa el método `largestDivisibleSubset`. Este método toma como entrada una lista de enteros positivos y devuelve el subconjunto más largo que cumpla con la propiedad de divisibilidad mencionada anteriormente.

## Detalles de la implementación

- **Ordenamiento del array:** Se comienza ordenando la lista de números para facilitar la verificación de la divisibilidad, ya que si `a < b` y `b % a == 0`, entonces es más sencillo construir los subconjuntos válidos.

- **Programación dinámica:** Se utiliza un enfoque de programación dinámica para construir los subconjuntos:
  - Se mantiene un array `dp` donde `dp[i]` representa el tamaño del subconjunto más largo que termina en `nums[i]`.
  - Se mantiene un array `prev` que guarda los índices de los elementos anteriores para poder reconstruir el subconjunto al final del proceso.

- **Construcción del subconjunto:** Al finalizar el recorrido, se reconstruye el subconjunto usando los índices almacenados en `prev`, empezando desde el índice que representa el final del subconjunto más largo.

- **Devolución del resultado:** Finalmente, el subconjunto se invierte para presentarlo en orden ascendente, tal como estaba estructurado originalmente.

## Uso

Para utilizar esta solución, simplemente se debe crear una instancia de la clase `Solution`, y luego llamar al método `largestDivisibleSubset` pasando como argumento una lista de enteros positivos.

```python
if __name__ == "__main__":
    nums = [1, 2, 4, 8]

    sol = Solution()
    result = sol.largestDivisibleSubset(nums)
    print(result)  # Output: [1, 2, 4, 8]
```

## Conclusión

El ejercicio "Largest Divisible Subset" representa un excelente caso de aplicación de programación dinámica para resolver problemas de subconjuntos bajo condiciones específicas. La solución implementada aprovecha un enfoque sistemático para construir de manera eficiente el conjunto más largo que respeta la relación de divisibilidad entre sus elementos. Este tipo de algoritmos no solo es útil en competencias de programación, sino también en el desarrollo de sistemas que trabajan con estructuras numéricas jerárquicas o reglas de factorización.
