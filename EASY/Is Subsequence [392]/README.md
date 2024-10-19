# Is Subsequence

## Descripción

El ejercicio "Is Subsequence" consiste en determinar si una cadena `s` es una subsecuencia de otra cadena `t`. Una subsecuencia se define como una nueva cadena que se forma a partir de la original eliminando algunos (o ninguno) de los caracteres, sin alterar el orden relativo de los caracteres restantes. Este problema es común en aplicaciones relacionadas con la verificación de patrones en cadenas y secuencias de datos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution`, que contiene el método `isSubsequence`. Este método verifica si la cadena `s` es subsecuencia de `t` mediante un proceso iterativo, donde se comparan los caracteres de `s` con los de `t` manteniendo el orden relativo.

### Detalles de la implementación

1. **Extracción de caracteres de `t` que están en `s`:** Se filtran los caracteres de `t` que existen en `s` para construir una lista intermedia.
2. **Verificación de subsecuencia:** Se recorre la lista filtrada y se verifica si los caracteres coinciden con la cadena `s`, respetando el orden relativo.
3. **Manejo de excepciones:** Se maneja el flujo en caso de que no se cumpla la condición de subsecuencia y se validan los casos en que no hay coincidencia.

## Uso

Para utilizar este código, simplemente se deben definir las cadenas de texto s y t, crear una instancia de la clase Solution y llamar al método isSubsequence. El método retornará True si s es subsecuencia de t, o False en caso contrario.

```python
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"

    sol = Solution()
    result = sol.isSubsequence(s, t)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Is Subsequence" permite determinar si una cadena es una subsecuencia de otra, un concepto fundamental en la manipulación de secuencias y patrones en informática. La solución implementada aprovecha la capacidad de Python para manipular cadenas y listas de manera eficiente, proporcionando una forma clara y concisa de verificar la condición de subsecuencia. Este tipo de ejercicios es clave en la práctica del manejo de secuencias de datos, con aplicaciones en diversas áreas como procesamiento de texto y algoritmos de búsqueda de patrones.
