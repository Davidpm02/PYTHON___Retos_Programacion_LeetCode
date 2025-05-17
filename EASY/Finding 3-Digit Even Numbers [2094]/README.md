# Finding 3-Digit Even Numbers

## Descripción

El ejercicio **"Finding 3-Digit Even Numbers"** consiste en encontrar todos los enteros únicos de tres dígitos que pueden formarse a partir de una lista de dígitos dada. Los enteros deben cumplir tres condiciones fundamentales:

1. Deben estar compuestos por exactamente tres dígitos de la lista original, sin añadir dígitos externos.
2. No deben comenzar con cero (para evitar números con ceros a la izquierda).
3. Deben ser pares, es decir, su último dígito debe ser par.

Este tipo de ejercicio resulta muy útil para practicar operaciones con combinaciones, manipulación de listas y validaciones condicionales.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que contiene el método `findEvenNumbers`. Este método genera todos los números pares de tres dígitos posibles, y luego evalúa si cada uno de ellos puede formarse utilizando únicamente los dígitos presentes en la lista de entrada.

## Detalles de la implementación

- **Generación de candidatos:** Se genera una lista de números pares de tres dígitos en el rango de `100` a `999`, garantizando que no hay ceros a la izquierda y que el número es par.
- **Verificación de composición:** Para cada número candidato, se verifica si puede formarse con los dígitos disponibles. Se utiliza una copia de la lista original de dígitos para evitar modificar la lista original durante la validación.
- **Control de repeticiones:** Cada dígito del número debe encontrarse en la lista, y en la cantidad adecuada (por ejemplo, si el número requiere dos dígitos 2, deben estar disponibles dos veces en la lista).
- **Filtrado y ordenación:** Solo se añaden al resultado aquellos números que cumplen todas las condiciones, y se devuelve la lista resultante en orden ascendente.

## Uso

Para utilizar este código, basta con definir el array de dígitos y crear una instancia de la clase `Solution`. A continuación, se llama al método `findEvenNumbers` pasando como argumento dicho array. El método devolverá una lista ordenada de los enteros válidos.

```python
if __name__ == "__main__":
    digits = [2, 1, 3, 0]

    sol = Solution()
    valid_numbers = sol.findEvenNumbers(digits)
    print(valid_numbers)  # Output: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
```

## Conclusión

El ejercicio "Finding 3-Digit Even Numbers" proporciona una oportunidad para reforzar conceptos clave como la generación de combinaciones válidas, el manejo de condiciones específicas (como la paridad y los ceros iniciales), y el uso eficiente de estructuras de datos en Python. La solución presentada es clara, modular y fácilmente extensible, lo que la convierte en una base sólida para abordar problemas similares en entrevistas técnicas o en desafíos de programación.
