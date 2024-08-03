# Length of Last Word

## Descripción

El ejercicio "Length of Last Word" consiste en encontrar la longitud de la última palabra en una cadena de texto que contiene palabras y espacios. Una palabra se define como una subcadena máxima que consiste únicamente en caracteres que no son espacios.

**Ejemplos:**

1. **Input:** s = "Hello World"  
   **Output:** 5  
   **Explicación:** La última palabra es "World" con una longitud de 5.

2. **Input:** s = "   fly me   to   the moon  "  
   **Output:** 4  
   **Explicación:** La última palabra es "moon" con una longitud de 4.

3. **Input:** s = "luffy is still joyboy"  
   **Output:** 6  
   **Explicación:** La última palabra es "joyboy" con una longitud de 6.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `lengthOfLastWord`. Este método se encarga de procesar la cadena de texto, identificar la última palabra y devolver su longitud.

### Detalles de la implementación

- **Inversión de la cadena:** Se invierte la cadena de texto para facilitar la identificación de la última palabra.
- **Contador de longitud:** Se utiliza un contador para medir la longitud de la última palabra, incrementándolo hasta encontrar un espacio después de una secuencia de caracteres no espaciales.

## Uso

Para utilizar este código, simplemente se debe definir la cadena de texto s, y luego crear una instancia de la clase Solution. Se llama al método lengthOfLastWord con esta cadena y se obtiene la longitud de la última palabra.

```python
if __name__ == "__main__":
    s = "   fly me   to   the moon  "

    sol = Solution()
    s_length = sol.lengthOfLastWord(s)
    print(s_length)  # Output: 4
```

## Conclusión

El ejercicio "Length of Last Word" proporciona una manera eficiente de determinar la longitud de la última palabra en una cadena de texto. Esta tarea es común en el procesamiento de textos y tiene aplicaciones prácticas en muchas áreas de la programación y el análisis de datos. La implementación presentada es simple y efectiva, aprovechando las capacidades de manipulación de cadenas en Python para lograr el objetivo de manera clara y concisa.
