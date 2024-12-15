# Perfect Number

## Descripción

El ejercicio "Perfect Number" consiste en determinar si un número dado es un "número perfecto". Un número perfecto es un número entero positivo que es igual a la suma de sus divisores positivos, excluyendo el mismo número. Este tipo de problema se relaciona con el concepto de divisores de números y tiene aplicaciones tanto en la teoría de números como en la optimización de algoritmos.

## Implementación

La implementación se realiza en Python utilizando una clase llamada `Solution`, que contiene el método `checkPerfectNumber`. Este método verifica si un número dado es un número perfecto según la definición mencionada anteriormente.

### Detalles de la implementación

- **Divisores de un número:** La función primero calcula los divisores de un número `num`. Si `num` es mayor que 10,000, la función calcula los divisores utilizando la raíz cuadrada de `num` para reducir el número de iteraciones necesarias, al tratar de encontrar divisores hasta esa raíz.
- **Suma de los divisores:** Se suma la lista de divisores y se compara con el número original.
- **Optimización:** Para números más pequeños, se calcula directamente la lista de divisores hasta la mitad del número. Para números más grandes, se optimiza el cálculo considerando solo los divisores hasta la raíz cuadrada de `num`.

## Uso

Para utilizar este código, simplemente se debe instanciar la clase `Solution` y luego llamar al método `checkPerfectNumber` pasando como parámetro el número a verificar. El método retornará `True` si el número es perfecto, o `False` en caso contrario.

```python
if __name__ == "__main__":
    num = 28
    sol = Solution()
    is_perfect = sol.checkPerfectNumber(num)
    print(is_perfect)  # Output: True
```

## Conclusión

El ejercicio "Perfect Number" es una forma efectiva de verificar si un número dado es perfecto. Mediante el uso de optimizaciones como el cálculo de divisores hasta la raíz cuadrada para números grandes y una solución directa para números pequeños, el algoritmo logra una eficiencia considerable. Este tipo de ejercicio no solo refuerza la comprensión sobre divisores y la teoría de números, sino también cómo abordar problemas de optimización en programación. Además, proporciona una solución clara y fácil de implementar para un tipo de número interesante en matemáticas.
