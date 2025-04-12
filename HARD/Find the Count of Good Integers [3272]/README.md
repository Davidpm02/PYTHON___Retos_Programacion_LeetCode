# Find the Count of Good Integers

## Descripción

El ejercicio "Find the Count of Good Integers" plantea un reto de combinatoria y manipulación de números enteros con propiedades específicas. Dado un número de dígitos `n` y un entero positivo `k`, el objetivo es determinar cuántos enteros de exactamente `n` dígitos (sin ceros iniciales) pueden reordenarse para formar un número palindrómico que sea divisible por `k`. A estos números se los denomina **good integers**.

Un entero se considera **k-palindrómico** si:
- Es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
- Es divisible por `k`.

Un número es **good** si alguna de sus permutaciones puede formar un número **k-palindrómico**.

Este problema combina la generación eficiente de palíndromos, la validación de divisibilidad y el conteo de permutaciones sin ceros iniciales.

## Implementación

La solución se desarrolla en Python, implementando una clase `Solution` con el método `countGoodIntegers(n, k)`, el cual devuelve la cantidad de enteros "good" de `n` dígitos.

La estrategia consiste en:

- Generar todos los posibles palíndromos de `n` dígitos (dependiendo de si `n` es par o impar).
- Filtrar aquellos que son divisibles por `k`.
- Para cada palíndromo válido, obtener su frecuencia de dígitos.
- Contar cuántos números diferentes pueden construirse con esa misma frecuencia de dígitos, asegurando que no tengan ceros iniciales.
- Sumar el total de combinaciones válidas que puedan reordenarse para formar al menos un k-palíndromo.

Se utilizan las siguientes herramientas clave:

- `itertools.product`: para generar las mitades de los palíndromos.
- `math.factorial`: para contar las permutaciones posibles de un multiconjunto de dígitos.
- Manipulación directa de strings y enteros para formar y validar palíndromos.

## Uso

Para utilizar este código, simplemente se debe crear una instancia de la clase `Solution` y llamar al método `countGoodIntegers`, proporcionando los valores de `n` y `k` deseados.

```python
if __name__ == "__main__":
    n = 3
    k = 5

    sol = Solution()
    count = sol.countGoodIntegers(n, k)
    print(count)  # Output: 27
```

## Conclusión

El ejercicio "Find the Count of Good Integers" presenta un desafío interesante que requiere combinar generación eficiente de estructuras numéricas (palíndromos), validación matemática (divisibilidad), y conteo combinatorio (permutaciones sin repeticiones ni ceros iniciales). Esta solución proporciona un enfoque optimizado y modular para abordar el problema, destacando el uso de estructuras de datos adecuadas y técnicas de conteo avanzadas. Es un excelente ejemplo práctico de cómo aplicar teoría combinatoria y control de flujo lógico en programación para resolver problemas no triviales.
