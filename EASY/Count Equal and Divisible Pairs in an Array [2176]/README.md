# Count Equal and Divisible Pairs in an Array

## Descripción

El ejercicio **"Count Equal and Divisible Pairs in an Array"** tiene como objetivo contar el número de pares de índices `(i, j)` en un array de enteros `nums` que cumplan con dos condiciones específicas:

1. Los elementos en las posiciones `i` y `j` sean iguales, es decir, `nums[i] == nums[j]`.

2. El producto de los índices `(i * j)` sea divisible entre un número entero dado `k`.

Este problema combina aspectos de comparación de valores con propiedades aritméticas de los índices, lo que lo hace interesante desde el punto de vista de eficiencia y lógica condicional.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, utilizando un enfoque de fuerza bruta mediante dos bucles anidados. Esta técnica es adecuada debido a las restricciones moderadas del problema (`n <= 100`). Se exploran todas las combinaciones posibles de índices `(i, j)` asegurando que `i < j` y se evalúan ambas condiciones mencionadas.

## Detalles de la implementación

- **Recorrido completo:** Se recorren todos los pares posibles de índices utilizando bucles anidados, asegurando que `i < j`.
- **Comparación de elementos:** Se verifica si `nums[i] == nums[j]`.
- **Divisibilidad del producto de índices:** Se comprueba si `(i * j) % k == 0`.
- **Contador:** Se incrementa un contador cada vez que se cumplen ambas condiciones para un par dado.
- **Complejidad temporal:** Dado que se evalúan todos los pares posibles, la complejidad temporal es O(n²), lo cual es aceptable dada la cota máxima de `n = 100`.

## Uso

Para utilizar este código, basta con definir el array `nums` y el entero `k`, crear una instancia de la clase `Solution`, y llamar al método `countPairs`.

```python
if __name__ == "__main__":
    nums = [3,1,2,2,2,1,3]
    k = 2

    sol = Solution()
    result = sol.countPairs(nums, k)
    print(result)  # Output esperado: 4
```

## Conclusión

El ejercicio "Count Equal and Divisible Pairs in an Array" permite practicar la combinación de condiciones lógicas sobre elementos e índices dentro de un array. Aunque su implementación básica recurre a una doble iteración, resulta eficiente y clara gracias a las restricciones del problema. Además, refuerza el análisis cuidadoso de las condiciones impuestas y su correcta implementación. Esta solución también sirve como base para futuras optimizaciones si se enfrentan casos de entrada más grandes, mediante técnicas como el uso de estructuras de conteo o mapeo de índices por valor.
