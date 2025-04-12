# Count the Number of Powerful Integers

## Descripción

El ejercicio **"Count the Number of Powerful Integers"** plantea el problema de contar cuántos enteros dentro de un rango dado `[start, finish]` cumplen con una condición específica: deben ser enteros positivos que terminen con una cadena `s` (es decir, `s` debe ser un sufijo del número), y cada uno de sus dígitos debe ser menor o igual que un límite definido `limit`.

Este tipo de ejercicio combina técnicas de búsqueda por sufijos, autómatas finitos deterministas (DFA) y programación dinámica basada en dígitos (digit DP), lo cual es útil en el contexto de optimización de conteos numéricos sobre restricciones complejas.

## Implementación

La implementación se desarrolla en Python dentro de una clase `Solution`, que contiene el método principal `numberOfPowerfulInt`.

La lógica se basa en tres grandes bloques:

- **Construcción de una tabla de transición tipo DFA**, similar a la usada en el algoritmo de Knuth-Morris-Pratt (KMP), para gestionar de forma eficiente las coincidencias parciales del sufijo `s`.
- **Digit DP con memoización**, utilizada para explorar todas las posibles combinaciones de dígitos que respeten el límite impuesto, y a la vez mantener el seguimiento del estado de coincidencia con el sufijo `s`.
- **Conteo acumulativo entre rangos**, utilizando la técnica `count(finish) - count(start - 1)` para contar de forma eficiente los enteros poderosos entre los dos extremos.

## Uso

Para utilizar este código, basta con crear una instancia de la clase `Solution` e invocar el método `numberOfPowerfulInt` con los parámetros adecuados: `start`, `finish`, `limit`, y el sufijo `s`.

```python
if __name__ == "__main__":
    start = 1
    finish = 6000
    limit = 4
    s = "124"

    sol = Solution()
    result = sol.numberOfPowerfulInt(start, finish, limit, s)
    print(result)  # Output: 5
```

## Conclusión

El ejercicio "Count the Number of Powerful Integers" representa una excelente combinación entre teoría de autómatas y técnicas de programación dinámica sobre dígitos. Gracias al uso del autómata de transición basado en el patrón s, se consigue un control eficiente de las coincidencias de sufijos. La programación dinámica con memoización permite recorrer el espacio de soluciones de manera óptima, evitando cálculos redundantes. Este enfoque es fundamental en problemas que implican conteos en grandes rangos bajo múltiples restricciones, y refuerza conceptos avanzados tanto de teoría de lenguajes formales como de optimización computacional.
