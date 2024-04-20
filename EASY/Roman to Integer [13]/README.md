# Roman to Integer

## Descripción

Este ejercicio trata sobre convertir un número representado en numeral romano a su equivalente en entero. Los numerales romanos están formados por siete símbolos diferentes, cada uno con un valor específico. La tarea consiste en interpretar correctamente estos símbolos y sus combinaciones para determinar el valor numérico correspondiente.

El reto adicional radica en comprender y aplicar las reglas de substracción que se utilizan en ciertos casos especiales, como por ejemplo, el numeral para cuatro no es IIII sino IV, donde se resta uno a cinco.

## Implementación

La solución se ha implementado en Python dentro de la clase `Solution`, la cual contiene el método `romanToInt`. Este método toma una cadena de texto representando un número romano y devuelve su valor entero correspondiente.

Detalles técnicos:

- **Diccionario de Valores Romanos**: Se crea un diccionario que mapea cada símbolo romano y sus combinaciones especiales a sus respectivos valores enteros.
- **Procesamiento de la Cadena**: La cadena se procesa de izquierda a derecha, identificando y sumando los valores de cada símbolo o combinación especial encontrada.
- **Manejo de Substracciones Especiales**: Se realiza un manejo específico para los casos donde se aplican las reglas de substracción, verificando si el símbolo actual debe restar valor al siguiente.

## Uso

Para utilizar esta implementación en la conversión de números romanos a enteros, simplemente siga estos pasos:

```python
if __name__ == "__main__":
    roman_numeral = "MCMXCIV"
    solution = Solution()
    integer_value = solution.romanToInt(s=roman_numeral)
    print(integer_value)  # Salida esperada: 1994
```

## Conclusión

La conversión de números romanos a enteros es un problema clásico que no solo pone a prueba la habilidad para manipular cadenas y estructuras de datos, sino también la capacidad de aplicar lógica y reglas específicas de conversión. La implementación proporcionada es robusta y maneja eficientemente los casos de uso comunes y especiales, asegurando una conversión precisa dentro del rango permitido de números romanos válidos.
