# Lowest Common Ancestor of Deepest Leaves

## Descripción

El ejercicio "Lowest Common Ancestor of Deepest Leaves" tiene como objetivo encontrar el ancestro común más bajo (Lowest Common Ancestor, LCA) de todas las hojas más profundas de un árbol binario. En este contexto, una hoja se define como un nodo sin hijos, y la profundidad de un nodo se determina como la distancia desde la raíz (que tiene profundidad 0). El LCA es el nodo más profundo del cual todos los nodos hoja más profundos descienden.

Este problema es particularmente interesante ya que combina los conceptos de profundidad de árbol, hojas y la búsqueda de ancestros comunes, resultando útil en diversas aplicaciones como bases de datos jerárquicas, estructuras de árbol para organización de archivos o gestión de árboles genealógicos.

## Implementación

La implementación en Python utiliza una clase `Solution` con el método `lcaDeepestLeaves`, el cual resuelve el problema de forma recursiva a través de una función auxiliar `find_lca_and_depth`. Esta función explora el árbol de manera descendente (postorden), evaluando la profundidad de cada subárbol y determinando el punto de convergencia más profundo para las hojas con mayor profundidad.

## Detalles de la implementación

- **Estructura del nodo:** Se define una clase `TreeNode` que representa los nodos del árbol, con atributos para el valor del nodo y punteros a los hijos izquierdo y derecho.
- **Función auxiliar:** `find_lca_and_depth` devuelve una tupla compuesta por el nodo que representa el LCA de las hojas más profundas encontradas en el subárbol actual, y su profundidad correspondiente.
- **Comparación de profundidades:** Si las profundidades de los subárboles izquierdo y derecho son iguales, el nodo actual es el LCA. En caso contrario, se retorna el LCA del subárbol más profundo.
- **Complejidad:** La solución realiza una única pasada por cada nodo del árbol, resultando en una complejidad temporal de `O(n)` y espacial de `O(h)`, donde `n` es el número de nodos y `h` la altura del árbol.

## Uso

Para utilizar este código, se debe construir primero el árbol binario utilizando instancias de la clase `TreeNode`, luego instanciar la clase `Solution` y llamar al método `lcaDeepestLeaves` pasando como argumento la raíz del árbol.

```python
if __name__ == "__main__":
    # Ejemplo de construcción manual del árbol binario
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    sol = Solution()
    lca_node = sol.lcaDeepestLeaves(root)
    print(lca_node.val)  # Output esperado: 2
```

## Conclusión

El ejercicio "Lowest Common Ancestor of Deepest Leaves" es un ejemplo claro de cómo aplicar técnicas recursivas y traversal postorden para resolver problemas relacionados con la estructura jerárquica de árboles binarios. Esta implementación permite identificar eficientemente el nodo más profundo que actúa como punto común para todas las hojas más alejadas, haciendo uso óptimo de la recursividad y del almacenamiento parcial de resultados durante el recorrido del árbol. La solución es robusta, clara y extensible a variantes más complejas del problema.
