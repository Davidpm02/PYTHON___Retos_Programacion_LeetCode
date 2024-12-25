# Shortest Completing Word

## Descripción

El ejercicio "Shortest Completing Word" consiste en encontrar la palabra más corta en una lista de palabras que cumpla con un conjunto de restricciones definidas por una cadena dada (`licensePlate`). Una palabra es considerada "completadora" si contiene todas las letras de `licensePlate` (ignorando espacios, números y diferencias de mayúsculas/minúsculas) y si cada letra aparece en la palabra al menos tantas veces como en `licensePlate`. En caso de que existan múltiples palabras que cumplan con estas condiciones, se devuelve la primera en aparecer en la lista de entrada.

Este problema ilustra cómo manejar cadenas y listas utilizando operaciones de conteo, comparación y ordenamiento de forma eficiente.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con un método llamado `shortestCompletingWord`. Los pasos clave de la solución incluyen:

1. **Extracción de letras válidas:**
   - Se filtran las letras de `licensePlate`, ignorando números, espacios y distinción de mayúsculas/minúsculas.
   - Las letras se convierten a minúsculas para simplificar las comparaciones.

2. **Conteo de frecuencias de letras:**
   - Se utiliza `collections.Counter` para contabilizar la cantidad de cada letra requerida en `licensePlate`.

3. **Filtrado y selección de palabras completadoras:**
   - Se filtran las palabras que contienen todas las letras de `licensePlate`.
   - Se verifica que las palabras seleccionadas contengan cada letra con la frecuencia mínima requerida.
   - Finalmente, se ordenan las palabras por longitud y se selecciona la más corta.

## Uso

Para utilizar este código, crea una instancia de la clase Solution y llama al método shortestCompletingWord con la cadena licensePlate y la lista de palabras words como argumentos. El método retornará la palabra completadora más corta.

```python
if __name__ == "__main__":
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]

    sol = Solution()
    result = sol.shortestCompletingWord(licensePlate, words)
    print(result)  # Output: "steps"
```

## Conclusión

El ejercicio "Shortest Completing Word" es un problema interesante para practicar el manejo y procesamiento de cadenas, listas y frecuencias de caracteres en Python. Esta implementación muestra cómo combinar técnicas de filtrado, conteo y ordenamiento de manera eficiente, lo que es útil en aplicaciones de procesamiento de texto y análisis de datos. La solución presentada es robusta, eficiente y asegura la correcta selección de la palabra más corta que cumpla con todas las condiciones requeridas.
