# Contains Duplicate

## Descripción

El ejercicio **Contains Duplicate** tiene como objetivo verificar si un array de números enteros contiene elementos duplicados. El programa debe devolver `true` si algún valor aparece al menos dos veces en el array, o `false` si todos los elementos son únicos. Este tipo de operación es útil para validar la unicidad de elementos en diversas aplicaciones de datos y análisis.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution`, que contiene el método `containsDuplicate`. Este método toma una lista de números enteros y utiliza un diccionario para mapear la frecuencia de aparición de cada número. Si algún número aparece más de una vez, el método retorna `True`, de lo contrario, devuelve `False`.

### Detalles de la implementación

- **Uso de `Counter`**: Se utiliza el objeto `Counter` de la librería `collections` para contar la frecuencia de cada número en la lista.
- **Verificación de duplicados**: Después de contar los elementos, se analiza si alguno tiene una frecuencia mayor que 1. Si es así, se retorna `True`, indicando la presencia de duplicados.
- **Eficiencia**: Al utilizar un contador de frecuencia, el método tiene una complejidad temporal de O(n), lo que es eficiente para arrays grandes.

### Código

Para utilizar este código, primero se debe crear una instancia de la clase Solution y llamar al método containsDuplicate con una lista de enteros como argumento. El método retornará True si hay duplicados en la lista, y False si todos los elementos son distintos.

### Ejemplo de uso

```python
if __name__ == "__main__":
    sol = Solution()

    # Ejemplo 1
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums))  # Output: True

    # Ejemplo 2
    nums = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums))  # Output: False

    # Ejemplo 3
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(sol.containsDuplicate(nums))  # Output: True
```

En los ejemplos anteriores, el array [1, 2, 3, 1] contiene el número 1 dos veces, por lo que el resultado es True. En el segundo ejemplo, todos los elementos son únicos, por lo que el resultado es False. Finalmente, el tercer ejemplo también contiene duplicados, por lo que retorna True.

## Conclusión

El ejercicio Contains Duplicate proporciona una solución eficiente para detectar si hay valores repetidos en una lista de números enteros. Utiliza estructuras de datos optimizadas como Counter para contar las ocurrencias de cada elemento, lo que permite resolver el problema en tiempo O(n). Este tipo de verificación es fundamental en muchos contextos de programación, especialmente en la validación de datos y la manipulación de conjuntos de valores únicos.
