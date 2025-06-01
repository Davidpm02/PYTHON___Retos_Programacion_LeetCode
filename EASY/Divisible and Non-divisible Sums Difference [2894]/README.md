# Divisible and Non-divisible Sums Difference

## Descripción

El ejercicio "Divisible and Non-divisible Sums Difference" consiste en calcular la diferencia entre la suma de todos los enteros en el rango `[1, n]` que **no son divisibles** por un número `m` y la suma de aquellos que **sí son divisibles** por `m`.

Este tipo de problema es útil para reforzar conceptos relacionados con divisibilidad, uso de bucles y condicionales, así como la implementación eficiente de operaciones aritméticas dentro de un rango numérico definido.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `differenceOfSums`. Este método recorre todos los números desde `1` hasta `n` y evalúa si cada uno es divisible entre `m`. Dependiendo del resultado, acumula la suma en `num1` (no divisibles) o `num2` (divisibles), y finalmente retorna la diferencia `num1 - num2`.

## Detalles de la implementación

- **Inicialización:** Se crean dos acumuladores `num1` y `num2`, inicializados en cero.
- **Recorrido:** Se itera sobre todos los enteros en el intervalo `[1, n]`.
- **Evaluación de divisibilidad:** Mediante el operador módulo (`%`), se determina si el número es divisible por `m`.
- **Acumulación:** Dependiendo del resultado anterior, el número se suma a `num1` o `num2`.
- **Resultado:** Finalmente se devuelve la diferencia `num1 - num2`.

## Uso

Para utilizar este código, basta con definir los valores de `n` y `m`, crear una instancia de la clase `Solution` y llamar al método `differenceOfSums` con los argumentos apropiados:

```python
if __name__ == "__main__":
    n = 10
    m = 3

    sol = Solution()
    diff = sol.differenceOfSums(n, m)
    print(diff)  # Output: 19
```

## Conclusión

El ejercicio "Divisible and Non-divisible Sums Difference" proporciona una forma sencilla y clara de trabajar con la lógica de divisibilidad y acumulación de sumas dentro de un rango. Es una excelente práctica para el manejo de estructuras de control y operaciones aritméticas en Python. Su implementación es directa, eficiente y de fácil comprensión, lo que lo hace ideal para principiantes que buscan afianzar fundamentos básicos de programación.
