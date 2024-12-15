# Longest Palindrome

## Descripción

El ejercicio "Longest Palindrome" tiene como objetivo encontrar la longitud del palíndromo más largo que puede ser construido usando los caracteres de una cadena de texto dada. Este tipo de problema es importante en diversas aplicaciones, como la bioinformática (en la búsqueda de secuencias de ADN que pueden formar estructuras palindrómicas) y la programación de texto (como análisis de cadenas y procesamiento de texto).

Un palíndromo es una secuencia de caracteres que se lee igual de izquierda a derecha que de derecha a izquierda, como "racecar" o "level".

## Implementación

La implementación se realiza en Python utilizando una clase Solution con el método longestPalindrome. Este método utiliza un contador para calcular la frecuencia de cada carácter en la cadena de texto y luego emplea esa información para determinar la longitud máxima de un palíndromo que puede formarse. El código sigue un enfoque basado en las siguientes reglas:

1. Frecuencia de caracteres: Usamos el Counter de la librería collections para contar las ocurrencias de cada carácter en la cadena de entrada.
2. Construcción del palíndromo: Los caracteres cuya frecuencia es par pueden ser completamente utilizados para formar el palíndromo. Los caracteres con frecuencia impar solo pueden utilizarse parcialmente (por ejemplo, utilizando n−1n−1 caracteres de un conjunto cuyo tamaño es nn).
3. Elemento central: Si hay al menos un carácter con una frecuencia impar, uno de ellos puede ocupar el centro del palíndromo.

### Detalles de la implementación

* Counter: Se utiliza para contar las veces que cada carácter aparece en la cadena.
* Longitud del palíndromo: Se suma la cantidad de caracteres que pueden formar el palíndromo. Aquellos caracteres con frecuencia impar ceden solo su parte par para formar los "lados" del palíndromo, dejando uno para un posible centro.

## Uso

Para utilizar este código, simplemente debes definir una cadena s, crear una instancia de la clase Solution y luego llamar al método longestPalindrome con esa cadena. El resultado será la longitud del palíndromo más largo que puede ser formado.

```python
if __name__ == "__main__":
    s = "abccccdd"
    
    sol = Solution()
    palindrome_length = sol.longestPalindrome(s)
    print(palindrome_length)  # Salida: 7
```

## Conclusión

El ejercicio "Longest Palindrome" ofrece una forma eficiente de resolver el problema de encontrar el palíndromo más largo posible utilizando una cadena de caracteres. A través del uso del Counter, la solución puede contar rápidamente las frecuencias de los caracteres y determinar cuánto de cada carácter se puede usar para formar un palíndromo.

Este enfoque es muy útil para problemas que requieren la manipulación de cadenas y la optimización de recursos, como en la bioinformática, la programación de texto y otras áreas relacionadas. Además, ayuda a reforzar conceptos fundamentales como la manipulación de diccionarios (en este caso, a través de Counter) y la construcción de soluciones a partir de propiedades matemáticas (como la simetría en los palíndromos).
