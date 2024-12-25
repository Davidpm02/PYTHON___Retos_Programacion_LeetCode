# Prime Number of Set Bits in Binary Representation

## Descripción

El ejercicio "Prime Number of Set Bits in Binary Representation" consiste en determinar cuántos números en el rango inclusivo `[left, right]` tienen un número primo de bits establecidos (`1`) en su representación binaria. El número de bits establecidos corresponde al número de `1`s presentes al representar un número en binario.

Este problema combina conceptos de representaciones binarias y la identificación de números primos, aplicándolos de manera eficiente en un rango de valores.

## Implementación

La solución se implementa en Python mediante una clase `Solution` con un método `countPrimeSetBits`. A continuación, se describen los pasos de la solución:

1. **Cálculo de representaciones binarias:**
   - Se obtienen las representaciones binarias de todos los números en el rango `[left, right]`.

2. **Conteo de bits establecidos:**
   - Se cuenta la cantidad de `1`s en cada representación binaria.

3. **Verificación de primos:**
   - Para cada número de bits establecidos, se verifica si es un número primo mediante divisiones sucesivas.

4. **Acumulación de resultados:**
   - Se incrementa un contador cada vez que un número de bits establecidos resulta ser primo.

## Uso

Para utilizar este código, crea una instancia de la clase Solution y llama al método countPrimeSetBits, pasando los valores left y right como parámetros. El método devolverá la cantidad de números en el rango que cumplen con la condición.

```python
if __name__ == "__main__":
    left = 6
    right = 10

    sol = Solution()
    result = sol.countPrimeSetBits(left, right)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Prime Number of Set Bits in Binary Representation" demuestra cómo trabajar con representaciones binarias y aplicar propiedades matemáticas, como la determinación de números primos, en un contexto programático. La implementación resuelve el problema de manera directa y eficiente utilizando técnicas básicas de manejo de cadenas, ciclos y operaciones aritméticas. Este enfoque refuerza conceptos fundamentales de programación mientras ofrece un ejemplo práctico de cómo combinar distintos dominios de conocimiento.
