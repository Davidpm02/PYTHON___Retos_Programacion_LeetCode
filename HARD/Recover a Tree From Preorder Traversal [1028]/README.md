# Recover a Tree From Preorder Traversal

## Descripción

El ejercicio "Recover a Tree From Preorder Traversal" consiste en reconstruir un árbol binario a partir de un recorrido en preorden dado como una cadena de texto. En este recorrido, cada nodo se representa por su valor precedido por una cantidad de guiones que indica su profundidad en el árbol. El objetivo es reconstruir el árbol a partir de esta representación y devolver su raíz.

## Implementación

La implementación se lleva a cabo en Python utilizando una clase `Solution` con el método `recoverFromPreorder`. Este método reconstruye el árbol a partir de la cadena que representa el recorrido en preorden, utilizando una pila para rastrear los nodos y sus profundidades.

## Detalles de la implementación

- **Pila de nodos:** Utilizamos una pila (`stack`) para almacenar temporalmente los nodos a medida que vamos procesando el recorrido. Esto nos permite rastrear los padres de los nodos y sus hijos.
- **Profundidad del nodo:** La cantidad de guiones antes de un número indica la profundidad de ese nodo en el árbol. A medida que procesamos la cadena, ajustamos la pila para reflejar la estructura jerárquica del árbol.
- **Construcción de nodos:** Cada vez que encontramos un valor de nodo, creamos un nuevo `TreeNode` y lo conectamos a su padre adecuado, ya sea como hijo izquierdo o derecho.
- **Recuperación del árbol:** Al final del recorrido, el primer nodo agregado a la pila será la raíz del árbol, que es lo que devuelve el método.

## Uso

Para utilizar este código, simplemente se debe proporcionar la cadena que representa el recorrido en preorden y llamar al método `recoverFromPreorder`. El método devolverá la raíz del árbol reconstruido.

```python
if __name__ == "__main__":
    traversal = "1-2--3--4-5--6--7"

    sol = Solution()
    root = sol.recoverFromPreorder(traversal)
    print(root.val)  # Output: 1
    # El árbol reconstruido será:
    #       1
    #     /   \
    #    2     5
    #   / \   / \
    #  3   4 6   7
```

## Conclusión

El ejercicio "Recover a Tree From Preorder Traversal" proporciona una forma eficiente de reconstruir un árbol binario a partir de un recorrido en preorden. Utilizando una pila para rastrear los nodos y sus profundidades, podemos reconstruir la estructura jerárquica del árbol de manera precisa y eficiente. Este enfoque refuerza conceptos importantes de manipulación de árboles binarios y es una buena práctica en problemas de estructuras de datos en programación.
