# Ugly Number

## Descripción

El ejercicio "Ugly Number" consiste en determinar si un número entero dado es un "número feo" (ugly number). Un número feo es aquel cuyo conjunto de factores primos está limitado a los números 2, 3 y 5. Esto implica que, para un número dado, todos sus divisores deben ser una combinación de estos tres factores. El objetivo es devolver `True` si el número es feo, y `False` en caso contrario.

Este tipo de problema es relevante en el análisis de algoritmos y matemáticas numéricas, donde la descomposición en factores primos tiene muchas aplicaciones.

## Implementación

La solución se implementa utilizando la clase `Solution`, que contiene el método `isUgly`. Este método sigue un enfoque iterativo para dividir el número dado por los factores primos 2, 3 y 5 siempre que sea divisible por estos números. Si después de estas divisiones el número se convierte en 1, significa que todos sus factores eran 2, 3 o 5, y por lo tanto, es un número feo. Si en algún momento el número no es divisible por 2, 3 o 5, el método devuelve `False`.

### Detalles de la implementación

- **Verificación de valores límite:** Si `n` es igual a 1, se considera un número feo, ya que no tiene factores primos.
- **Descomposición en factores:** Se divide repetidamente el número por 2, 3 o 5 hasta que ya no sea divisible por ninguno de ellos.
- **Caso especial para 0 y negativos:** Cualquier número menor o igual a 0 no es un número feo.

## Uso

Para utilizar este código, basta con crear una instancia de la clase `Solution` y llamar al método `isUgly` con un número entero como argumento. El método devolverá `True` si el número es feo, o `False` en caso contrario.

```python
if __name__ == "__main__":
    sol = Solution()

    n = 6
    print(sol.isUgly(n))  # Output: True

    n = 14
    print(sol.isUgly(n))  # Output: False
```

## Conclusión

El ejercicio "Ugly Number" permite practicar la descomposición en factores primos y la verificación de propiedades numéricas específicas. La solución implementada es eficiente, dado que descompone el número solo en factores 2, 3 y 5. Este problema es útil en muchos algoritmos que requieren trabajar con divisibilidad y propiedades de los números enteros, además de fortalecer el uso de bucles y condiciones en Python.
