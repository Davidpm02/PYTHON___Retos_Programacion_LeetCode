# Construct K Palindrome Strings

## Descripción

El ejercicio "Construct K Palindrome Strings" consiste en determinar si es posible utilizar todos los caracteres de una cadena `s` para construir exactamente `k` subcadenas palíndromas. Un palíndromo es una cadena que se lee igual de izquierda a derecha que de derecha a izquierda. La función debe devolver `true` si es posible, o `false` en caso contrario.

El reto evalúa la capacidad de manipular cadenas de texto y comprender la propiedad de los palíndromos, para resolver el problema utilizando una técnica eficiente que cuente las ocurrencias de caracteres y determine la viabilidad de formar palíndromos a partir de esas frecuencias.

## Implementación

La implementación se lleva a cabo utilizando Python y una clase `Solution` que contiene el método `canConstruct`. Este método verifica si es posible dividir la cadena `s` en `k` subcadenas que sean palíndromas, teniendo en cuenta las restricciones en cuanto al número de veces que cada carácter puede ser utilizado.

### Detalles de la implementación

- **Contador de caracteres:** Se utiliza `Counter` de la biblioteca `collections` para contar las frecuencias de cada carácter en la cadena `s`.
- **Verificación de paridad de caracteres:** Se realiza un análisis de las frecuencias de los caracteres. Para un palíndromo válido, cada carácter debe aparecer una cantidad par de veces, salvo uno, que puede aparecer un número impar (en el caso de palíndromos con longitud impar).
- **Comprobaciones iniciales:** Se verifica si es posible formar exactamente `k` palíndromos:
  - Si el número de caracteres es menor que `k`, es imposible formar los palíndromos.
  - Si el número de caracteres es igual a `k`, se puede formar un palíndromo por cada carácter, ya que cada uno podría ser un palíndromo de longitud 1.

## Uso

Para utilizar el código, simplemente se debe pasar la cadena `s` y el valor de `k` al método `canConstruct` de la clase `Solution`. La función devuelve un valor booleano que indica si es posible dividir la cadena en `k` palíndromos. Aquí se muestra cómo usarlo en Python:

```python
if __name__ == "__main__":
    s = "annabelle"
    k = 2

    sol = Solution()
    can_construct = sol.canConstruct(s, k)
    print(can_construct)  # Output: true
```

## Conclusión

El ejercicio "Construct K Palindrome Strings" pone a prueba la capacidad de manipular cadenas y calcular las frecuencias de caracteres de manera eficiente para resolver un problema interesante relacionado con los palíndromos. La solución implementada es eficiente y efectiva, utilizando las herramientas adecuadas para manejar cadenas de texto y trabajar con ellas en función de las reglas de los palíndromos. A través de este ejercicio, no solo se refuerzan conceptos clave de estructuras de datos como contadores, sino que también se ejercita la resolución de problemas de optimización en programación.
