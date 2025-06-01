# Longest Palindrome by Concatenating Two Letter Words

## Descripción

El ejercicio **"Longest Palindrome by Concatenating Two Letter Words"** plantea el desafío de construir el palíndromo más largo posible a partir de un conjunto de palabras, donde cada palabra está compuesta por exactamente dos letras minúsculas. El objetivo es seleccionar un subconjunto de estas palabras (sin repetir elementos) y concatenarlas en cualquier orden, de forma que el resultado final sea un palíndromo válido y su longitud total sea máxima.

Este tipo de problema es especialmente interesante por su aplicación en algoritmos de búsqueda y manipulación de cadenas, y requiere un enfoque eficiente para poder escalar con listas de gran tamaño.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que expone el método `longestPalindrome`. Este método se basa en un análisis de frecuencia de las palabras utilizando la clase `Counter` del módulo `collections`, lo cual permite realizar emparejamientos eficientes entre palabras y sus reversos.

### Detalles de la implementación

- **Palabras palindrómicas:** Si una palabra es igual a su reverso (por ejemplo, `"aa"`, `"cc"`), se puede usar en pares para garantizar simetría. Además, si queda una palabra de este tipo sin emparejar, puede usarse como elemento central del palíndromo.
  
- **Palabras con reverso en la lista:** Si una palabra tiene su reverso presente en la lista (por ejemplo, `"ab"` y `"ba"`), se pueden emparejar entre sí para contribuir simétricamente al palíndromo.
  
- **Gestión del conteo:** Para cada palabra, se lleva un control de cuántas veces se puede emparejar con su correspondiente, actualizando los contadores para evitar reutilizaciones indebidas.

- **Optimización de longitud:** La longitud del palíndromo se va acumulando a medida que se forman pares válidos, teniendo en cuenta que cada par de palabras suma 4 caracteres, y un elemento central suma 2 caracteres.

## Uso

Para utilizar este código, basta con definir una lista de palabras (cada una de longitud dos) y luego crear una instancia de la clase `Solution`. Al llamar al método `longestPalindrome` con esta lista, se obtendrá como salida un entero que representa la longitud máxima del palíndromo que se puede construir.

```python
if __name__ == "__main__":
    words = ["lc", "cl", "gg"]
    
    sol = Solution()
    max_length = sol.longestPalindrome(words)
    print(max_length)  # Output: 6
```

## Conclusión

El ejercicio "Longest Palindrome by Concatenating Two Letter Words" demuestra cómo técnicas de conteo, manipulación de cadenas y lógica condicional pueden combinarse para resolver problemas de optimización con restricciones. La solución implementada no solo es eficiente —gracias al uso de estructuras como Counter— sino que también es clara y modular, lo cual la hace fácilmente extensible o adaptable a otros problemas similares. Este enfoque pone en práctica conceptos clave del desarrollo algorítmico en Python y fortalece la comprensión del trabajo con estructuras simétricas en listas de cadenas.
