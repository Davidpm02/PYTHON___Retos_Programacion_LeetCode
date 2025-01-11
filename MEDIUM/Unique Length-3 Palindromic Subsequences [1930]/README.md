# Unique Length-3 Palindromic Subsequences

## Descripción

El ejercicio "Unique Length-3 Palindromic Subsequences" consiste en encontrar todas las subsecuencias palindrómicas de longitud 3 dentro de una cadena de texto dada `s`. Una subsecuencia es una secuencia derivada de una cadena eliminando algunos caracteres sin alterar el orden relativo de los caracteres restantes. El objetivo es contar cuántas subsecuencias de longitud 3 pueden ser palíndromos, donde un palíndromo es una palabra o secuencia que se lee igual hacia adelante que hacia atrás.

### Consideraciones

- Se debe considerar cada subsecuencia de longitud 3 que sea palíndromo solo una vez, aunque pueda obtenerse por múltiples combinaciones de caracteres.
- La cadena dada consta solo de letras minúsculas.

## Implementación

La implementación se realiza en Python utilizando la clase `Solution` y su método `countPalindromicSubsequence`. El método tiene como entrada la cadena `s` y devuelve el número de subsecuencias de longitud 3 que son palíndromos.

### Detalles de la implementación

1. **Contador de caracteres:** El método utiliza un contador (`Counter`) para contar la cantidad de veces que aparece cada carácter en la cadena `s`.

2. **Evaluación de subsecuencias palindrómicas:**
   - Si un carácter aparece al menos 3 veces en la cadena, automáticamente es considerado un palíndromo (por ejemplo, "aaa").
   - Si un carácter aparece al menos 2 veces, se evalúa si existe algún carácter intermedio diferente entre las dos posiciones en las que ese carácter aparece, y si la subsecuencia formada por estos caracteres intermedios también es un palíndromo (por ejemplo, "aba").

3. **Conjunto de caracteres procesados:** Se utiliza un conjunto para llevar un registro de los caracteres que ya se han procesado y evitar realizar cálculos redundantes.

4. **Resultado:** El método devuelve la cantidad total de subsecuencias palindrómicas de longitud 3 encontradas.

### Complejidad

- La complejidad temporal de la solución es \(O(n^2)\) en el peor caso, donde \(n\) es la longitud de la cadena `s`. Sin embargo, dada la naturaleza del problema y los casos de prueba típicos, este enfoque es efectivo para cadenas con longitudes moderadas.

## Uso

Para utilizar este código, se debe proporcionar una cadena de caracteres `s`, luego crear una instancia de la clase `Solution`. Se llama al método `countPalindromicSubsequence` con la cadena y se obtiene el resultado como un número entero.

```python
if __name__ == "__main__":
    s = "aabca"

    sol = Solution()
    result = sol.countPalindromicSubsequence(s)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Unique Length-3 Palindromic Subsequences" es una forma interesante de explorar subsecuencias y palíndromos en cadenas de texto. La solución proporciona un enfoque directo para contar subsecuencias palindrómicas de longitud 3, aprovechando el uso de contadores y conjuntos para hacer frente a la repetición de caracteres y mejorar la eficiencia del cálculo. Aunque el enfoque tiene un rendimiento cuadrático en el peor caso, es adecuado para cadenas de longitud moderada, y resalta la importancia de optimizar algoritmos que involucran combinaciones de elementos dentro de secuencias.
