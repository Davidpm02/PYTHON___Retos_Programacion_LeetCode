# The k-th Lexicographical String of All Happy Strings of Length n

## Descripción

El ejercicio "The k-th Lexicographical String of All Happy Strings of Length n" consiste en generar una cadena que cumple con las siguientes condiciones:

- La cadena está formada únicamente por los caracteres 'a', 'b' y 'c'.
- No debe haber caracteres consecutivos iguales dentro de la cadena.
- Se deben generar todas las cadenas posibles que cumplen con las reglas anteriores y ordenarlas lexicográficamente.
- Se devuelve la k-ésima cadena de esta lista, o una cadena vacía si k es mayor que el número total de cadenas generadas.

Este problema pone a prueba habilidades en combinatoria y generación de permutaciones con restricciones específicas.

## Implementación

La implementación se realiza en Python dentro de una clase `Solution`, que contiene el método `getHappyString`. Este método sigue los siguientes pasos:

- Calcula el número total de cadenas "happy" posibles para la longitud dada.
- Si k es mayor que el número total de combinaciones, retorna una cadena vacía.
- Construye la cadena de manera iterativa, seleccionando en cada posición el carácter adecuado basado en el orden lexicográfico y la cantidad de combinaciones restantes.
- Garantiza que no haya caracteres consecutivos repetidos.

## Uso

Para utilizar este código, simplemente se deben definir los valores de `n` y `k`, luego crear una instancia de la clase `Solution` y llamar al método `getHappyString`.

```python
if __name__ == "__main__":
    n = 3
    k = 9
    
    sol = Solution()
    happy_string = sol.getHappyString(n, k)
    print(happy_string)  # Output: "cab"
```

## Conclusión

El ejercicio "The k-th Lexicographical String of All Happy Strings of Length n" proporciona un enfoque estructurado para generar combinaciones con restricciones y ordenarlas eficientemente. La solución presentada optimiza el proceso evitando la generación de todas las combinaciones de antemano, reduciendo el tiempo de cómputo y el uso de memoria. Este tipo de problema es útil para reforzar conceptos en generación de combinaciones, orden lexicográfico y programación eficiente en Python.
