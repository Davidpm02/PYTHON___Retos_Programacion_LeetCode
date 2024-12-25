# Largest Number At Least Twice of Others

## Descripción

El ejercicio "Largest Number At Least Twice of Others" busca determinar si el número más grande en un array de enteros es al menos el doble de cada uno de los otros números en el array. Si esta condición se cumple, el programa debe devolver el índice del número más grande. En caso contrario, devuelve \(-1\).

Por ejemplo:

- Para un array como \([3,6,1,0]\), el resultado sería \(1\), ya que el \(6\) (en la posición 1) es al menos el doble de los demás números.
- Para el array \([1,2,3,4]\), el resultado es \(-1\), ya que ningún número cumple la condición.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con el método `dominantIndex`. Este método sigue los siguientes pasos:

1. Identifica el número más grande en el array utilizando la función `max`.
2. Elimina el número más grande del array para evaluar la relación de este con los demás números.
3. Comprueba si el número más grande es al menos el doble que todos los números restantes.
4. Retorna el índice del número más grande si la condición se cumple, o \(-1\) en caso contrario.

### Detalles de la implementación

- **Manejo del mayor número:** El número más grande se identifica y se elimina temporalmente para analizar los números restantes.
- **Relación de magnitudes:** La evaluación se realiza utilizando divisiones para verificar que el mayor número sea al menos dos veces más grande que los demás.
- **Indice del mayor número:** Se utiliza la lista original para determinar la posición del mayor número.

## Uso

Para utilizar este código, simplemente crea una instancia de la clase Solution y llama al método dominantIndex con el array de enteros deseado como argumento. Esto devolverá el índice del mayor número si cumple la condición, o −1−1 en caso contrario.

```python
if __name__ == "__main__":
    sol = Solution()
    result = sol.dominantIndex([3,6,1,0])
    print(result)  # Output: 1
```

## Conclusión

El ejercicio "Largest Number At Least Twice of Others" es una excelente manera de aplicar conceptos básicos de manejo de listas y control de flujo en Python. La implementación presentada optimiza el procesamiento al evaluar sólo los elementos necesarios y garantizar que las comparaciones se realicen de manera eficiente. Esta tarea fortalece habilidades en manejo de listas, operaciones condicionales y uso de funciones integradas.
