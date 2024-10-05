# Intersection of Two Arrays

## Descripción

El ejercicio "Intersection of Two Arrays" consiste en encontrar la intersección de dos arrays de números enteros. La intersección de dos arrays es el conjunto de elementos que aparecen en ambos arrays. El resultado debe contener solo elementos únicos, y se puede devolver en cualquier orden. Este tipo de operación es común en diversas aplicaciones relacionadas con conjuntos y bases de datos, donde es necesario encontrar coincidencias o elementos comunes entre dos colecciones.

## Implementación

La implementación se realiza en Python utilizando una clase Solution que contiene el método intersection. Este método recibe dos listas de enteros, nums1 y nums2, y retorna una lista que contiene la intersección de ambos arrays.

### Detalles de la implementación

* Intersección de arrays: El método compara cada elemento del primer array (nums1) con los elementos del segundo array (nums2) y guarda los elementos que coinciden en un conjunto para eliminar duplicados automáticamente.  
* Retorno del resultado: El resultado se devuelve en forma de lista después de haber filtrado los elementos comunes.

El uso de un conjunto (set) asegura que los elementos repetidos en los arrays de entrada no se incluyan varias veces en el resultado, logrando así una solución eficiente y óptima.

## Uso

Para utilizar este código, simplemente se deben definir dos arrays de enteros y crear una instancia de la clase Solution. Luego, se llama al método intersection con ambos arrays como parámetros, y el resultado será una lista que contiene los elementos comunes.

```python
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    sol = Solution()
    result = sol.intersection(nums1, nums2)
    print(result)  # Output: [2]

    # Otro ejemplo
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = sol.intersection(nums1, nums2)
    print(result)  # Output: [9, 4]
```

## Conclusión

El ejercicio "Intersection of Two Arrays" demuestra cómo trabajar eficientemente con conjuntos de datos para encontrar elementos comunes entre dos colecciones. La solución implementada aprovecha las características de los conjuntos en Python para eliminar duplicados y garantizar una respuesta rápida. Esta tarea es relevante en problemas relacionados con el procesamiento de datos y la manipulación de colecciones, además de ser un buen ejercicio para fortalecer el entendimiento sobre conjuntos y estructuras de datos en programación.
