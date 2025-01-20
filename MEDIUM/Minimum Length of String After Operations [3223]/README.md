# Minimum Length of String After Operations

## Descripción

El ejercicio **"Minimum Length of String After Operations"** consiste en reducir una cadena de caracteres `s` a su longitud mínima aplicando repetidamente una operación de eliminación. En cada operación, se eliminan caracteres adyacentes a ambos lados de un índice específico, siempre que estos sean iguales al carácter del índice seleccionado. El objetivo es retornar la longitud mínima de la cadena tras realizar todas las operaciones posibles.

Este problema se centra en la manipulación de cadenas, la implementación eficiente de operaciones repetitivas, y el uso de estructuras como contadores para simplificar las validaciones necesarias.

## Implementación

La implementación se realiza en Python, utilizando la clase `Solution` y el método `minimumLength`. El proceso principal del método incluye:

1. **Contar las ocurrencias de los caracteres:** Utiliza la estructura `Counter` de la biblioteca estándar `collections` para calcular la frecuencia de cada carácter en la cadena.
2. **Simplificación de caracteres:** Recoge caracteres y sus frecuencias para determinar su contribución mínima a la longitud final tras aplicar operaciones de eliminación.
3. **Reducción y combinación:** Con base en las reglas del problema, se conserva el conteo adecuado de caracteres no eliminados y se calcula la longitud de la cadena resultante.

El enfoque se enfoca en optimizar el manejo de los datos de entrada para procesar cadenas largas de manera eficiente.

## Uso

Para utilizar este código, define una cadena de caracteres `s`. Luego, crea una instancia de la clase `Solution` y llama al método `minimumLength` pasando la cadena como argumento:

```python
if __name__ == "__main__":
    s = "abaacbcbb"

    sol = Solution()
    result = sol.minimumLength(s)
    print(result)  # Debería imprimir la longitud mínima de la cadena tras realizar todas las operaciones
```

## Conclusión

El ejercicio "Minimum Length of String After Operations" es un desafío interesante que combina el procesamiento eficiente de cadenas con el uso de operaciones algorítmicas como contadores y estructuras de datos simples. Su solución no solo es práctica para problemas similares en manipulación de textos, sino que también es una buena manera de reforzar conceptos relacionados con la optimización de algoritmos para estructuras secuenciales. La implementación demuestra cómo Python puede manejar operaciones complejas de forma concisa y efectiva.
