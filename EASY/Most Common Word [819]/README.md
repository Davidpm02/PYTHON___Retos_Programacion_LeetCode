# Most Common Word

## Descripción

El ejercicio "Most Common Word" consiste en identificar la palabra más frecuente en un párrafo dado, excluyendo un conjunto de palabras prohibidas. Este problema se basa en el análisis de texto, donde las palabras deben ser consideradas de manera insensible a mayúsculas y sin incluir caracteres de puntuación. El resultado garantiza que haya una palabra no prohibida más común, y esta debe retornarse en minúsculas.

## Implementación

La solución se implementa en Python utilizando una clase `Solution`, la cual contiene el método `mostCommonWord`. Este método procesa el párrafo dado para eliminar caracteres de puntuación, convertir el texto a minúsculas y contar la frecuencia de las palabras que no están en la lista de palabras prohibidas.

### Detalles de la implementación

- **Eliminación de caracteres no válidos:** Se remueven caracteres como `!?',;.` del texto de entrada.
- **Normalización del texto:** Se convierte el texto completo a minúsculas para garantizar insensibilidad a mayúsculas y minúsculas.
- **Filtrado de palabras prohibidas:** Las palabras especificadas en la lista `banned` se eliminan del párrafo.
- **Conteo de palabras:** Se utiliza la clase `Counter` del módulo `collections` para determinar la palabra más frecuente.

## Uso

El siguiente código muestra cómo utilizar la implementación. Defina el párrafo de entrada y la lista de palabras prohibidas, luego cree una instancia de la clase `Solution` y llame al método `mostCommonWord` para obtener la palabra más común.

## Conclusión

El ejercicio "Most Common Word" combina técnicas de procesamiento de texto y análisis de frecuencia para identificar patrones en datos textuales. La solución implementada es robusta y abarca casos comunes, como la eliminación de caracteres no válidos y la normalización del texto. Este enfoque es particularmente útil en aplicaciones de análisis textual y minería de datos, proporcionando una herramienta eficiente para determinar términos relevantes en conjuntos de datos basados en texto.
