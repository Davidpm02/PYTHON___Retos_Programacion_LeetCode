# First Unique Character in a String

## Descripción

El ejercicio "First Unique Character in a String" tiene como objetivo encontrar el primer carácter no repetido en una cadena de texto dada y devolver su índice. Si no existe ningún carácter único en la cadena, se debe devolver -1. Este tipo de problema es común en la programación competitiva y es útil para entender el manejo de estructuras de datos como contadores o diccionarios.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `firstUniqChar`. Este método utiliza la clase `Counter` del módulo `collections` para contar las ocurrencias de cada carácter en la cadena. Luego, filtra aquellos caracteres que aparecen solo una vez y devuelve el índice del primero de ellos.

### Detalles de la implementación

- **Conteo de caracteres:** Se utiliza `Counter` para contar cuántas veces aparece cada carácter en la cadena.
- **Filtrado de caracteres únicos:** Se filtran los caracteres que solo tienen una ocurrencia.
- **Búsqueda del índice:** Para los caracteres únicos, se calcula el índice mínimo utilizando el método `index()` de las cadenas.
- **Resultado:** Si no se encuentran caracteres únicos, se retorna -1.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `firstUniqChar` con la cadena de texto deseada. El resultado será el índice del primer carácter único o -1 si no hay caracteres únicos.

```python
if __name__ == "__main__":
    s = "leetcode"

    sol = Solution()
    first_unique_index = sol.firstUniqChar(s)
    print(first_unique_index)  # Output: 0
```

## Conclusión

El ejercicio "First Unique Character in a String" es una excelente manera de practicar el manejo de cadenas y el uso de contadores para identificar caracteres únicos. La solución propuesta hace uso eficiente de las herramientas incorporadas en Python para trabajar con colecciones y cadenas, y proporciona una forma directa y eficiente de encontrar el primer carácter no repetido. Este tipo de problema puede aplicarse en situaciones reales, como la detección de patrones en grandes volúmenes de texto.
