# Self Dividing Numbers

## Descripción

El ejercicio "Self Dividing Numbers" busca identificar todos los números en un rango dado que cumplan con la propiedad de ser divisibles por cada uno de los dígitos que los componen. Un número es considerado "self-dividing" si:

1. No contiene el dígito `0`.
2. Es divisible por cada uno de sus dígitos.

Por ejemplo, el número 128 es un número "self-dividing" porque \(128 \% 1 = 0\), \(128 \% 2 = 0\), y \(128 \% 8 = 0\).

## Implementación

La solución está implementada en Python mediante una clase `Solution` que contiene el método `selfDividingNumbers`. Este método toma dos enteros (`left` y `right`) como entrada y devuelve una lista con todos los números "self-dividing" dentro del rango cerrado \([left, right]\).

### Detalles de la implementación

- **Extracción de dígitos:** Cada número en el rango se descompone en una lista de sus dígitos individuales para facilitar las operaciones.
- **Validación de divisibilidad:** Se verifica si cada dígito es divisor del número original utilizando el operador módulo (\(%\)).
- **Filtrado:** Los números que contienen el dígito `0` se descartan de inmediato, ya que no pueden ser divisibles por 0.
- **Construcción de resultados:** Los números que cumplen todas las condiciones se almacenan en una lista de salida.

## Uso

Para utilizar este código, crea una instancia de la clase Solution e invoca el método selfDividingNumbers con los valores de rango deseados (leftleft y rightright) como argumentos. Esto devolverá una lista con todos los números que cumplen con la propiedad "self-dividing" dentro del rango especificado.

```python
if __name__ == "__main__":
    sol = Solution()
    result = sol.selfDividingNumbers(1, 22)
    print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

## Conclusión

El ejercicio "Self Dividing Numbers" es un buen ejemplo de cómo procesar datos numéricos y aplicar operaciones iterativas para validar condiciones específicas. La solución presentada aprovecha las características de Python, como las listas por comprensión y funciones integradas, para garantizar un código claro, eficiente y fácil de mantener. Esta implementación es adecuada para abordar tareas similares en análisis numérico y procesamiento de datos.
