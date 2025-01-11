# Find Smallest Letter Greater Than Target

## Descripción

El ejercicio "Find Smallest Letter Greater Than Target" consiste en encontrar el carácter más pequeño de un arreglo, ordenado de forma no decreciente, que sea lexicográficamente mayor que un carácter objetivo dado (`target`). Si no existe tal carácter, se debe devolver el primer carácter del arreglo. Este problema es relevante para aplicaciones relacionadas con ordenación y búsquedas en estructuras de datos ordenadas.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `nextGreatestLetter`. Este método utiliza operaciones sobre listas y funciones integradas de Python para determinar el carácter deseado.

### Detalles de la implementación

- **Conversión Unicode:**
  - Para realizar comparaciones lexicográficas, los caracteres se convierten en sus valores Unicode utilizando la función `ord()`.

- **Iteración y Filtrado:**
  - Se recorre la lista de caracteres utilizando una lista por compresión.
  - Se filtran únicamente aquellos caracteres cuyo valor Unicode es mayor que el de `target`.

- **Excepción por Índice:**
  - En caso de no encontrar caracteres mayores, se captura la excepción `IndexError` para retornar el primer carácter del arreglo, según la especificación del ejercicio.

## Uso

Para utilizar este código, basta con instanciar la clase `Solution` y llamar al método `nextGreatestLetter`, proporcionando como parámetros el arreglo de caracteres `letters` y el carácter objetivo `target`.

```python
if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"

    sol = Solution()
    result = sol.nextGreatestLetter(letters, target)
    print(result)  # Output: "c"
```

## Conclusión

El ejercicio "Find Smallest Letter Greater Than Target" es una práctica eficiente para trabajar con búsquedas en datos ordenados. La implementación aprovecha la simplicidad de las estructuras de Python y maneja de manera adecuada los casos límite mediante el uso de excepciones. Este enfoque asegura un rendimiento óptimo y resulta adecuado para problemas relacionados con búsquedas y manejo de datos ordenados.
