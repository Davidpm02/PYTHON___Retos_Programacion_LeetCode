# Count Symmetric Integers

## Descripción

El ejercicio "Count Symmetric Integers" tiene como objetivo determinar cuántos números enteros simétricos existen dentro de un rango dado, definido por los enteros `low` y `high`. Un número se considera *simétrico* si tiene un número par de cifras y la suma de su primera mitad de dígitos es igual a la suma de su segunda mitad.

Este tipo de problema es útil para practicar operaciones sobre cadenas numéricas, manipulación de listas y control de flujo en estructuras iterativas, lo que lo convierte en un buen ejercicio para fortalecer habilidades de programación en Python y el razonamiento lógico aplicado a datos numéricos.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `countSymmetricIntegers`. Este método realiza una iteración sobre todos los enteros dentro del rango especificado (`low` a `high`), y determina si cada uno de ellos cumple con la condición de simetría.

## Detalles de la implementación

- **Filtrado de números con cantidad impar de cifras:** Se omiten de inmediato, ya que no pueden ser simétricos por definición.
- **Separación en mitades:** Para cada número válido, se convierte en cadena y se divide en dos listas de enteros: la primera mitad y la segunda mitad.
- **Verificación de simetría:** Se calcula la suma de cada mitad y se compara. Si ambas sumas son iguales, el número es simétrico y se incrementa el contador.

## Uso

Para utilizar este código, basta con instanciar la clase `Solution` y llamar al método `countSymmetricIntegers` pasando los valores deseados para `low` y `high`.

```python
if __name__ == "__main__":
    low = 1
    high = 100

    sol = Solution()
    symmetric_count = sol.countSymmetricIntegers(low, high)
    print(symmetric_count)  # Output: 9
```

## Conclusión

El ejercicio "Count Symmetric Integers" proporciona una forma efectiva de explorar conceptos relacionados con la manipulación de enteros como cadenas, el uso de estructuras de control para filtrar condiciones específicas, y la aplicación de operaciones aritméticas sobre subconjuntos de dígitos. La solución propuesta es clara y comprensible, aprovechando las características del lenguaje Python para trabajar de manera eficiente con listas y cadenas. Este ejercicio también refuerza la importancia de validar condiciones estructurales (como la longitud par de los números) antes de aplicar lógica adicional, asegurando así un enfoque robusto y preciso.
