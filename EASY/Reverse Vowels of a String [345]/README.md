# Reverse Vowels of a String

## Descripción

El ejercicio "Reverse Vowels of a String" consiste en invertir el orden de todas las vocales de una cadena de texto dada, sin alterar el resto de los caracteres. Las vocales consideradas son 'a', 'e', 'i', 'o', 'u', tanto en minúsculas como en mayúsculas. El resto de los caracteres permanecen en su posición original, lo que convierte este ejercicio en un desafío interesante de manipulación de cadenas y búsqueda selectiva de caracteres.

Este tipo de operaciones es útil en diversos contextos de procesamiento de texto, donde se requiere transformar o modificar ciertas subcadenas en función de criterios específicos.

## Implementación

La implementación se realiza en Python utilizando una clase Solution que contiene el método reverseVowels. Este método toma una cadena como entrada, identifica las vocales, invierte su orden y luego reconstruye la cadena original con las vocales invertidas. La lógica principal está dividida en los siguientes pasos:

### Detalles de la implementación

* Identificación de vocales: Se construyen dos listas: una con las vocales en minúsculas y otra con las vocales en mayúsculas. Estas listas se utilizan para identificar las vocales presentes en la cadena de entrada.
* Recolección de vocales: Recorremos la cadena de texto y guardamos las vocales encontradas en un array temporal.
* Inversión de vocales: Invertimos el array de vocales recogido para cumplir con el requerimiento del ejercicio.
* Reconstrucción de la cadena: Se reconstruye la cadena original, reemplazando las vocales por las que hemos invertido, mientras que el resto de los caracteres se dejan sin cambios.

## Uso

Para utilizar este código, simplemente crea una instancia de la clase Solution y llama al método reverseVowels, proporcionando la cadena de texto que deseas procesar. El método devolverá una nueva cadena con las vocales invertidas.

```python
if __name__ == "__main__":
    # Ejemplo 1
    s = "IceCreAm"
    sol = Solution()
    result = sol.reverseVowels(s)
    print(result)  # Output: "AceCreIm"

    # Ejemplo 2
    s = "leetcode"
    sol = Solution()
    result = sol.reverseVowels(s)
    print(result)  # Output: "leotcede"
```

## Conclusión

El ejercicio "Reverse Vowels of a String" es un buen ejemplo de cómo manipular una cadena de texto selectivamente, centrándose solo en los caracteres que cumplen un criterio específico, en este caso, las vocales. La implementación es eficiente y utiliza técnicas como el uso de diccionarios para mapear y reconstruir la cadena de forma efectiva. Este tipo de problemas son útiles para mejorar la comprensión de la manipulación de strings y la optimización del uso de memoria, al evitar la creación de estructuras adicionales innecesarias.
