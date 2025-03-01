# Construct Binary Tree from Preorder and Postorder Traversal

## Descripción

El ejercicio "Construct Binary Tree from Preorder and Postorder Traversal" consiste en reconstruir un árbol binario a partir de dos listas de enteros: `preorder` y `postorder`, que representan los recorridos en preorden y postorden del mismo árbol.

El resultado debe ser el árbol original, aunque si existen varias soluciones válidas, se permite devolver cualquiera de ellas.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` que contiene el método `constructFromPrePost`. Este método emplea recursión para reconstruir el árbol dividiendo los nodos en subárboles izquierdo y derecho basándose en la información de los recorridos dados.

### Detalles de la implementación

- **Definición de la estructura del árbol:** Se utiliza la clase `TreeNode` para representar los nodos del árbol.
- **Caso base:** Si la lista `preorder` está vacía, la función retorna `None`.
- **Construcción del árbol:**
  - Se toma el primer elemento de `preorder` como la raíz del árbol.
  - Se encuentra la posición del primer nodo del subárbol izquierdo en `postorder`.
  - Se dividen las listas para construir recursivamente los subárboles izquierdo y derecho.

## Uso

Para utilizar este código, simplemente se deben definir las listas `preorder` y `postorder`, y luego crear una instancia de la clase `Solution`. Se llama al método `constructFromPrePost` con estas listas para obtener el árbol resultante.

```python
if __name__ == "__main__":
    preorder = [1,2,4,5,3,6,7]
    postorder = [4,5,2,6,7,3,1]

    sol = Solution()
    root = sol.constructFromPrePost(preorder, postorder)
    print(root.val)  # Output: 1
```

## Conclusión

El ejercicio "Construct Binary Tree from Preorder and Postorder Traversal" es un problema clásico en la reconstrucción de estructuras de datos a partir de sus representaciones parciales. Su resolución mediante recursión es elegante y eficiente, permitiendo comprender mejor la relación entre distintos tipos de recorridos de árboles binarios. Esta solución es aplicable en diversos escenarios, como la interpretación de expresiones matemáticas o la optimización de estructuras jerárquicas en informática.
