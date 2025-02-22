# Find Elements in a Contaminated Binary Tree

## Descripción

El ejercicio "Find Elements in a Contaminated Binary Tree" consiste en recuperar un árbol binario contaminado en el que todos los valores de los nodos han sido cambiados a `-1`. Se debe reconstruir el árbol siguiendo reglas específicas y luego implementar una función para determinar si un valor dado está presente en el árbol recuperado.

Las reglas de recuperación del árbol son:

- El nodo raíz (`root`) tiene el valor `0`.
- Si un nodo tiene un valor `x`:
  - Su hijo izquierdo (`left`) tendrá el valor `2 * x + 1`.
  - Su hijo derecho (`right`) tendrá el valor `2 * x + 2`.

Se debe implementar la clase `FindElements` que permite:

1. Inicializar un árbol binario contaminado y recuperarlo.
2. Verificar si un valor dado existe en el árbol recuperado.

## Implementación

La solución se desarrolla en Python y define la clase `FindElements`, la cual contiene los siguientes métodos:

- **`__init__(self, root: Optional[TreeNode])`**: Constructor que recibe la raíz de un árbol contaminado e inicia el proceso de recuperación.
- **`recover_tree(self, node: Optional[TreeNode], value: int)`**: Método recursivo que asigna los valores correctos a los nodos y los almacena en un conjunto.
- **`find(self, target: int) -> bool`**: Método que verifica si un valor `target` está presente en el conjunto de valores recuperados.

La implementación usa un conjunto (`set`) para almacenar los valores del árbol recuperado, lo que permite realizar búsquedas en tiempo constante `O(1)`.

## Uso

Para utilizar este código, se debe proporcionar un árbol binario contaminado con valores `-1`. Luego, se instancia la clase `FindElements`, que reconstruye el árbol según las reglas establecidas. Posteriormente, se puede llamar al método `find` para verificar si un valor específico existe en el árbol recuperado.

```python
if __name__ == "__main__":
    root = TreeNode(-1, None, TreeNode(-1))  # Ejemplo de árbol contaminado
    find_elements = FindElements(root)
    
    print(find_elements.find(1))  # Output: False
    print(find_elements.find(2))  # Output: True
```

## Conclusión

El ejercicio "Find Elements in a Contaminated Binary Tree" presenta un desafío interesante de recuperación y búsqueda eficiente en estructuras de datos. La solución implementada aprovecha la recursividad para reconstruir el árbol y un conjunto (`set`) para almacenar los valores recuperados, permitiendo consultas eficientes en `O(1)`. Este enfoque es útil en problemas relacionados con la manipulación y validación de estructuras jerárquicas en informática.
