# Solving Questions With Brainpower

## Descripción

El ejercicio "Solving Questions With Brainpower" plantea el problema de maximizar la puntuación obtenida en un examen compuesto por una serie de preguntas. Cada pregunta tiene una recompensa en puntos y un "coste de energía mental" que impide resolver un número determinado de preguntas posteriores si se decide resolverla. La secuencia de preguntas debe procesarse en orden, y para cada una se debe decidir si se resuelve o se omite. El objetivo es encontrar la estrategia óptima que proporcione la mayor cantidad posible de puntos al final del examen.

## Implementación

La implementación está desarrollada en Python dentro de una clase `Solution`, que contiene el método `mostPoints`. Este método aplica programación dinámica para evaluar todas las posibles decisiones (resolver o saltar) desde cada posición hacia el final, almacenando los resultados parciales para evitar cálculos repetidos.

## Detalles de la implementación

- **Estrategia de programación dinámica (DP):** Se utiliza un array `dp` donde `dp[i]` representa la máxima puntuación posible comenzando desde la pregunta `i`.
- **Recorrido inverso:** El algoritmo recorre las preguntas desde el final hacia el principio, calculando para cada una:
  - La puntuación total si se decide resolverla (`solve_points`), que incluye su puntuación más el mejor resultado desde la siguiente pregunta disponible tras aplicar el coste de brainpower.
  - La puntuación total si se decide omitirla (`skip_points`), equivalente a la mejor puntuación a partir de la siguiente pregunta.
- **Selección óptima:** En cada paso, se guarda en `dp[i]` la opción que brinda la mayor cantidad de puntos entre resolver y saltar.
- **Resultado final:** La solución corresponde a `dp[0]`, es decir, el valor óptimo calculado desde la primera pregunta.

## Uso

Para utilizar este código, se debe definir una lista de listas `questions`, donde cada sublista contiene dos enteros: los puntos obtenidos por resolver una pregunta y el número de preguntas siguientes que deben omitirse si se resuelve. Luego, se crea una instancia de la clase `Solution` y se llama al método `mostPoints` pasando dicha lista como argumento.

```python
if __name__ == "__main__":
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]

    sol = Solution()
    max_score = sol.mostPoints(questions)
    print(max_score)  # Output: 5
```

## Conclusión

El ejercicio "Solving Questions With Brainpower" es un ejemplo claro de cómo la programación dinámica puede aplicarse para tomar decisiones óptimas en problemas secuenciales con restricciones. El enfoque implementado es eficiente en tiempo y espacio, y permite evaluar grandes conjuntos de preguntas de manera eficaz. Esta técnica resulta útil no solo en problemas similares de optimización, sino también como base para resolver tareas más complejas en planificación, estrategias de juego y toma de decisiones condicionadas.
