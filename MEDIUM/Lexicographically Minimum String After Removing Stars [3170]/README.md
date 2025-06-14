# Lexicographically Minimum String After Removing Stars

## Descripción

El ejercicio **"Lexicographically Minimum String After Removing Stars"** plantea el problema de eliminar todos los caracteres '*' de una cadena dada `s`. Para cada '*' encontrado, se debe eliminar también el carácter lexicográficamente más pequeño que esté a la izquierda de dicho '*'. En caso de que existan varios caracteres mínimos, se puede eliminar cualquiera de ellos. El objetivo final es devolver la cadena resultante más pequeña lexicográficamente tras eliminar todos los '*'.

Este problema combina la manipulación de cadenas con la gestión eficiente de posiciones y ordenamientos para garantizar que la eliminación de caracteres siga la condición especificada, manteniendo el resultado lexicográficamente mínimo.

## Implementación

La implementación está realizada en Python dentro de una clase `Solution` que contiene el método `clearStars`. Este método procesa la cadena de izquierda a derecha, gestionando la eliminación de caracteres a medida que se encuentran '*':

### Detalles de la implementación

- **Estructuras auxiliares:**  
  - Una lista `result` para construir la cadena sin '*'.  
  - Un arreglo booleano `deleted` para marcar qué caracteres han sido eliminados.  
  - Una lista de listas `positions` para almacenar las posiciones de cada carácter (de la 'a' a la 'z') en `result`.  

- **Recorrido de la cadena:**  
  - Cuando se encuentra un carácter distinto de '*', se añade a `result`, se marca como no eliminado, y se registra su posición en `positions` correspondiente a su letra.  
  - Al encontrar un '*', se busca el carácter lexicográficamente más pequeño disponible (es decir, con la letra más baja) que no haya sido eliminado y se marca como eliminado. Esto se realiza buscando en `positions` desde la 'a' hasta la 'z' y extrayendo la última posición registrada (la más cercana al '*').  

- **Construcción del resultado:**  
  - Finalmente, se construye la cadena final uniendo solo los caracteres no eliminados en el orden original.

Este enfoque permite gestionar la eliminación selectiva y eficiente, garantizando la condición lexicográfica requerida.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `clearStars` pasando la cadena de entrada. Se obtendrá como resultado la cadena procesada sin '*', con la mínima lexicografía posible según las reglas del problema.

```python
if __name__ == "__main__":
    s = "aaba*"

    sol = Solution()
    cleaned_str = sol.clearStars(s)
    print(cleaned_str)  # Output: "aab"
```

## Conclusión

El ejercicio "Lexicographically Minimum String After Removing Stars" es un buen ejemplo de manipulación avanzada de cadenas y control eficiente de datos mediante estructuras auxiliares para asegurar condiciones de ordenamiento lexicográfico. La solución implementa una técnica que permite eliminar caracteres en función de la posición y el valor lexicográfico, garantizando un resultado óptimo sin necesidad de ordenamientos adicionales complejos. Este problema es ideal para afianzar conceptos de programación eficiente, gestión de índices y lógica condicional aplicada a cadenas.
