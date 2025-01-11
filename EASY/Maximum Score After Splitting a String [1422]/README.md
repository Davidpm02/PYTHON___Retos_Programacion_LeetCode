# Maximum Score After Splitting a String

## Descripción

El ejercicio "Maximum Score After Splitting a String" tiene como objetivo encontrar la puntuación máxima que se puede obtener al dividir una cadena binaria `s` en dos subcadenas no vacías. La puntuación se calcula sumando el número de ceros en la subcadena izquierda y el número de unos en la subcadena derecha.

Este problema es útil para comprender operaciones en cadenas, optimización de soluciones iterativas y conceptos relacionados con el manejo de subcadenas.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `maxScore`. Este método evalúa todas las posibles formas de dividir la cadena `s`, calcula las puntuaciones correspondientes y devuelve la puntuación máxima obtenida.

### Detalles de la implementación

1. **Iteración:**
   - El método recorre todos los posibles puntos de división dentro de la cadena, excluyendo los extremos (para asegurar que las subcadenas no estén vacías).

2. **Cálculo de la Puntuación:**
   - Para cada división, se calcula:
     - La cantidad de ceros en la subcadena izquierda utilizando el método `count`.
     - La cantidad de unos en la subcadena derecha también utilizando `count`.
   - Se suma el número de ceros y unos para obtener la puntuación total para esa división.

3. **Evaluación de Máximo:**
   - Se almacena cada puntuación en una lista.
   - Al final, se devuelve la puntuación máxima de la lista.

## Uso

Para utilizar este código, crea una instancia de la clase `Solution` y llama al método `maxScore`, proporcionando la cadena binaria `s` como argumento.

```python
if __name__ == "__main__":
    s = "011101"

    sol = Solution()
    result = sol.maxScore(s)
    print(result)  # Output: 5
```

## Conclusión

El ejercicio "Maximum Score After Splitting a String" es una excelente práctica para aprender a dividir cadenas y realizar cálculos basados en el contenido de subcadenas. La implementación presentada es simple y eficiente, recorriendo la cadena una vez para evaluar todas las divisiones posibles. Este enfoque refuerza habilidades de manipulación de cadenas y optimización de bucles, fundamentales en programación y resolución de problemas.
