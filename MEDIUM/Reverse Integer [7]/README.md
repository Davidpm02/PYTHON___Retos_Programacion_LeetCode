# Reverse Integer

## Descripción

Este ejercicio aborda la problemática de invertir los dígitos de un número entero de 32 bits firmado. El objetivo es devolver el número con sus dígitos invertidos. Si al invertir el número este sale del rango permitido para un entero de 32 bits firmado, que es de [-2^31, 2^31 - 1], se debe retornar 0. Se asume que el entorno de ejecución no permite el uso de enteros de 64 bits (firmados o no firmados).

## Implementación

La implementación se lleva a cabo mediante una clase llamada `Solution` que incluye un método `reverse`. Este método toma un entero como argumento y devuelve el entero con sus dígitos invertidos, siempre que el resultado sea un entero válido dentro del rango de 32 bits. Aquí se utilizan técnicas como:

- Conversión de números a cadenas para manipular sus dígitos.
- Control de flujo para manejar signos negativos y asegurar que el resultado permanezca dentro de los límites válidos.

El código incluye un bloque de pruebas unitarias para validar la funcionalidad del método `reverse`.

## Uso

Para usar el método `reverse` de la clase `Solution`, primero se debe instanciar la clase y luego llamar al método con un número específico. Por ejemplo:

```python
solution = Solution()
result = solution.reverse(-123)
print(result)  # Output: -321
```

## Conclusión

El ejercicio "Reverse Integer" es una útil práctica para entender cómo manejar las operaciones con enteros y cadenas en Python, prestando especial atención a los límites y requerimientos de los tipos de datos en entornos de computación limitados. Asimismo, resalta la importancia de considerar los casos de borde en la implementación de algoritmos que involucran manipulación de números.
