# Merge k Sorted Lists

## Descripción

El propósito de este ejercicio es fusionar k listas enlazadas, cada una ordenada en orden ascendente, en una única lista enlazada ordenada. La implementación se realiza en Python y se aprovecha de características como la recursión y la comprensión de listas para lograr el objetivo de manera eficiente y clara.

## Implementación

El código consta de una clase principal llamada Solution que contiene el método mergeKLists. Este método toma una lista de listas enlazadas y las fusiona en una única lista enlazada ordenada.

Para lograr esto, se define una clase auxiliar ListNode que representa un nodo en una lista enlazada, conteniendo un valor y un enlace al siguiente nodo.

El método mergeKLists funciona en varios pasos:

* **Extracción de valores**: Se recorren todos los nodos de cada lista enlazada y se extraen los valores para almacenarlos en una lista plana.
* **Ordenamiento**: Se ordena la lista plana de valores.
* **Reconstrucción de la lista enlazada**: Se construye una nueva lista enlazada a partir de la lista de valores ordenados.

Se emplean dos funciones recursivas auxiliares para procesar y crear nodos de la lista enlazada.

## Uso

Para utilizar esta solución, instancie un objeto de la clase Solution y llame al método mergeKLists pasando la lista de cabezas de las listas enlazadas como argumento. El método devolverá la cabeza de la lista enlazada resultante, que estará ordenada.

## Ejemplo

```python
if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    solution = Solution()
    sol = solution.mergeKLists(lists=lists)
    print(sol)  # El output mostrará los nodos de la lista enlazada resultante
```

## Conclusión

Este ejercicio demuestra una aplicación práctica de estructuras de datos como listas enlazadas y técnicas de programación como la recursión y la ordenación para resolver problemas complejos de manera eficiente. La solución es flexible y puede manejar diferentes números de listas y tamaños de lista, lo que la hace robusta para diversos escenarios de uso.
