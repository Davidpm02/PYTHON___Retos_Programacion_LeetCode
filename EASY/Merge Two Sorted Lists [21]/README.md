# Merge Two Sorted Lists

## Descripción

El ejercicio "Merge Two Sorted Lists" consiste en fusionar dos listas enlazadas que están ordenadas. El resultado debe ser una única lista enlazada ordenada que contenga todos los elementos de las dos listas originales. Este problema es común en entrevistas técnicas y es fundamental para entender el manejo de estructuras de datos como las listas enlazadas.

## Implementación

La implementación se realiza en Python utilizando el tipo `ListNode`, que representa un nodo en una lista enlazada. La clase `Solution` contiene el método `mergeTwoLists`, el cual acepta dos nodos, `list1` y `list2`, que son las cabezas de las dos listas enlazadas a fusionar.

### Detalles de la implementación

* **Clase ListNode**: Utilizada para definir la estructura de un nodo de lista enlazada, incluyendo un valor y un enlace al siguiente nodo.

* **Método mergeTwoLists**: Este método compara los valores de los nodos actuales de ambas listas y agrega el nodo de menor valor a la nueva lista fusionada. El proceso se repite hasta que todos los nodos de ambas listas han sido procesados.

El código asegura que todos los nodos se procesen adecuadamente, y al final, si una lista aún contiene nodos mientras la otra no, estos nodos restantes se añaden directamente al final de la lista fusionada.

## Uso

Para utilizar este código, primero debe definirse la estructura de las listas enlazadas que se desean fusionar. Después, se crea una instancia de `Solution` y se llama al método `mergeTwoLists` con las cabezas de las dos listas. El método devolverá la cabeza de la lista enlazada resultante.

```python
if __name__ == "__main__":
    # Creación de las listas enlazadas de ejemplo
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    # Instancia de la solución y ejecución del método
    solution = Solution()
    merged_list_head = solution.mergeTwoLists(list1, list2)

    # Impresión de la lista resultante
    current_node = merged_list_head
    while current_node:
        print(current_node.val)
        current_node = current_node.next
```

## Conclusión

Este ejercicio no solo ayuda a entender cómo trabajar con listas enlazadas, sino que también ofrece una buena práctica para manejar algoritmos de comparación y fusión de estructuras de datos ordenadas. La capacidad de fusionar dos listas enlazadas de manera eficiente es una habilidad crucial en el desarrollo de software, especialmente en áreas relacionadas con el procesamiento y manipulación de datos.
