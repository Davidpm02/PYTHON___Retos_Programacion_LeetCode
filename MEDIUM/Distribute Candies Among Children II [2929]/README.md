# Distribute Candies Among Children II

## Descripción

El ejercicio "Distribute Candies Among Children II" consiste en calcular el número total de formas posibles de distribuir **n** caramelos entre 3 niños, bajo la restricción de que ningún niño reciba más caramelos que un límite especificado. Este problema es una variante clásica de conteo combinatorio con restricciones, útil para entender técnicas de combinatoria y principios de inclusión-exclusión.

## Implementación

La implementación se basa en el uso de combinatoria matemática para contar el número de soluciones enteras no negativas a la ecuación \(a + b + c = n\), donde \(a, b, c\) representan los caramelos recibidos por cada niño.

### Detalles de la implementación

- **Combinaciones sin restricciones:** Se calcula el total de distribuciones posibles sin limitar la cantidad máxima de caramelos por niño, usando el concepto de "combinaciones con repetición" expresado por la fórmula \(\binom{n+2}{2}\).
- **Principio de inclusión-exclusión:** Para aplicar la restricción del límite, se resta el número de distribuciones inválidas (donde uno o más niños superan el límite) ajustando el conteo mediante el principio de inclusión-exclusión, sumando y restando combinaciones correspondientes a subconjuntos de niños que exceden el límite.

El código está implementado en Python dentro de la clase `Solution`, que contiene el método `distributeCandies`.

## Uso

Para utilizar el código, simplemente se debe instanciar la clase `Solution` y llamar al método `distributeCandies` pasando como argumentos el número total de caramelos y el límite máximo por niño. El método devuelve un entero con el número total de formas válidas de distribuir los caramelos.

```python
if __name__ == "__main__":
    n = 5
    limit = 2

    sol = Solution()
    ways = sol.distributeCandies(n, limit)
    print(ways)  # Resultado esperado: 3
```

## Conclusión

El ejercicio "Distribute Candies Among Children II" muestra cómo aplicar técnicas combinatorias y el principio de inclusión-exclusión para resolver problemas de conteo con restricciones. Este enfoque es eficiente y escalable, incluso para valores grandes de n y limit, gracias a la utilización de la función combinatoria comb de Python. Además, el método refuerza conceptos importantes en matemáticas discretas y programación combinatoria que son fundamentales en diversos ámbitos del Machine Learning y análisis de datos.
