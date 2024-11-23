# Reverse Words in a String III

## Descripción

El ejercicio **"Reverse Words in a String III"** consiste en invertir el orden de los caracteres de cada palabra en una cadena, manteniendo tanto los espacios en blanco como el orden original de las palabras.

## Implementación

La solución está implementada en Python dentro de la clase `Solution`, la cual incluye el método `reverseWords`. Este método toma como entrada una cadena `s` y retorna la cadena con todas las palabras invertidas, respetando la separación de palabras original.

### Detalles de la implementación

1. **Separación de palabras:** Se utiliza el método `split()` para dividir la cadena `s` en una lista de palabras.
2. **Inversión de caracteres en cada palabra:** Se emplea una comprensión de listas para invertir cada palabra usando la notación de slicing `[::-1]`.
3. **Recomposición de la cadena:** Las palabras invertidas se vuelven a unir con un espacio intermedio utilizando `" ".join()`.
4. **Devolución del resultado:** La cadena resultante contiene las palabras originales con sus caracteres invertidos.

## Uso

Para utilizar este código, define una cadena que contenga palabras separadas por espacios y crea una instancia de la clase Solution. Llama al método reverseWords con la cadena como argumento para obtener el resultado.

```python
if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    
    sol = Solution()
    result = sol.reverseWords(s)
    print(result)  # Output: "s'teL ekat edoCteeL tsetnoc"
```

## Conclusión

El ejercicio "Reverse Words in a String III" es una tarea práctica que refuerza conceptos fundamentales de manipulación de cadenas en Python, como la división (split), la comprensión de listas y la unión de palabras (join). El enfoque utilizado es eficiente, con una complejidad lineal respecto al tamaño de la cadena. Este problema es relevante en escenarios donde es necesario procesar y transformar texto, como en el desarrollo de aplicaciones de procesamiento de lenguaje natural o formatos de texto dinámicos.
