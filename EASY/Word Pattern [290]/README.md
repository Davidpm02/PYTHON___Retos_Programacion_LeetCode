# Word Pattern

## Descripción

El ejercicio "Word Pattern" consiste en verificar si una cadena de texto sigue un patrón determinado. Este patrón se basa en una correspondencia única entre las letras de un patrón y las palabras de una cadena de texto. Para que la cadena siga el patrón, cada letra debe mapearse a exactamente una palabra única y viceversa. Esta correspondencia debe mantenerse consistente a lo largo de toda la cadena.

El objetivo es determinar si existe una biyección entre las letras del patrón y las palabras en la cadena, lo que significa que:

* Cada letra del patrón se asocia con una palabra única en la cadena.
* Cada palabra en la cadena se asocia con una única letra del patrón.
* No se permite que dos letras diferentes se asocien a la misma palabra, ni que una palabra se asocie a dos letras diferentes.

## Implementación

La implementación del ejercicio se realiza en Python utilizando una clase Solution, que contiene el método wordPattern. Este método se encarga de realizar las siguientes operaciones para verificar si la cadena de texto sigue el patrón:

* Mapeo entre letras y palabras: Se crea un diccionario donde las letras del patrón se utilizan como claves, y las palabras correspondientes de la cadena se asignan como valores.
* Comprobación de longitudes: Se verifica que la cantidad de letras en el patrón sea igual a la cantidad de palabras en la cadena.
* Consistencia del mapeo: Para cada letra del patrón, se comprueba si ya tiene una palabra asignada y si esta asignación es coherente a lo largo de toda la cadena.

### Detalles de la implementación

* Inicialización del diccionario: Se crea un diccionario donde cada letra del patrón tiene una asignación inicial vacía.
* Separación de palabras en la cadena: La cadena de texto se divide en palabras usando el método split().
* Iteración y validación: A través de un bucle, se comparan las palabras de la cadena con las letras del patrón. Si una letra no tiene asignada una palabra, se establece el mapeo, pero si ya tiene una asignación, se verifica que coincida con la palabra actual.
* Condición de fallo: Si en algún punto se rompe la biyección (es decir, dos letras intentan mapearse a la misma palabra o viceversa), el método devuelve False.

## Uso

Para utilizar este código, simplemente se define un patrón y una cadena de texto, y luego se crea una instancia de la clase Solution. Se llama al método wordPattern con el patrón y la cadena de texto como argumentos para verificar si la cadena sigue el patrón.

```python
if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"

    sol = Solution()
    result = sol.wordPattern(pattern, s)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Word Pattern" es un desafío interesante que involucra la gestión de mapeos entre un conjunto de letras y un conjunto de palabras. Este tipo de problema es común en la verificación de patrones, relaciones uno a uno, y el manejo de estructuras de datos como diccionarios en Python. La solución presentada es eficiente, manejando adecuadamente los casos en los que el patrón y la cadena no coinciden en longitud, así como garantizando que la relación entre las letras y las palabras sea consistente.
