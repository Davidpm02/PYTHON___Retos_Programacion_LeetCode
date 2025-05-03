# Minimum Domino Rotations For Equal Row

## Descripción

El ejercicio **"Minimum Domino Rotations For Equal Row"** consiste en encontrar el número mínimo de rotaciones necesarias para que todos los valores en la fila superior (`tops`) sean iguales o todos los valores en la fila inferior (`bottoms`) sean iguales. Dado un conjunto de dominós representado por dos listas, `tops` y `bottoms`, donde cada lista contiene los valores de la mitad superior e inferior de cada dominó, la tarea es determinar la cantidad mínima de rotaciones necesarias para lograr la uniformidad en alguna de las filas.

Si no es posible lograr que todos los valores en una fila sean iguales, se debe devolver `-1`.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `minDominoRotations`. Este método recibe dos listas de enteros (`tops` y `bottoms`), representando las filas superior e inferior de los dominós, respectivamente, y devuelve el número mínimo de rotaciones requeridas para hacer que todos los valores en una de las filas sean iguales.

### Detalles de la implementación

- **Función `check_rotations(target)`**: Esta función intenta hacer que todos los valores en la fila superior o inferior sean iguales al valor `target`. La función recorre todas las posiciones de las listas `tops` y `bottoms`, contabilizando las rotaciones necesarias y verificando si es posible lograr la uniformidad con el valor `target`.
- **Comparación de valores**: Se prueba primero con el valor del primer dominó en la fila superior (`tops[0]`), y luego se realiza el mismo proceso con el valor del primer dominó en la fila inferior (`bottoms[0]`) si es diferente. Si no es posible hacer que todas las posiciones en alguna de las filas tengan el mismo valor, se devuelve `-1`.
- **Resultado final**: El método devuelve el número mínimo de rotaciones necesarias, ya sea en la fila superior o en la fila inferior.

## Uso

Para utilizar este código, basta con definir las listas `tops` y `bottoms`, y luego crear una instancia de la clase `Solution`. Después, se llama al método `minDominoRotations` con las listas y se obtiene el número mínimo de rotaciones necesarias.

```python
if __name__ == "__main__":
    tops = [2, 1, 2, 4, 2, 2]
    bottoms = [5, 2, 6, 2, 3, 2]

    sol = Solution()
    rotations = sol.minDominoRotations(tops, bottoms)
    print(rotations)  # Output: 2
```

## Conclusión

El ejercicio "Minimum Domino Rotations For Equal Row" es una excelente forma de practicar la implementación de soluciones algorítmicas para problemas de optimización en secuencias. La implementación utilizada es eficiente y permite resolver el problema en tiempo lineal respecto al número de dominós, lo que es crucial dado que las restricciones pueden alcanzar tamaños grandes (hasta 20,000 dominós). La solución demuestra cómo combinar la búsqueda en diferentes posibles objetivos (filas uniformes) y aplicar rotaciones de manera eficiente, lo cual refuerza conceptos de programación y análisis de complejidad.
