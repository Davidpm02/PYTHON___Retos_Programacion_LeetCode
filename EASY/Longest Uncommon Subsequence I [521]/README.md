# Longest Uncommon Subsequence I

## Descripción

El ejercicio "Longest Uncommon Subsequence I" consiste en encontrar la longitud de la subsecuencia más larga que es "uncommon" (no común) entre dos cadenas dadas, a y b. Una subsecuencia no común se define como una cadena que es una subsecuencia de exactamente una de las dos cadenas.

## Implementación

La implementación está en Python y se realiza mediante una clase Solution con el método findLUSlength. Este método evalúa si las cadenas son iguales. Si lo son, devuelve -1 porque no existe una subsecuencia no común. En caso contrario, devuelve la longitud de la cadena más larga entre a y b.

### Detalles de la implementación

1. Igualdad de cadenas:
    Si a == b, significa que no existe ninguna subsecuencia no común, por lo que se devuelve -1.

2. Longitud máxima:
    Si las cadenas son diferentes, la subsecuencia no común más larga será la cadena completa más larga entre a y b. Esto se evalúa utilizando la función len() y max().

## Uso

Para usar este código, define las cadenas a y b, crea una instancia de la clase Solution, y llama al método findLUSlength. El resultado será la longitud de la subsecuencia no común más larga.

```python
if __name__ == "__main__":
    a = "aba"
    b = "cdc"

    sol = Solution()
    result = sol.findLUSlength(a, b)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Longest Uncommon Subsequence I" permite analizar y comparar cadenas de texto para encontrar subsecuencias no comunes, reforzando conceptos fundamentales sobre manipulación de cadenas y subsecuencias en programación. La solución presentada es simple y directa, utilizando operaciones básicas de comparación y longitud de cadenas. Este enfoque es eficiente, dado que opera en tiempo constante en términos de la longitud de las cadenas, cumpliendo con las restricciones del problema.
