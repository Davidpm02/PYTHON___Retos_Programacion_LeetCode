# Find the Difference

## Descripción

El ejercicio "Find the Difference" consiste en identificar el carácter adicional que ha sido añadido a una cadena de texto. Se te proporcionan dos cadenas, `s` y `t`. La cadena `t` se genera a partir de una permutación aleatoria de `s`, con una letra adicional insertada en una posición aleatoria. El objetivo es encontrar y devolver esta letra adicional que no está en la cadena original `s`.

## Implementación

La solución está implementada en Python mediante una clase `Solution` que contiene el método `findTheDifference`. Este método utiliza un enfoque basado en el uso de la clase `Counter` del módulo `collections`, la cual permite contar de manera eficiente la frecuencia de aparición de cada carácter en ambas cadenas.

### Detalles de la implementación

1. **Contador de caracteres:** Se utiliza la clase `Counter` para contar la frecuencia de los caracteres en la cadena `s`.
2. **Actualización con la cadena `t`:** Posteriormente, el contador se actualiza con los caracteres de la cadena `t`, lo que incrementa la frecuencia de los caracteres presentes en ambas cadenas.
3. **Detección del carácter diferencial:** El carácter añadido en la cadena `t` será aquel cuya frecuencia total sea impar (debido a la adición de un solo carácter), y este es el valor que se devuelve.

## Uso

Para utilizar este código, simplemente se deben definir las cadenas de texto s y t, y luego crear una instancia de la clase Solution. Al llamar al método findTheDifference, se obtendrá el carácter adicional presente en la cadena t.

```python
if __name__ == "__main__":
    s = "abcd"
    t = "abcde"

    sol = Solution()
    extra_char = sol.findTheDifference(s, t)
    print(extra_char)  # Output: "e"
```

## Conclusión

El ejercicio "Find the Difference" presenta una manera eficiente de identificar un carácter añadido a una cadena a partir de una permutación de otra cadena de texto. La solución implementada utiliza la clase Counter, lo que hace que el proceso de comparación sea directo y sencillo. Este ejercicio es una excelente manera de practicar el uso de estructuras de datos como los diccionarios y las operaciones de conteo, que son comunes en la manipulación de cadenas de texto y algoritmos de frecuencia de caracteres.
