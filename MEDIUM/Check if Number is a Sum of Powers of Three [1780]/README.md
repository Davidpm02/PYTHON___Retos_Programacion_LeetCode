# Check if Number is a Sum of Powers of Three

## Descripción

El ejercicio "Check if Number is a Sum of Powers of Three" consiste en determinar si un número entero dado puede representarse como la suma de distintas potencias de tres. Un número entero \( y \) es una potencia de tres si existe un entero \( x \) tal que \( y = 3^x \). Si el número puede expresarse como la suma de estos valores, la función devuelve `True`, de lo contrario, devuelve `False`.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `checkPowersOfThree`. Este método evalúa si un número dado puede descomponerse en la suma de potencias de tres utilizando la representación en base 3.

## Detalles de la implementación

- **Conversión a base 3:** Se divide el número sucesivamente entre 3 para obtener sus restos.
- **Verificación de coeficientes:** Si en la representación base 3 aparece el valor `2`, el número no puede representarse como una suma de potencias de tres y se devuelve `False`.
- **Resultado final:** Si todos los coeficientes en la representación base 3 son `0` o `1`, el número es válido y se devuelve `True`.

## Uso

Para utilizar este código, se debe definir el número entero `n`, luego crear una instancia de la clase `Solution` y llamar al método `checkPowersOfThree` con `n` como parámetro.

```python
if __name__ == "__main__":
    n = 12
    
    sol = Solution()
    result = sol.checkPowersOfThree(n)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Check if Number is a Sum of Powers of Three" permite verificar de manera eficiente si un número puede representarse como la suma de distintas potencias de tres. Utilizando la conversión a base 3, se puede determinar rápidamente la validez de la representación sin necesidad de realizar cálculos extensivos con potencias. Este enfoque demuestra una aplicación práctica de la aritmética en diferentes bases y su utilidad en problemas matemáticos y computacionales.
