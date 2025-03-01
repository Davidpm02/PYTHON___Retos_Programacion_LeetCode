# Shortest Common Supersequence

## Descripción

El ejercicio "Shortest Common Supersequence" consiste en encontrar la cadena más corta que contenga a dos cadenas dadas (`str1` y `str2`) como subsecuencias. En otras palabras, la solución debe garantizar que tanto `str1` como `str2` aparezcan en el mismo orden dentro de la cadena resultante, aunque puedan intercalarse caracteres adicionales.

Una subsecuencia de una cadena es aquella que se obtiene eliminando algunos caracteres (posiblemente ninguno) sin alterar el orden de los caracteres restantes.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `shortestCommonSupersequence`. Este método emplea programación dinámica para encontrar la subsecuencia común más larga (LCS, por sus siglas en inglés) y, a partir de ella, construir la supersecuencia más corta.

### Detalles de la implementación

- **Cálculo de la subsecuencia común más larga (LCS):** Se utiliza una matriz `dp` para almacenar la longitud de la LCS entre diferentes subcadenas de `str1` y `str2`.
- **Construcción de la supersecuencia más corta:** Partiendo de la matriz `dp`, se reconstruye la supersecuencia más corta combinando caracteres de `str1` y `str2` siguiendo la LCS.
- **Manejo de caracteres adicionales:** Una vez utilizada la LCS, los caracteres restantes de `str1` y `str2` se agregan a la supersecuencia final.

## Uso

Para utilizar este código, simplemente se deben definir las cadenas de texto `str1` y `str2`, y luego crear una instancia de la clase `Solution`. Se llama al método `shortestCommonSupersequence` con estas cadenas y se obtiene el resultado.

```python
if __name__ == "__main__":
    str1 = "abac"
    str2 = "cab"

    sol = Solution()
    result = sol.shortestCommonSupersequence(str1, str2)
    print(result)  # Output: "cabac"
```

## Conclusión

El ejercicio "Shortest Common Supersequence" es un problema clásico de programación dinámica que tiene aplicaciones en bioinformática, edición de texto y manejo de datos secuenciales. La solución presentada es eficiente y permite encontrar la secuencia más corta que contenga ambas cadenas de entrada como subsecuencias, asegurando un balance óptimo entre la longitud de la cadena resultante y el orden de los caracteres de `str1` y `str2`. Este enfoque resalta la importancia de la programación dinámica en la optimización de problemas combinatorios.
