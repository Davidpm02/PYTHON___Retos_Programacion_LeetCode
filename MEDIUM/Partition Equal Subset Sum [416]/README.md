# Partition Equal Subset Sum

## Descripción

El ejercicio **"Partition Equal Subset Sum"** plantea el reto de determinar si es posible dividir un array de enteros positivos en dos subconjuntos con la misma suma total. Este problema pertenece a la familia de problemas de partición y es especialmente importante en el estudio de algoritmos de programación dinámica, ya que requiere identificar subconjuntos que cumplan condiciones específicas de suma.

El problema tiene aplicaciones prácticas en el ámbito de la optimización, diseño de sistemas de balanceo de carga y segmentación de recursos de forma equitativa.

## Implementación

La solución está implementada en Python dentro de una clase llamada `Solution`, que incluye el método `canPartition`. Este método devuelve un valor booleano indicando si es posible realizar la partición del array en dos subconjuntos con igual suma.

## Detalles de la implementación

- **Verificación de paridad:** Se calcula la suma total de los elementos del array. Si esta suma es impar, es imposible dividirla en dos partes iguales, por lo que se retorna `False` inmediatamente.

- **Transformación a un problema de suma de subconjuntos:** Si la suma es par, se define como objetivo (`target`) la mitad de la suma total. El problema se convierte entonces en verificar si existe un subconjunto cuya suma sea igual al objetivo.

- **Programación dinámica con lista booleana:** Se utiliza una lista `dp` de tamaño `target + 1`, donde `dp[i]` indica si es posible formar la suma `i` con los elementos disponibles. Se inicializa `dp[0]` como `True`, ya que siempre es posible formar la suma cero sin utilizar ningún elemento.

- **Actualización de la tabla DP:** Para cada número en el array, se recorre la tabla DP en orden descendente para evitar reutilizar un mismo número en múltiples combinaciones. Si `dp[i - num]` es `True`, entonces `dp[i]` también puede ser `True`, indicando que se puede alcanzar esa suma incluyendo el número actual.

- **Resultado final:** El valor en `dp[target]` indica si es posible formar un subconjunto cuya suma sea exactamente la mitad del total, lo cual implica que el array puede ser particionado en dos subconjuntos de suma igual.

## Uso

Para utilizar esta implementación, basta con crear una instancia de la clase `Solution` y llamar al método `canPartition`, pasando como argumento un array de enteros positivos.

```python
if __name__ == "__main__":
    nums = [1, 5, 11, 5]

    sol = Solution()
    is_partitionable = sol.canPartition(nums)
    print(is_partitionable)  # Output: True
```

## Conclusión

El ejercicio "Partition Equal Subset Sum" es un claro ejemplo de cómo aplicar programación dinámica para resolver problemas de partición y suma de subconjuntos. El enfoque implementado es eficiente y escalable, permitiendo determinar en tiempo razonable si una partición equitativa es posible incluso en arrays con varios elementos. Este tipo de problemas refuerza habilidades fundamentales para la resolución de desafíos de optimización en estructuras de datos y algoritmos.
