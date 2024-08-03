# Sqrt(x)

## Descripción

El ejercicio "Sqrt(x)" consiste en encontrar la raíz cuadrada de un número entero no negativo `x` y devolver la parte entera de la raíz cuadrada. El valor devuelto debe ser también un número entero no negativo. No se permite el uso de funciones o operadores de exponenciación integrados como `pow(x, 0.5)` o `x ** 0.5`.

**Ejemplos:**

1. **Input:** x = 4  
   **Output:** 2  
   **Explicación:** La raíz cuadrada de 4 es 2, por lo que se devuelve 2.

2. **Input:** x = 8  
   **Output:** 2  
   **Explicación:** La raíz cuadrada de 8 es aproximadamente 2.82842..., y al redondear hacia abajo al entero más cercano, se devuelve 2.

**Restricciones:**

- 0 <= x <= 2³¹ - 1

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `mySqrt`. Este método calcula la raíz cuadrada de un entero utilizando un enfoque basado en la resta consecutiva de números impares, que es una técnica alternativa para evitar el uso de funciones de exponenciación.

### Detalles de la implementación

- **Resta de números impares:** Se utiliza un bucle para restar números impares consecutivos de `x` hasta que `x` se vuelve menor que el siguiente número impar. El número de iteraciones proporciona la parte entera de la raíz cuadrada.

## Uso

Para utilizar este código, simplemente se debe definir el valor x. Luego, se crea una instancia de la clase Solution y se llama al método mySqrt con el valor x. El método devolverá la parte entera de la raíz cuadrada de x.

```python
if __name__ == "__main__":
    x = 8

    sol = Solution()
    sqrt_x = sol.mySqrt(x)
    print(sqrt_x)  # Output: 2
```

## Conclusión

El ejercicio "Sqrt(x)" proporciona una manera eficiente de calcular la parte entera de la raíz cuadrada de un número entero sin utilizar funciones de exponenciación integradas. La implementación basada en la resta de números impares es simple y efectiva, permitiendo obtener el resultado deseado con una complejidad temporal razonable. Este enfoque es útil en contextos donde no se permite el uso de funciones matemáticas avanzadas y se busca una solución directa y comprensible.
