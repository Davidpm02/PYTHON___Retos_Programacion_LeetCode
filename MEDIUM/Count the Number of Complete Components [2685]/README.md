# Count the Number of Complete Components

## Descripción

El ejercicio "Count the Number of Complete Components" consiste en contar el número de componentes completos dentro de un grafo no dirigido. Un grafo está compuesto por vértices (nodos) y aristas (conexiones entre nodos). En este caso, se nos da un grafo con `n` vértices, numerados desde 0 hasta `n-1`, y una lista de aristas que conectan estos vértices.

Una **componente conectada** es un subconjunto del grafo en el que existe un camino entre cualquier par de vértices dentro de ella. Una **componente completa** es una componente conectada en la que todos los vértices están conectados entre sí, es decir, para una componente de `k` vértices, debe haber exactamente `k * (k - 1) / 2` aristas.

## Implementación

La implementación está realizada en Python utilizando una clase llamada `Solution` que contiene el método `countCompleteComponents`. Este método realiza los siguientes pasos:

1. **Creación de la lista de adyacencia:** Construye un grafo representado por una lista de adyacencia a partir de las aristas proporcionadas.
2. **Búsqueda de componentes conectadas:** Utiliza un algoritmo de búsqueda en profundidad (DFS) para identificar las componentes conectadas en el grafo.
3. **Verificación de componentes completas:** Para cada componente conectada, verifica si el número de aristas es igual al número esperado para una componente completa.
4. **Conteo de componentes completas:** Cuenta cuántas de las componentes conectadas son completas.

### Detalles de la implementación

- **Lista de adyacencia:** Se crea un diccionario `adj` donde cada clave es un vértice y su valor es una lista de vértices adyacentes.
- **DFS (Depth First Search):** Se utiliza DFS para recorrer el grafo y encontrar todas las componentes conectadas.
- **Comprobación de completitud:** Para cada componente, se calcula el número de aristas dentro de la misma y se compara con el número esperado para una componente completa.
- **Conteo de componentes completas:** Se incrementa un contador por cada componente que cumpla con la condición de ser completa.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y luego llamar al método `countCompleteComponents`, proporcionando el número de vértices `n` y la lista de aristas `edges`. El resultado será el número de componentes completas en el grafo.

```python
if __name__ == "__main__":
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]
    
    sol = Solution()
    complete_components_count = sol.countCompleteComponents(n, edges)
    print(complete_components_count)  # Output: 3
```

## Conclusión

El ejercicio "Count the Number of Complete Components" es útil para comprender la teoría de grafos, especialmente en la identificación de componentes conectadas y completas dentro de un grafo no dirigido. El algoritmo implementado es eficiente para grafo de tamaño moderado (hasta 50 vértices), y hace uso de técnicas fundamentales como la búsqueda en profundidad (DFS) para recorrer el grafo y verificar las propiedades de las componentes. Este enfoque no solo refuerza conceptos importantes de grafos, sino que también es aplicable en diversos escenarios de análisis de redes y optimización de estructuras de datos.
