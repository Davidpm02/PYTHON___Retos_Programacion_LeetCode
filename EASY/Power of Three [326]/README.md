# Power of Three

## Descripción

El ejercicio "Power of Three" tiene como objetivo determinar si un número entero dado es una potencia de tres. En otras palabras, el problema consiste en verificar si existe un número entero x tal que el número de entrada n sea igual a 3^x. Este tipo de operaciones es relevante en múltiples áreas, como la teoría de números y la informática, donde la manipulación de potencias de números primos es común.

## Implementación

La implementación se realiza en Python dentro de la clase Solution, que contiene el método isPowerOfThree. Este método emplea una combinación de condiciones y un bucle while para determinar si el número dado es divisible repetidamente por 3, hasta llegar a 1, momento en el que se concluye que el número es efectivamente una potencia de tres.

### Detalles de la implementación

* Validación inicial: Se asegura que el número n sea mayor que 0, ya que las potencias de tres son siempre positivas.

* Caso base: Si n es igual a 1, se devuelve True directamente, ya que 3^0 = 1.

* Bucle de división: Mientras n sea divisible por 3, se divide repetidamente. Si en algún momento n es menor que 3 y no es exactamente 1 o 3, se concluye que no es una potencia de tres.

* Manejo de errores: Se utiliza una excepción AssertionError para capturar números no válidos en las divisiones.

## Uso

Para utilizar este código, simplemente se debe crear una instancia de la clase Solution y llamar al método isPowerOfThree pasando el número entero que se desea evaluar. A continuación, se muestra un ejemplo de uso:

```python
if __name__ == "__main__":
    n = 27

    sol = Solution()
    result = sol.isPowerOfThree(n)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Power of Three" ofrece una solución eficiente para determinar si un número es una potencia de tres utilizando un enfoque iterativo basado en divisiones sucesivas. La implementación es intuitiva y utiliza estructuras de control básicas para resolver el problema, lo que la convierte en una solución adecuada para números dentro de un rango de enteros. Este tipo de problemas refuerza la comprensión sobre divisibilidad y potencias en teoría de números, y proporciona una manera efectiva de trabajar con potencias de bases numéricas.
