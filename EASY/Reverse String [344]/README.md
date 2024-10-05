# Reverse String

## Descripción

El ejercicio "Reverse String" consiste en invertir el orden de una cadena de caracteres que es proporcionada como un array de caracteres s. La solución debe modificar el array original in-place (es decir, sin usar memoria adicional para otro array), logrando un uso de memoria constante, es decir, O(1).

Este problema es común cuando se trabaja con estructuras de datos que requieren modificaciones en su lugar, lo que lo convierte en un ejercicio clave para mejorar la eficiencia en la manipulación de datos.

## Implementación

La implementación de este ejercicio se realiza en Python utilizando una clase Solution que contiene el método reverseString. Este método se encarga de invertir los elementos del array s directamente, sin la creación de estructuras de datos auxiliares.

### Detalles de la implementación

* Modificación in-place: Utilizamos una asignación sobre el mismo array con el slicing inverso (s[::-1]), lo que permite invertir el contenido del array sin necesidad de memoria adicional.
* Slicing: Python permite invertir fácilmente el orden de los elementos de una lista utilizando esta técnica de slicing, que accede a todos los elementos del array de derecha a izquierda y los reasigna en el mismo array.

El código cumple con los requisitos de complejidad de memoria O(1), ya que no se crea una nueva estructura de datos; la modificación se realiza directamente sobre la entrada proporcionada.

## Uso

Para utilizar este código, basta con crear una instancia de la clase Solution y llamar al método reverseString, proporcionando el array de caracteres como parámetro. El array original será modificado en el lugar.

```python
if __name__ == "__main__":
    # Ejemplo 1
    s = ["h", "e", "l", "l", "o"]
    sol = Solution()
    sol.reverseString(s)
    print(s)  # Output: ["o", "l", "l", "e", "h"]

    # Ejemplo 2
    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    print(s)  # Output: ["h", "a", "n", "n", "a", "H"]
```

## Conclusión

El ejercicio "Reverse String" es un buen ejemplo de cómo manipular arrays de manera eficiente en términos de espacio, modificando la estructura original sin usar memoria extra. Esto es fundamental en escenarios donde los recursos de memoria son limitados o donde se requiere una alta eficiencia en tiempo de ejecución. La implementación utilizando slicing de Python no solo es concisa y clara, sino también altamente eficiente, cumpliendo con los requisitos del problema de una manera simple y directa.
