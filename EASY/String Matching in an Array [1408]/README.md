# String Matching in an Array

## Descripción

El ejercicio "String Matching in an Array" tiene como objetivo encontrar todas las cadenas en un arreglo que sean subcadenas de alguna otra cadena dentro del mismo arreglo. Una subcadena es una secuencia contigua de caracteres contenida dentro de otra cadena. El resultado se devuelve como una lista que contiene las cadenas identificadas como subcadenas.

Este problema es útil para explorar conceptos de manipulación de cadenas, detección de patrones y optimización a través de estructuras como conjuntos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `stringMatching`. Este método evalúa cada palabra de la lista y comprueba si puede ser encontrada como una subcadena en alguna de las otras palabras.

### Detalles de la implementación

1. **Uso de un conjunto:**  
   - Se emplea un conjunto (`set`) para almacenar las cadenas identificadas como subcadenas, evitando duplicados automáticamente.

2. **Comparación exhaustiva:**  
   - El método utiliza dos bucles anidados para comparar cada cadena de la lista con todas las demás cadenas.
   - Si una cadena es encontrada como subcadena de otra y no es igual a la cadena en sí misma, se agrega al conjunto.

3. **Conversión del resultado:**  
   - Finalmente, el conjunto de subcadenas se convierte a una lista y se retorna como resultado.

Este enfoque asegura que se detecten todas las subcadenas posibles dentro del conjunto dado.

## Uso

Para utilizar este código, define una lista de palabras y llama al método `stringMatching` proporcionando esta lista como entrada.

```python
if __name__ == "__main__":
    words = ["mass", "as", "hero", "superhero"]

    sol = Solution()
    result = sol.stringMatching(words)
    print(result)  # Output: ["as", "hero"]
```

## Conclusión

El ejercicio "String Matching in an Array" es una herramienta práctica para trabajar con cadenas de texto y entender cómo identificar patrones dentro de un conjunto de datos. La solución implementada aprovecha la simplicidad del uso de conjuntos para evitar duplicados y emplea comparaciones exhaustivas para garantizar resultados precisos. Este problema fortalece habilidades en el análisis de cadenas y el diseño de algoritmos eficientes para detectar patrones, fundamentales en campos como la informática y el análisis de datos.
