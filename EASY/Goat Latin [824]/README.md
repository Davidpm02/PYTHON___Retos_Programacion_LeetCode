# Goat Latin

## Descripción

El ejercicio "Goat Latin" consiste en transformar una cadena de texto que representa una oración en un idioma ficticio llamado Goat Latin. Esta transformación sigue unas reglas específicas basadas en las características de cada palabra en la oración original:

1. Si una palabra comienza con una vocal ('a', 'e', 'i', 'o', 'u'), se le añade "ma" al final.
2. Si una palabra comienza con una consonante, se elimina su primera letra, se mueve al final de la palabra, y se le añade "ma".
3. A cada palabra se le añade al final una cadena formada por una o más letras 'a', cuyo número corresponde al índice de la palabra (empezando en 1).

El resultado final es una oración en el idioma Goat Latin.

## Implementación

La implementación utiliza Python y se estructura en una clase `Solution` con un método principal llamado `toGoatLatin`. Este método procesa las palabras de la oración para transformarlas siguiendo las reglas mencionadas.

### Detalles de la implementación

- **División de palabras:** La cadena de entrada se divide en una lista de palabras utilizando el método `split()`.
- **Transformación individual:** Cada palabra se procesa según las reglas de Goat Latin, verificando si comienza con vocal o consonante.
- **Concatenación del resultado:** Las palabras transformadas se combinan de nuevo en una única cadena utilizando el método `join()`.

## Conclusión

El ejercicio "Goat Latin" ofrece una oportunidad de practicar la manipulación de cadenas y estructuras como listas en Python. Implementar este tipo de transformaciones refuerza habilidades clave en programación, como el uso de bucles, condiciones y manejo de datos estructurados. Este ejercicio, además de ser lúdico, introduce conceptos útiles para la solución de problemas relacionados con procesamiento de texto.
