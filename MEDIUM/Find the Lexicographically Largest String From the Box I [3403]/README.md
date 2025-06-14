# Find The Lexicographically Largest String From the Box I

## Descripción

El ejercicio "Find The Lexicographically Largest String From the Box I" plantea el problema de dividir una cadena `word` en `numFriends` subcadenas no vacías en múltiples rondas. En cada ronda, se generan diferentes divisiones sin repetir ninguna división exacta previa. Todas las subcadenas obtenidas en cada ronda se colocan en una "caja". El objetivo es encontrar la cadena lexicográficamente más grande que pueda aparecer en la caja después de que todas las rondas hayan concluido.

## Implementación

La solución aprovecha propiedades combinatorias para determinar cuál es la subcadena lexicográficamente mayor que puede aparecer en cualquier posible división de `word` en `numFriends` partes. En lugar de generar todas las divisiones (que sería computacionalmente costoso), se basa en la observación de que la subcadena más larga posible dentro de las restricciones será la candidata a ser la más grande lexicográficamente.

### Detalles de la implementación

- **Condición base:** Si `numFriends` es 1, la única subcadena es la cadena completa.
- **Longitud máxima de subcadena:** Se calcula como `n - numFriends + 1`, que representa la máxima longitud posible para una subcadena válida en la división.
- **Búsqueda:** Se recorren todas las posiciones posibles de inicio en `word` para extraer subcadenas con la longitud máxima o la longitud restante desde el índice actual.
- **Comparación lexicográfica:** Se mantiene un registro de la subcadena lexicográficamente mayor encontrada hasta el momento y se actualiza si se encuentra una mejor candidata.

## Uso

Para utilizar este código, se definen los valores de `word` y `numFriends`, se instancia la clase `Solution` y se llama al método `answerString` con los argumentos. El resultado es la cadena lexicográficamente más grande posible que puede obtenerse tras todas las rondas de división.

```python
if __name__ == "__main__":
    word = "dbca"
    numFriends = 2

    sol = Solution()
    result = sol.answerString(word, numFriends)
    print(result)  # Output esperado: "dbc"
```

## Conclusión

El ejercicio "Find The Lexicographically Largest String From the Box I" permite comprender cómo abordar problemas de combinatoria y cadenas con restricciones complejas, evitando búsquedas exhaustivas mediante análisis lógico. La implementación es eficiente, con una complejidad lineal respecto a la longitud de la cadena, y destaca la importancia de detectar patrones y acotar soluciones en problemas de división y partición de cadenas para obtener resultados óptimos.
