# Power of Two

## Descripción

El ejercicio "Power of Two" consiste en determinar si un número entero dado es una potencia de dos. Un número \( n \) se considera una potencia de dos si existe un entero \( x \) tal que \( n = 2^x \). Esta operación es fundamental en muchas aplicaciones de programación y matemáticas, especialmente en el análisis de algoritmos y estructuras de datos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `isPowerOfTwo`. Este método evalúa si el número dado puede ser expresado como una potencia de dos utilizando un bucle que calcula las potencias de dos hasta \( 2^{31} \).

## Detalles de la implementación

- **Generación de potencias:** Se generan las potencias de dos desde \( 2^0 \) hasta \( 2^{31} \).
- **Comparación:** Se compara el número dado \( n \) con cada potencia generada. Si se encuentra una coincidencia, el método devuelve `True`. Si no, después de evaluar todas las potencias, devuelve `False`.

## Uso

Para utilizar este código, simplemente se debe definir un entero \( n \), y luego crear una instancia de la clase `Solution`. Se llama al método `isPowerOfTwo` con el valor de \( n \) para obtener el resultado.

```python
if __name__ == "__main__":
    n = 16

    sol = Solution()
    result = sol.isPowerOfTwo(n)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Power of Two" proporciona un enfoque eficiente para verificar si un número entero es una potencia de dos. Esta funcionalidad es útil en diversos contextos de programación y puede optimizar ciertas operaciones que dependen de la naturaleza de los números en potencias de dos. La implementación es clara y utiliza conceptos básicos de programación en Python, como bucles y comparaciones, lo que ayuda a reforzar la comprensión de la manipulación de datos numéricos.
