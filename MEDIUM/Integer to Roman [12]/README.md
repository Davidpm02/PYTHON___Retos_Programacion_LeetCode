# Integer to Roman

## Descripción

Este ejercicio se enfoca en la conversión de números enteros a numerales romanos. Los numerales romanos se componen de siete símbolos distintos que representan diferentes valores:

- I: 1
- V: 5
- X: 10
- L: 50
- C: 100
- D: 500
- M: 1000

Los numerales romanos generalmente se escriben del mayor al menor de izquierda a derecha. Existen reglas específicas para ciertas combinaciones que implican la substracción para formar otros números (por ejemplo, IV para el 4 y IX para el 9). El desafío del ejercicio es convertir un número entero dado, en el rango de 1 a 3999, a su representación en numeral romano.

## Implementación

El código está estructurado en una clase llamada `Solution` que contiene el método `intToRoman`, el cual recibe un número entero y devuelve su representación en numeral romano. El método utiliza:

- Un diccionario para mapear los valores enteros con sus respectivos símbolos romanos.
- Un proceso iterativo que, comenzando por el valor más grande posible, determina cuántas veces cada símbolo debe aparecer en la representación final.

Este enfoque garantiza que el numeral romano generado esté correctamente formateado y cumpla con las reglas tradicionales de los numerales romanos.

## Uso

Para utilizar la función `intToRoman`, primero se debe instanciar un objeto de la clase `Solution`. Luego, se llama al método `intToRoman` pasando un número entero como argumento. Por ejemplo:

```python
solution = Solution()
result = solution.intToRoman(1994)
print(result)  # Output: "MCMXCIV"
```

## Conclusión

El ejercicio "Integer to Roman" es una excelente manera de entender la aplicación de diccionarios y estructuras de control en Python para resolver problemas de conversión basados en reglas específicas. Además, refuerza el conocimiento sobre cómo estructurar las clases y métodos de una manera que facilite el uso y la comprensión del código.
