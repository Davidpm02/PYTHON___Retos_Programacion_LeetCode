# Push Dominoes

## Descripción

El ejercicio **"Push Dominoes"** plantea un problema de simulación en el que se tiene una fila de dominós colocados verticalmente. Cada dominó puede ser empujado a la izquierda (`'L'`), a la derecha (`'R'`) o estar en equilibrio (`'.'`). El objetivo es determinar el estado final de la fila de dominós una vez que todas las fuerzas hayan surtido efecto.

Este problema modela un sistema físico simple con reglas claras de propagación de fuerzas, siendo especialmente útil para ejercitar habilidades de razonamiento algorítmico, simulación por pasos y manejo eficiente de estructuras lineales con restricciones de rendimiento.

## Implementación

La implementación está desarrollada en Python dentro de una clase `Solution`, que contiene el método `pushDominoes`. Este método toma como entrada una cadena que representa el estado inicial de los dominós y devuelve una nueva cadena con el estado final.

El enfoque adoptado en esta solución consiste en modelar las **fuerzas netas** aplicadas sobre cada posición de la fila. Para ello, se utilizan dos barridos sobre la cadena:

- Un primer barrido de izquierda a derecha para aplicar las fuerzas generadas por los dominós empujados hacia la derecha.
- Un segundo barrido de derecha a izquierda para aplicar las fuerzas generadas por los dominós empujados hacia la izquierda.

La combinación de ambas fuerzas (positiva hacia la derecha, negativa hacia la izquierda) determina la dirección final de cada dominó.

## Detalles de la implementación

- **Inicialización de fuerzas:** Se crea una lista `fuerza` con longitud igual a la cadena de entrada, que almacena la fuerza neta en cada índice.
- **Barrido izquierda a derecha:** Se simulan las fuerzas hacia la derecha. Un valor máximo (igual a `n`) se asigna al encontrar un `'R'`, disminuyendo gradualmente con la distancia.
- **Barrido derecha a izquierda:** Se simulan las fuerzas hacia la izquierda. Se repite el proceso anterior pero en sentido inverso, restando las fuerzas para obtener el valor neto.
- **Resultado final:** Se interpreta el valor neto de fuerza en cada posición:
  - Positivo: el dominó cae a la derecha (`'R'`).
  - Negativo: el dominó cae a la izquierda (`'L'`).
  - Cero: el dominó permanece en equilibrio (`'.'`).

## Uso

Para utilizar esta implementación, se debe crear una instancia de la clase `Solution` y llamar al método `pushDominoes`, pasando como argumento la cadena que representa el estado inicial de los dominós.

```python
if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."

    sol = Solution()
    final_state = sol.pushDominoes(dominoes)
    print(final_state)  # Output: "LL.RR.LLRRLL.."
```

## Conclusión

El ejercicio "Push Dominoes" ofrece una interesante combinación de simulación física y programación eficiente. La estrategia utilizada, basada en el análisis de fuerzas acumuladas en dos direcciones, permite resolver el problema en tiempo lineal, lo que es crucial dada la restricción de hasta 10⁵ dominós. Esta implementación es un ejemplo claro de cómo un modelo físico conceptual puede traducirse de manera elegante y eficiente a un algoritmo programático.
