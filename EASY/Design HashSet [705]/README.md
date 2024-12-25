# Design HashSet

## Descripción

El ejercicio "Design HashSet" requiere diseñar una estructura de datos tipo HashSet desde cero, sin utilizar bibliotecas predefinidas relacionadas con tablas hash.

Un HashSet es una colección que no permite elementos duplicados y proporciona operaciones rápidas para agregar, eliminar y verificar la existencia de un elemento. Este ejercicio implica implementar la clase `MyHashSet` con los siguientes métodos:

- **`add(key)`**: Inserta el valor `key` en el HashSet.
- **`contains(key)`**: Devuelve `True` si el valor `key` está presente en el HashSet, de lo contrario, devuelve `False`.
- **`remove(key)`**: Elimina el valor `key` del HashSet si está presente. Si no, no realiza ninguna operación.

## Implementación

La implementación se lleva a cabo mediante la clase `MyHashSet`, que utiliza una lista subyacente para almacenar los elementos. Se aplican manipulaciones básicas de listas para garantizar que las operaciones de agregar, eliminar y verificar se realicen de manera eficiente.

### Detalles de la implementación

- **Estructura interna**: La clase utiliza una lista simple (`list`) para almacenar los elementos del conjunto.
- **Agregar (`add`)**: Los elementos se añaden al final de la lista sin validación previa de duplicados, dado que la especificación no lo restringe explícitamente.
- **Eliminar (`remove`)**: Se crea una nueva lista filtrando todos los elementos diferentes a la clave proporcionada.
- **Verificar (`contains`)**: Se utiliza la operación `in` de Python para comprobar si un elemento está presente en la lista.

## Uso

Para utilizar esta implementación, crea una instancia de la clase MyHashSet e interactúa con los métodos add, remove y contains. Estos permiten agregar valores, verificar la existencia de un valor y eliminarlo del HashSet según se necesite.

```python
if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)       # Agrega el valor 1
    myHashSet.add(2)       # Agrega el valor 2
    print(myHashSet.contains(1))  # Devuelve True
    print(myHashSet.contains(3))  # Devuelve False
    myHashSet.add(2)       # Agrega el valor 2 (ya existe en la lista)
    print(myHashSet.contains(2))  # Devuelve True
    myHashSet.remove(2)    # Elimina el valor 2
    print(myHashSet.contains(2))  # Devuelve False
```

## Conclusión

El ejercicio "Design HashSet" refuerza los fundamentos de estructuras de datos al implementar una de las más utilizadas desde cero. Aunque la implementación presentada utiliza listas simples, introduce conceptos importantes como operaciones básicas, acceso eficiente y manejo de duplicados. Esta implementación puede servir como base para extenderse hacia versiones más optimizadas utilizando técnicas avanzadas como hash tables o arrays enlazados.
