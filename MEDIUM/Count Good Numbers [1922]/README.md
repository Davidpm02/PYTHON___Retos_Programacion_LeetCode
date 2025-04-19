# Count Good Numbers

## Descripción

El ejercicio "Count Good Numbers" consiste en calcular cuántas cadenas de dígitos de longitud `n` pueden ser consideradas "buenas", bajo una condición específica: los dígitos en las posiciones pares (0-indexadas) deben ser pares (0, 2, 4, 6, 8) y los dígitos en las posiciones impares deben ser primos (2, 3, 5, 7).

Este problema pone en práctica conceptos fundamentales de teoría de números y optimización algorítmica, especialmente cuando se trabaja con valores grandes de `n`, donde el uso de técnicas eficientes de exponenciación modular es clave para mantener el rendimiento y evitar sobreflujo de enteros.

## Implementación

La solución está implementada en Python utilizando una clase `Solution` con un único método llamado `countGoodNumbers`. Este método se encarga de calcular de forma eficiente el número total de combinaciones válidas ("números buenos") de longitud `n`, retornando el resultado módulo `10^9 + 7`.

## Detalles de la implementación

- **Modularidad:** Se define una constante `MOD = 10^9 + 7`, que se utiliza para realizar todas las operaciones bajo este módulo y así evitar desbordamientos numéricos, dado que `n` puede ser extremadamente grande (hasta `10^15`).
- **Distribución de posiciones:** Las posiciones pares (0, 2, 4, ...) son aquellas en las que se permiten 5 posibles dígitos (0, 2, 4, 6, 8), y las impares (1, 3, 5, ...) tienen 4 posibilidades (2, 3, 5, 7).
- **Exponenciación rápida:** Se implementa una función auxiliar `power_mod` que realiza una exponenciación modular eficiente (también conocida como "binary exponentiation") para calcular potencias grandes de forma recursiva en tiempo logarítmico.

El resultado final se obtiene multiplicando las posibles combinaciones en posiciones pares por las combinaciones en posiciones impares, todo bajo el módulo definido.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `countGoodNumbers` pasando como argumento la longitud deseada `n`. A continuación se muestra cómo hacerlo:

```python
if __name__ == "__main__":
    n = 50

    sol = Solution()
    result = sol.countGoodNumbers(n)
    print(result)  # Output esperado: 564908303
```

## Conclusión

El ejercicio "Count Good Numbers" ofrece un escenario excelente para practicar técnicas de optimización algorítmica y cálculo modular. Este tipo de problemas son comunes en competencias de programación y entrevistas técnicas, ya que permiten evaluar la capacidad de abstraer patrones numéricos y aplicar algoritmos eficientes como la exponenciación rápida. La solución propuesta es altamente escalable, permitiendo manejar valores de n muy grandes sin comprometer la eficiencia ni la precisión del cálculo.
