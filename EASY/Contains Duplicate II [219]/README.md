# Contains Duplicate II

## Descripción

El ejercicio "Contains Duplicate II" consiste en determinar si en un array de enteros existen dos índices distintos `i` y `j` tal que los elementos en esos índices son iguales y la distancia absoluta entre ellos es menor o igual a un valor `k`. Este problema es relevante en el análisis de datos y la detección de patrones en secuencias.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `containsNearbyDuplicate`. Este método utiliza un diccionario para rastrear los números y sus respectivas posiciones en el array, verificando si hay duplicados dentro de la distancia especificada.

## Detalles de la implementación

- **Uso de un diccionario:** Se utiliza un diccionario para contar las ocurrencias de cada número en el array.
- **Rastreo de índices:** Para cada número que aparece más de una vez, se guardan sus índices en una lista.
- **Comprobación de distancia:** Se verifica si la diferencia absoluta entre los índices de las apariciones es menor o igual a `k`.

## Uso

Para utilizar este código, se debe definir una lista de enteros nums y un entero k. Luego, se crea una instancia de la clase Solution y se llama al método containsNearbyDuplicate con estos parámetros. El resultado será un valor booleano que indica si se cumplen las condiciones.

```python
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3

    sol = Solution()
    result = sol.containsNearbyDuplicate(nums, k)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Contains Duplicate II" proporciona una solución efectiva para identificar duplicados en un array de enteros dentro de una distancia especificada. Este problema es útil en diversas aplicaciones de programación y análisis de datos, y la implementación presentada es clara y eficiente, aprovechando estructuras de datos adecuadas como diccionarios y listas. Este enfoque no solo facilita la detección de patrones en los datos, sino que también refuerza conceptos fundamentales en la manipulación de colecciones en Python.
