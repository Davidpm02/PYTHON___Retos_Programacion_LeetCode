# Palindrome Number

## Descripción

Este ejercicio tiene como objetivo determinar si un número entero es un palíndromo. Un número es considerado palíndromo cuando se lee igual de izquierda a derecha y de derecha a izquierda. El reto incluye tratar con números negativos y grandes, garantizando que la solución sea eficiente y directa.

La solución debe manejar números dentro del rango de `-2^31` a `2^31 - 1` según las restricciones del problema. Ejemplos claros del comportamiento esperado son proporcionados para facilitar la comprensión y verificación del correcto funcionamiento de la implementación.

## Implementación

El código está encapsulado en una clase `Solution` que contiene el método `isPalindrome`. Este método toma un entero `x` y devuelve `True` si `x` es un palíndromo, y `False` en caso contrario. La implementación utiliza técnicas de conversión de tipos y operaciones con strings para verificar la condición de palíndromo de manera eficiente y legible.

Detalles de implementación:

- **Conversión y Reversión**: El número entero se convierte a string. Esto permite utilizar el slicing de Python para revertir el string y compararlo con su versión original.
- **Comparación**: Se compara el string original con su versión invertida. Si son iguales, el número es un palíndromo.

## Uso

Para utilizar esta solución en un proyecto o durante el desarrollo, simplemente se necesita:

1. Crear una instancia de la clase `Solution`.
2. Llamar al método `isPalindrome` con el número deseado como argumento.

Ejemplo de uso:

```python
if __name__ == "__main__":
    x = 121
    solution = Solution()
    result = solution.isPalindrome(x)
    print(result)  # Salida esperada: True

```

## Conclusión

El ejercicio "Palindrome Number" proporciona una excelente oportunidad para explorar y aplicar técnicas básicas de manipulación de strings y operaciones de comparación en Python. La solución presentada es eficiente y fácil de entender, haciendo uso de características poderosas del lenguaje para lograr una verificación efectiva de palíndromos en números enteros. Además, el código está diseñado para ser fácilmente integrable y reusable en otros proyectos que requieran funcionalidades similares.
