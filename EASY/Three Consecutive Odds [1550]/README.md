# Three Consecutive Odds

## Descripción

El ejercicio **"Three Consecutive Odds"** consiste en determinar si, dentro de un array de enteros, existen **tres números impares consecutivos**. Esta tarea es relevante cuando se requiere analizar patrones de secuencias en datos numéricos, ya sea en contextos matemáticos, de análisis de datos o de validaciones de reglas en estructuras secuenciales.

## Implementación

La solución se ha implementado en Python mediante una clase `Solution`, que contiene el método `threeConsecutiveOdds`. Este método recorre el array de entrada y mantiene un contador que se incrementa al detectar un número impar. Si se alcanzan tres números impares consecutivos, se retorna `True`. En caso contrario, se continúa la iteración hasta el final del array, devolviendo `False` si no se cumple la condición.

## Detalles de la implementación

- **Contador de impares consecutivos:** Se utiliza una variable `consecutive_odds` para llevar la cuenta de cuántos números impares consecutivos se han encontrado.
- **Control del índice:** Se utiliza una variable `last_odd_index` para asegurarse de que los números impares consecutivos realmente lo son (es decir, están uno a continuación del otro).
- **Reinicio del contador:** Si se encuentra un número par, el contador de impares consecutivos se reinicia, ya que se ha roto la secuencia.
- **Condición de corte:** Si en algún punto se alcanzan tres impares consecutivos, se retorna inmediatamente `True` para optimizar el rendimiento del algoritmo.

## Uso

Para utilizar este código, basta con definir el array de entrada y crear una instancia de la clase `Solution`. A continuación, se llama al método `threeConsecutiveOdds` pasando como argumento dicho array. El método retornará un valor booleano indicando si se ha encontrado o no una secuencia de tres impares consecutivos.

```python
if __name__ == "__main__":
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]

    sol = Solution()
    result = sol.threeConsecutiveOdds(arr)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Three Consecutive Odds" proporciona una manera eficiente de verificar la existencia de un patrón específico dentro de una lista de números enteros. La implementación presentada aprovecha estructuras de control simples y claras para mantener la lógica fácilmente comprensible y escalable. Esta solución es particularmente útil como práctica para el manejo de listas, condiciones de control y lógica secuencial en Python, y puede adaptarse fácilmente a otros tipos de patrones o condiciones numéricas.
