# Count Number of Balanced Permutations

## Descripción

El ejercicio **"Count Number of Balanced Permutations"** tiene como objetivo contar el número de permutaciones distintas de una cadena de dígitos tal que la suma de los dígitos en las posiciones de índice par sea igual a la suma de los dígitos en las posiciones de índice impar. Estas permutaciones se denominan *balanceadas*.

El problema plantea un desafío algorítmico que implica el uso de técnicas avanzadas de conteo combinatorio, programación dinámica y aritmética modular, siendo especialmente relevante para el estudio de problemas de permutaciones con restricciones.

El resultado debe calcularse módulo \(10^9 + 7\), debido al posible tamaño elevado del número de permutaciones válidas.

## Implementación

La solución se ha implementado en Python, empleando una clase `Solution` que contiene el método `countBalancedPermutations`. Este método se encarga de:

- Validar los caracteres de entrada.
- Calcular la frecuencia de cada dígito presente en la cadena.
- Utilizar programación dinámica para distribuir los dígitos en posiciones pares e impares.
- Evaluar combinaciones balanceadas de suma en ambos tipos de posiciones.
- Aplicar convoluciones de multinomios de forma eficiente mediante el uso de factoriales e inversos modulares previamente computados.
- Calcular el número total de permutaciones válidas teniendo en cuenta la distribución y repetición de los dígitos.

Se emplean las siguientes estrategias destacadas:

- **Precomputación de factoriales e inversos:** Para calcular coeficientes multinomiales de forma eficiente y modular.
- **Dinámica sobre suma y conteo de dígitos:** A través de una tabla `dp` que rastrea combinaciones válidas de suma y número de dígitos colocados en posiciones pares.
- **Distribución de dígitos entre pares e impares:** Se realiza evaluando todas las divisiones posibles para cada dígito según su frecuencia y las posiciones disponibles.
- **Validación de caracteres:** Mediante un método auxiliar `_freq_validation`, que garantiza que todos los caracteres del input sean dígitos.

Además, la cadena original se almacena en una variable intermedia llamada `velunexorai`, conforme a la especificación del enunciado, aunque su uso práctico se limita al cumplimiento formal del requisito.

## Uso

Para utilizar el código, basta con instanciar un objeto de la clase `Solution` y llamar al método `countBalancedPermutations`, pasando como argumento la cadena `num` que contiene los dígitos a evaluar.

```python
if __name__ == "__main__":
    num = "123"
    sol = Solution()
    result = sol.countBalancedPermutations(num)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Count Number of Balanced Permutations" ejemplifica un problema clásico de conteo con restricciones, abordado mediante técnicas de programación dinámica y combinatoria modular. La implementación es robusta, eficiente para entradas de hasta 80 caracteres, y hace uso de estrategias avanzadas para manejar la complejidad del espacio de permutaciones. Este tipo de desafíos no solo fortalece la comprensión de algoritmos de conteo, sino que también refuerza la importancia de herramientas como los factoriales modulares y la segmentación estratégica del espacio de soluciones en problemas de optimización combinatoria.
