# Minimum Index Sum of Two Lists

## Descripción

El ejercicio "Minimum Index Sum of Two Lists" consiste en encontrar las cadenas comunes entre dos listas de cadenas (`list1` y `list2`), cuyo índice combinado (es decir, la suma de los índices en ambas listas) sea el menor. El objetivo es devolver todas las cadenas que cumplen con este criterio. Este ejercicio es útil para manejar y comparar listas de elementos de manera eficiente, optimizando la búsqueda por las posiciones de los elementos.

## Implementación

La implementación se lleva a cabo en Python, utilizando una clase llamada `Solution`, que incluye el método `findRestaurant`. Este método itera sobre las dos listas de cadenas y encuentra los elementos comunes. Luego, se calcula la suma de sus índices en ambas listas y se seleccionan aquellos que tienen la menor suma.

### Detalles de la implementación

- **Filtrado de palabras comunes:** Se utiliza un diccionario para almacenar las palabras comunes entre ambas listas, con sus respectivas sumas de índices.
- **Ordenamiento por suma de índices:** El diccionario se ordena de menor a mayor según el valor de las sumas de índices.
- **Selección de palabras con el índice mínimo:** Finalmente, se retorna una lista con las palabras que tienen la suma de índices mínima.

## Uso

Para utilizar este código, basta con definir las dos listas de cadenas (`list1` y `list2`). Luego, se crea una instancia de la clase `Solution`, y se llama al método `findRestaurant` con estas listas como parámetros. El resultado será una lista con las cadenas que comparten la menor suma de índices.

```python
if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

    sol = Solution()
    common_strings = sol.findRestaurant(list1, list2)
    print(common_strings)  # Output: ["Shogun"]
```

## Conclusión

El ejercicio "Minimum Index Sum of Two Lists" ofrece una forma eficiente de encontrar los elementos comunes entre dos listas y seleccionar aquellos con la menor suma de índices. La implementación es directa y aprovecha estructuras de datos como los diccionarios y listas para lograr una solución óptima. Este tipo de problema es común en aplicaciones de análisis de datos y manejo de grandes volúmenes de información, y la solución presentada permite resolverlo de manera clara y eficiente.
