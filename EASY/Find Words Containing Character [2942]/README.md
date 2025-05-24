# Find Words Containing Character

## Descripción

El ejercicio "Find Words Containing Character" consiste en encontrar, dado un arreglo de cadenas de texto y un carácter específico, los índices de todas las palabras que contienen al menos una aparición de dicho carácter. Esta tarea es común en procesamiento de texto y búsqueda dentro de colecciones de cadenas, donde es necesario filtrar elementos según ciertos criterios de contenido.

## Implementación

La solución se implementa en Python a través de una clase `Solution` que contiene el método `findWordsContaining`. Este método recibe un arreglo de palabras y un carácter, y devuelve una lista con los índices de las palabras que incluyen el carácter dado.

## Detalles de la implementación

- **Iteración con índice:** Se recorre el arreglo de palabras usando `enumerate` para tener acceso tanto al índice como al contenido de cada palabra.
- **Verificación de contenido:** Se usa la operación `in` para determinar si el carácter buscado está presente dentro de cada palabra.
- **Almacenamiento de índices:** Si la palabra contiene el carácter, su índice se agrega a una lista que será el resultado final.

## Uso

```python
if __name__ == "__main__":
    words = ["leet", "code"]
    x = "e"

    sol = Solution()
    indices = sol.findWordsContaining(words, x)
    print(indices)  # Output esperado: [0, 1]
```

## Conclusión

El ejercicio "Find Words Containing Character" presenta una solución simple y directa para filtrar palabras basándose en la presencia de un carácter específico. Este tipo de problema es habitual en tareas de análisis y manipulación de textos, y la implementación propuesta es eficiente y clara, aprovechando las funcionalidades nativas de Python para manejo de cadenas y colecciones. La técnica empleada refuerza conceptos de iteración, búsqueda y filtrado en estructuras de datos básicas.
