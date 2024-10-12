# Ransom Note

## Descripción

El ejercicio "Ransom Note" consiste en verificar si se puede construir una cadena ransomNote utilizando únicamente las letras disponibles en otra cadena llamada magazine. Cada letra en magazine puede usarse una sola vez. Esta tarea se puede visualizar como un problema clásico de manipulación de cadenas y es común en situaciones donde se requiere comprobar la disponibilidad de ciertos recursos (en este caso, letras) para cumplir con una demanda.

## Implementación

La implementación de este ejercicio se realiza en Python utilizando la clase Solution, que contiene el método canConstruct. Este método compara la frecuencia de las letras en ambas cadenas y determina si la cadena ransomNote se puede formar con las letras disponibles en magazine.

### Detalles de la implementación

* Contadores de caracteres: Se utiliza el módulo collections.Counter para contar las apariciones de cada letra tanto en ransomNote como en magazine.
* Comparación de contadores: La función compara las frecuencias de cada carácter de ransomNote con las de magazine. Si alguna letra en ransomNote aparece más veces de lo que está disponible en magazine, el método devuelve False.
* Excepciones: Se utiliza un bloque try-except con AssertionError para gestionar los casos en los que no se puede formar la cadena ransomNote.

## Uso

Para utilizar este código, se debe crear una instancia de la clase Solution y llamar al método canConstruct pasando las cadenas ransomNote y magazine. El método devolverá True si es posible construir ransomNote con las letras de magazine, o False en caso contrario.

```python
if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"

    sol = Solution()
    result = sol.canConstruct(ransomNote, magazine)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Ransom Note" presenta una solución eficiente al problema de verificar si una cadena puede ser formada utilizando los caracteres de otra cadena, lo que es útil en contextos de manipulación de cadenas y problemas relacionados con la gestión de recursos. El uso de collections.Counter simplifica la comparación de frecuencias de caracteres, y el enfoque utilizado aprovecha las estructuras de datos de Python para lograr un código claro y eficiente.
