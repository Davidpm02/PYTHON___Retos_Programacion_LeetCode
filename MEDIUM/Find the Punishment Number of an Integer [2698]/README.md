# Find the Punishment Number of an Integer

## Descripcion

El ejercicio "Find the Punishment Number of an Integer" consiste en calcular el "punishment number" de un entero positivo `n`. Este se define como la suma de los cuadrados de todos los enteros `i` en el rango `[1, n]` que cumplen con la siguiente condición:

- El valor decimal de `i * i` puede ser particionado en subcadenas contiguas de tal forma que la suma de estas subcadenas sea igual a `i`.

Este problema implica técnicas de manipulación de cadenas, recursión y backtracking para verificar si un número al cuadrado puede ser particionado de la manera deseada.

## Implementacion

La solución se implementa en Python dentro de la clase `Solution`, la cual contiene el método `punishmentNumber`. Este método calcula el número de castigo verificando cada número en el rango `[1, n]` para determinar si su cuadrado puede ser particionado según la condición dada.

### Detalles de la Implementación

- **Verificación de la condición de partición**: Se usa una función recursiva `can_partition` que verifica si un número al cuadrado puede dividirse en subcadenas cuya suma sea igual al número original.
- **Optimización con propiedades de múltiplos de 9**: Se usa la regla de divisibilidad por 9 para descartar ciertos números y reducir la cantidad de cálculos.
- **Acumulación de la suma**: Se recorren todos los números desde `1` hasta `n` y se acumulan los valores de sus cuadrados si cumplen la condición.

## Uso

Para utilizar este código, se debe instanciar la clase `Solution` y llamar al método `punishmentNumber` con un entero `n` como entrada:

```python
if __name__ == "__main__":
    n = 10
    sol = Solution()
    result = sol.punishmentNumber(n)
    print(result)  # Output: 182
```

## Conclusion

El ejercicio "Find the Punishment Number of an Integer" es un problema interesante que combina manipulación de cadenas, aritmética y algoritmos de backtracking. La solución implementada es eficiente al evitar cálculos innecesarios mediante reglas matemáticas y permite evaluar números hasta `n = 1000`. Su comprensión ayuda a reforzar habilidades en programación dinámica, optimización y manipulación de cadenas en Python.
