# Number of Substrings Containing All Three Characters

## Descripción

El ejercicio "Number of Substrings Containing All Three Characters" consiste en encontrar cuántas subcadenas de la cadena de entrada contienen al menos una ocurrencia de cada uno de los caracteres 'a', 'b' y 'c'.

Este problema es relevante en la manipulación de cadenas de texto y en la búsqueda de patrones dentro de una secuencia de caracteres. Se puede abordar eficientemente utilizando la técnica de ventanas deslizantes.

## Implementación

La solución se implementa en Python dentro de una clase `Solution` que contiene el método `numberOfSubstrings`. Este método utiliza una ventana deslizante para recorrer la cadena y contar las subcadenas que cumplen la condición.

### Detalles de la implementación

- **Estructura de datos:** Se utiliza un diccionario para contar la cantidad de ocurrencias de cada carácter ('a', 'b' y 'c') dentro de la ventana actual.
- **Ventana deslizante:** Se recorre la cadena con dos punteros, `left` y `right`, expandiendo la ventana con `right` y contrayéndola con `left` cuando se encuentra una subcadena válida.
- **Conteo de subcadenas:** Cuando la ventana contiene al menos un 'a', un 'b' y un 'c', se cuenta cuántas subcadenas pueden formarse desde el índice `left` hasta el final de la cadena.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `numberOfSubstrings` con una cadena de entrada.

```python
if __name__ == "__main__":
    s = "abcabc"
    
    sol = Solution()
    result = sol.numberOfSubstrings(s)
    print(result)  # Salida esperada: 10
```

## Conclusión

El ejercicio "Number of Substrings Containing All Three Characters" es un problema de manipulación de cadenas que se resuelve de manera eficiente con una técnica de ventana deslizante. Este enfoque permite encontrar todas las subcadenas que contienen los caracteres requeridos con un tiempo de ejecución óptimo. Es un ejemplo de cómo optimizar la búsqueda de patrones en cadenas de texto sin necesidad de generar todas las posibles subcadenas explícitamente.
