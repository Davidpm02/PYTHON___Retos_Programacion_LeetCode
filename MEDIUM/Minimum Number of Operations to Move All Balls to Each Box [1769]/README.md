# Minimum Number of Operations to Move All Balls to Each Box

## Descripción

El ejercicio "Minimum Number of Operations to Move All Balls to Each Box" tiene como objetivo calcular el número mínimo de operaciones requeridas para mover todas las bolas en un conjunto de cajas (`boxes`) hacia cada una de las posiciones posibles. Dada una cadena binaria, donde `1` representa una caja con una bola y `0` una caja vacía, el problema evalúa cuántos movimientos se necesitan considerando que solo se pueden mover bolas a cajas adyacentes.

## Implementación

La solución utiliza un enfoque que evalúa para cada caja la cantidad de operaciones necesarias para mover todas las bolas hacia esa posición específica. Esto se realiza recorriendo cada posición en la cadena y calculando la distancia entre las bolas (`1`) y la caja objetivo.

### Detalles de la implementación

1. **Iteración sobre todas las posiciones:**
   - La solución calcula las operaciones requeridas para cada posición de la cadena `boxes`.

2. **Cálculo de movimientos necesarios:**
   - Se calcula la distancia absoluta entre la posición de cada bola y la caja objetivo.
   - Si una caja no contiene una bola (`0`), no contribuye a la cuenta de movimientos.

3. **Acumulación de resultados:**
   - Se utiliza una lista para almacenar el número total de movimientos requeridos para cada posición.

### Complejidad

El enfoque tiene una complejidad de \(O(n^2)\) debido al doble recorrido: un recorrido sobre las cajas y otro sobre las posiciones relevantes en cada iteración. Este enfoque es eficiente para valores moderados de \(n\) y respeta los límites del problema.

## Uso

Para utilizar este código, define una cadena binaria que representa las cajas con bolas y llama al método `minOperations` con esta cadena como parámetro.

```python
if __name__ == "__main__":
    boxes = "110"

    sol = Solution()
    result = sol.minOperations(boxes)
    print(result)  # Output: [1, 1, 3]
```

## Conclusión

El ejercicio "Minimum Number of Operations to Move All Balls to Each Box" aborda de manera eficiente el cálculo de movimientos en escenarios donde las operaciones dependen de posiciones relativas. Este problema tiene aplicaciones prácticas en simulaciones, optimización y distribución de recursos. La solución presentada aprovecha técnicas fundamentales de programación, como la iteración y el cálculo de distancias, para generar una implementación directa y funcional, adecuada para un rango amplio de datos.
