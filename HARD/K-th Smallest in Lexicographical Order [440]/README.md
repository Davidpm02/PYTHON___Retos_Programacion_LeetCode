# K-th Smallest in Lexicographical Order

## Descripción

El ejercicio **"K-th Smallest in Lexicographical Order"** consiste en encontrar el k-ésimo número entero más pequeño en orden lexicográfico dentro del rango `[1, n]`. Esto significa que los números se ordenan como si fueran cadenas de texto, no por su valor numérico tradicional. Por ejemplo, en el rango `[1, 13]`, el orden lexicográfico sería `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`. El objetivo es devolver el número que ocupa la posición k en esta secuencia ordenada.

Este problema es relevante para entender cómo aplicar búsquedas y conteos eficientes sobre espacios grandes de números, optimizando mediante técnicas inspiradas en árboles prefix (tries) y evitando la enumeración directa.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método principal `findKthNumber`. Este método utiliza una estrategia basada en contar cuántos números existen bajo un cierto prefijo lexicográfico para avanzar de manera eficiente hacia el k-ésimo número.

### Detalles de la implementación

- **Variables iniciales:** Se inicia con `curr = 1` como el primer número lexicográfico y se decrementa `k` en 1, dado que `1` ya representa el primer número.
- **Conteo de nodos:** Se define un método auxiliar `_count_nodes` que calcula cuántos números existen en el rango de prefijos `[prefix, next_prefix)` acotados por `n`.
- **Búsqueda iterativa:** Mientras `k > 0`, se cuenta cuántos números hay bajo el prefijo actual. Si el total es menor o igual a `k`, se avanza al siguiente hermano incrementando el prefijo y reduciendo `k`. Si el bloque contiene el objetivo, se desciende un nivel en el árbol multiplicando el prefijo por 10 y decrementando `k` en 1.
- **Optimización:** Este método evita la enumeración completa, permitiendo operar en rangos grandes como `n` hasta 10^9 con alta eficiencia.

## Uso

Para usar esta solución, basta con definir los valores `n` y `k`, crear una instancia de la clase `Solution` y llamar al método `findKthNumber`. El resultado es el k-ésimo número en orden lexicográfico dentro del rango dado.

```python
if __name__ == "__main__":
    n = 13
    k = 2

    sol = Solution()
    kth_number = sol.findKthNumber(n, k)
    print(kth_number)  # Output: 10
```

## Conclusión

El ejercicio "K-th Smallest in Lexicographical Order" plantea un desafío interesante que combina lógica de conteo y estructuras tipo árbol para encontrar una posición específica en un orden lexicográfico. La solución implementada es eficiente y escalable, evitando búsquedas lineales y usando una técnica que puede ser aplicable a problemas similares de enumeración ordenada en grandes espacios discretos. Además, este enfoque refuerza conceptos de algoritmos avanzados y análisis de prefijos que son útiles en muchos contextos de programación y Machine Learning.
