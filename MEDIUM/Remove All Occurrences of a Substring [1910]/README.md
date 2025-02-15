# Remove All Occurrences of a Substring

## Descripción

El ejercicio "Remove All Occurrences of a Substring" consiste en eliminar todas las apariciones de una subcadena dentro de una cadena dada. El proceso se repite hasta que la subcadena ya no esté presente en la cadena original. Una subcadena es una secuencia contigua de caracteres dentro de una cadena.

## Implementación

La solución implementada en Python utiliza un bucle `while` para buscar y eliminar repetidamente la subcadena dentro de la cadena principal. A continuación, se describen los pasos clave de la implementación:

- **Búsqueda de la subcadena:** Se verifica si la subcadena `part` está presente dentro de `s`.
- **Eliminación de la subcadena:** Se usa el método `replace()` para eliminar la primera aparición de `part` en `s`.
- **Repetición del proceso:** Se repite el proceso hasta que `part` ya no esté en `s`.

Este enfoque garantiza que todas las apariciones de `part` sean eliminadas de manera eficiente.

## Uso

Para utilizar este código, se debe definir una cadena principal `s` y una subcadena `part`, y luego llamar al método `removeOccurrences` de la clase `Solution`.

```python
if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    
    sol = Solution()
    result = sol.removeOccurrences(s, part)
    print(result)  # Output: "dab"
```

## Conclusión

El ejercicio "Remove All Occurrences of a Substring" demuestra el uso eficiente de métodos de manipulación de cadenas en Python. La solución basada en `replace()` y un bucle `while` permite eliminar todas las ocurrencias de una subcadena de manera iterativa y efectiva. Este enfoque es fácil de entender y aplicar a problemas similares de procesamiento de texto.
