# Candy

## Descripción

El ejercicio **"Candy"** plantea el reto de seleccionar `p` pares de índices en una lista de enteros `nums`, de manera que se minimice la *diferencia máxima* entre los elementos de cada par seleccionado. Cada índice debe usarse una sola vez. El objetivo es garantizar que, entre todas las diferencias absolutas de los `p` pares elegidos, la más grande sea lo menor posible.

Este problema es representativo de técnicas de optimización combinatoria y es especialmente útil para entrenar habilidades como la búsqueda binaria en el espacio de soluciones, la toma de decisiones bajo restricciones y la optimización por emparejamiento de elementos cercanos.

## Implementación

La solución está desarrollada en Python dentro de una clase `Solution`, que implementa el método `minimizeMax`. Este método sigue los siguientes pasos clave:

- **Ordenación del array:** Para facilitar la comparación de elementos cercanos y emparejar valores que puedan minimizar la diferencia.
- **Búsqueda binaria:** Se aplica sobre el espacio de diferencias posibles, con el objetivo de encontrar la menor diferencia máxima válida.
- **Función auxiliar `can_form_pairs`:** Esta función comprueba si es posible formar al menos `p` pares cumpliendo que la diferencia entre los elementos de cada par no supere un umbral dado (`max_diff`). Se aplica una estrategia greedy para maximizar la cantidad de pares válidos.

### Detalles de la implementación

- **Ordenación previa:** Permite recorrer los elementos adyacentes buscando diferencias mínimas.
- **Emparejamiento greedy:** Se recorren los elementos consecutivamente. Si dos consecutivos cumplen la condición, se toman como par y se avanza dos posiciones.
- **Control binario del umbral de diferencia:** Se ajusta el límite superior e inferior de forma iterativa, buscando el mínimo valor de diferencia que aún permita formar `p` pares.

## Uso

Para utilizar este código, basta con definir la lista de enteros `nums` y el número de pares `p` a formar. Luego, se crea una instancia de la clase `Solution` y se llama al método `minimizeMax` con los parámetros adecuados.

```python
if __name__ == "__main__":
    nums = [10, 1, 2, 7, 1, 3]
    p = 2

    sol = Solution()
    result = sol.minimizeMax(nums, p)
    print(result)  # Output: 1
```

## Conclusión

El ejercicio "Candy" representa un ejemplo eficaz de cómo aplicar técnicas de optimización combinadas con búsqueda binaria en problemas complejos de selección de subconjuntos bajo restricciones. Esta implementación demuestra cómo estructurar soluciones eficientes en problemas de gran escala (hasta 10⁵ elementos), al aprovechar ordenación previa y estrategias greedy junto con búsqueda binaria para reducir la complejidad del espacio de búsqueda. Además, refuerza conceptos clave como la diferencia absoluta, el emparejamiento eficiente y el uso práctico de funciones auxiliares para validar hipótesis en tiempo logarítmico.
