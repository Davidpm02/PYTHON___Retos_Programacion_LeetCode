# Maximum Difference Between Adjacent Elements in a Circular Array

## Descripción

El ejercicio "Maximum Difference Between Adjacent Elements in a Circular Array" consiste en encontrar la mayor diferencia absoluta entre elementos adyacentes en un array circular. A diferencia de un array lineal, en un array circular el primer y el último elemento también se consideran adyacentes. Este tipo de problema es común en estructuras de datos circulares, donde es fundamental tener en cuenta la continuidad entre extremos para evitar errores lógicos.

## Implementación

La solución está desarrollada en Python dentro de una clase `Solution`, que incluye el método `maxAdjacentDistance`. Este método toma como entrada una lista de enteros `nums` y retorna un valor entero que representa la mayor diferencia absoluta entre elementos adyacentes, considerando el comportamiento circular del array.

## Detalles de la implementación

- **Inicialización de resultados:** Se comienza evaluando la diferencia absoluta entre el primer y el último elemento, ya que forman una pareja adyacente en un array circular.
- **Recorrido lineal:** Se recorre el array evaluando cada par de elementos consecutivos, es decir, `nums[i]` y `nums[i + 1]`, y se calcula su diferencia absoluta.
- **Almacenamiento de diferencias:** Cada diferencia se guarda en una lista auxiliar.
- **Resultado final:** Se devuelve el valor máximo de las diferencias calculadas, representando la mayor diferencia entre elementos adyacentes.

## Uso

Para utilizar este código, simplemente se debe definir el array circular de enteros, crear una instancia de la clase `Solution` y llamar al método `maxAdjacentDistance` con dicho array como argumento.

```python
if __name__ == "__main__":
    nums = [1, 2, 4]

    sol = Solution()
    max_diff = sol.maxAdjacentDistance(nums)
    print(max_diff)  # Output: 3
```

## Conclusión

El ejercicio "Maximum Difference Between Adjacent Elements in a Circular Array" destaca por su enfoque en el tratamiento de arrays circulares, un concepto esencial en la programación de estructuras como buffers o listas enlazadas circulares. La solución implementada es clara, eficiente y adaptable a diferentes tamaños de array. Además, refuerza el entendimiento de operaciones con índices y el manejo de diferencias absolutas en estructuras circulares, habilidades útiles en problemas algorítmicos y de optimización.
