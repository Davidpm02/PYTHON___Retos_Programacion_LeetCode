# Making a Large Island

## Descripción

El ejercicio "Making a Large Island" consiste en encontrar el tamaño de la isla más grande en una matriz binaria de tamaño `n x n` después de cambiar como máximo un `0` a `1`. Una isla se define como un grupo de `1s` conectados en dirección horizontal o vertical.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `largestIsland`. Este método explora la matriz, identifica las islas existentes y evalúa el impacto de convertir un `0` en un `1` para maximizar el tamaño de la isla más grande.

## Detalles de la implementación

- **Exploración de islas:** Se utiliza un algoritmo DFS para identificar y etiquetar cada isla con un identificador único y calcular su tamaño.
- **Almacenamiento de tamaños:** Se mantiene un diccionario que asocia cada identificador de isla con su tamaño.
- **Evaluación de cambios:** Se recorre la matriz para evaluar cómo la conversión de un `0` a `1` puede maximizar el tamaño de la isla.
- **Cálculo del tamaño máximo:** Se suman los tamaños de las islas conectadas a un `0` para determinar el mayor tamaño posible después de la conversión.

## Uso

Para utilizar este código, simplemente se debe definir la matriz binaria `grid`, y luego crear una instancia de la clase `Solution`. Se llama al método `largestIsland` con la matriz y se obtiene el tamaño de la isla más grande después de cambiar como máximo un `0` a `1`.

```python
if __name__ == "__main__":
    grid = [[1, 0], [0, 1]]
    
    sol = Solution()
    max_island_size = sol.largestIsland(grid)
    print(max_island_size)  # Output: 3
```

## Conclusión

El ejercicio "Making a Large Island" presenta un desafío interesante en términos de exploración de grafos y optimización de recursos en una matriz binaria. La solución implementada utiliza una combinación de DFS y evaluación de conectividad para encontrar la mejor forma de expandir una isla. Este enfoque permite determinar el impacto de convertir un solo `0` en `1`, logrando así la mayor expansión posible de una isla dentro de la matriz dada.
