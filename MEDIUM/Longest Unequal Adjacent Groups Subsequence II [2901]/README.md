# Longest Unequal Adjacent Groups Subsequence II

## Descripción

El ejercicio **"Longest Unequal Adjacent Groups Subsequence II"** consiste en seleccionar la subsecuencia más larga posible de palabras, cumpliendo dos condiciones clave entre cada par de palabras consecutivas en dicha subsecuencia:

1. **Pertenencia a grupos distintos**: Las palabras deben estar asociadas a identificadores de grupo diferentes.
2. **Distancia de Hamming igual a 1**: Las palabras deben tener la misma longitud y diferir exactamente en un único carácter.

Este tipo de problema es relevante en tareas donde se requiere detectar transformaciones mínimas entre elementos categorizados, como en procesamiento de cadenas, análisis de mutaciones o clasificación con restricciones.

## Implementación

La implementación está desarrollada en Python, encapsulada dentro de la clase `Solution`, con el método principal `getWordsInLongestSubsequence`.

### Detalles de la implementación

- **Función de distancia de Hamming**: Se define una función auxiliar para calcular la distancia de Hamming entre dos cadenas, comparando carácter a carácter.
- **Estrategia de programación dinámica**: 
  - Se mantiene un vector `dp[i]` para almacenar la longitud máxima de la subsecuencia que termina en la posición `i`.
  - Un vector `prev[i]` ayuda a rastrear el índice anterior en la subsecuencia óptima.
- **Condiciones de actualización**:
  - Solo se considera ampliar una subsecuencia si las palabras tienen la misma longitud, su distancia de Hamming es exactamente 1 y pertenecen a grupos diferentes.
- **Reconstrucción de la subsecuencia**: Una vez completadas las iteraciones, se rastrea hacia atrás desde el índice con la subsecuencia más larga, reconstruyendo el camino óptimo.

Este enfoque garantiza una exploración eficiente de todas las posibles subsecuencias que respeten las restricciones impuestas.

## Uso

Para utilizar este código, simplemente se deben definir las listas `words` y `groups`, crear una instancia de la clase `Solution` y llamar al método `getWordsInLongestSubsequence`:

```python
if __name__ == "__main__":
    words = ["bab", "dab", "cab"]
    groups = [1, 2, 2]

    sol = Solution()
    result = sol.getWordsInLongestSubsequence(words, groups)
    print(result)  # Posibles salidas: ["bab", "cab"] o ["bab", "dab"]
```

## Conclusión

El ejercicio "Longest Unequal Adjacent Groups Subsequence II" permite poner en práctica conceptos importantes como el uso de programación dinámica, cálculo de distancia de Hamming y el manejo de restricciones múltiples en subsecuencias. La solución presentada es eficiente y escalable para un tamaño de entrada razonable (hasta 1000 palabras). Además, ilustra cómo aplicar estrategias algorítmicas para extraer patrones relevantes bajo condiciones específicas, lo que es clave en tareas de análisis de secuencias o en contextos de clasificación avanzada.
