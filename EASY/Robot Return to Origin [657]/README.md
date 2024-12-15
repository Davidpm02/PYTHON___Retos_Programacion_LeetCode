# Robot Return to Origin

## Descripción

El ejercicio "Robot Return to Origin" consiste en analizar una secuencia de movimientos de un robot que comienza en la posición (0, 0) de un plano 2D. El objetivo es determinar si el robot vuelve a la posición de inicio después de realizar todos los movimientos indicados en la secuencia.

La secuencia de movimientos es una cadena de caracteres, donde cada carácter representa un movimiento del robot en alguna de las cuatro direcciones posibles: 'R' (derecha), 'L' (izquierda), 'U' (arriba), 'D' (abajo). La tarea es evaluar si, al final de la secuencia, las coordenadas del robot son (0, 0), es decir, si el robot regresa a su punto de partida.

## Implementación

La implementación se realiza en Python mediante una clase `Solution`, que contiene el método `judgeCircle`. Este método toma como parámetro una cadena `moves`, que representa los movimientos del robot, y devuelve un valor booleano (`True` o `False`) indicando si el robot regresa a la posición de origen.

## Detalles de la implementación

- **Inicialización de coordenadas:** El robot comienza en la posición (0, 0), que es representada por un par de coordenadas [0, 0].
- **Recorrido de la secuencia de movimientos:** Cada carácter de la cadena se procesa y se utiliza para actualizar las coordenadas del robot. Los movimientos son los siguientes:
  - 'U' (up): Aumenta la coordenada y.
  - 'D' (down): Disminuye la coordenada y.
  - 'L' (left): Disminuye la coordenada x.
  - 'R' (right): Aumenta la coordenada x.
- **Comprobación del resultado final:** Después de procesar todos los movimientos, se verifica si las coordenadas finales son [0, 0]. Si lo son, el robot ha regresado al origen y se devuelve `True`; de lo contrario, se devuelve `False`.

## Uso

Para utilizar este código, simplemente se debe pasar una cadena de movimientos `moves` a la función `judgeCircle` de la clase `Solution`, y esta devolverá si el robot regresa al origen.

```python
if __name__ == "__main__":
    moves = "UD"
    sol = Solution()
    result = sol.judgeCircle(moves)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Robot Return to Origin" es una manera sencilla pero eficaz de practicar el manejo de secuencias de movimientos en un plano 2D y trabajar con coordenadas. El enfoque implementado es directo, utilizando una lista para mantener el seguimiento de la posición del robot y una estructura simple de control de flujo para evaluar si el robot regresa al origen. Este ejercicio refuerza conceptos de manipulación de cadenas y control de estado, que son útiles en una variedad de problemas en programación y análisis de movimientos o simulaciones espaciales.
