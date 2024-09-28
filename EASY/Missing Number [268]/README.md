# Missing Number

## Descripción

El ejercicio "Missing Number" consiste en encontrar el único número faltante en un conjunto de números enteros consecutivos dentro del rango [0, n]. Dada una lista de números enteros distintos, el objetivo es determinar cuál número no está presente en la lista, tomando en cuenta que todos los demás números dentro del rango sí lo están. Este tipo de problema es muy común en estructuras de datos y algoritmos, ya que se enfoca en la búsqueda eficiente y la manipulación de listas.

## Implementación

La implementación de la solución se realiza en Python, utilizando una clase Solution que contiene el método missingNumber. Este método recibe como argumento una lista de enteros nums y devuelve el número faltante en el rango [0, n], donde n es el tamaño de la lista.

### Detalles de la implementación

* Rango de enteros: El método calcula el tamaño de la lista nums para definir un rango de números consecutivos de [0, n].

* Búsqueda del número faltante: Para cada número en el rango [0, n], se verifica si está presente en la lista nums. El primer número que no se encuentre es el número faltante.

* Complejidad: La solución actual utiliza un enfoque de búsqueda lineal con un bucle for para comprobar cada número en el rango, lo que da una complejidad temporal de O(n²), ya que cada comprobación implica una búsqueda en la lista.

## Uso

Para utilizar este código, basta con crear una instancia de la clase Solution y llamar al método missingNumber, pasando como argumento una lista de enteros nums. A continuación, un ejemplo de cómo utilizar la implementación:

```python
if __name__ == "__main__":
    nums = [3, 0, 1]

    sol = Solution()
    missing_num = sol.missingNumber(nums)
    print(missing_num)  # Output: 2
```

## Conclusión

El ejercicio "Missing Number" proporciona una forma directa de encontrar el número ausente en un rango definido. La implementación actual es sencilla y fácil de entender, pero puede mejorarse en términos de eficiencia utilizando enfoques más avanzados, como operaciones matemáticas o técnicas de suma acumulativa (por ejemplo, utilizando la fórmula de la suma de números consecutivos). Este problema refuerza conceptos importantes relacionados con la manipulación de listas y la búsqueda de patrones en datos secuenciales.
