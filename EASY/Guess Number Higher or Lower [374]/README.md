# Guess Number Higher or Lower

## Descripción

El ejercicio "Guess Number Higher or Lower" consiste en adivinar un número seleccionado entre 1 y n. Después de cada intento de adivinanza, se proporciona una pista indicando si el número a adivinar es mayor, menor o igual al número que has intentado. Para esto, se utiliza una API predefinida llamada guess(), que devuelve uno de los siguientes valores:

* -1: Si el número que has adivinado es mayor que el número seleccionado.
* 1: Si el número que has adivinado es menor que el número seleccionado.
* 0: Si has acertado el número.

El objetivo es implementar una función que adivine el número correcto utilizando estas pistas.

## Implementación

La implementación de este problema utiliza una búsqueda binaria para optimizar el proceso de adivinanza. Al reducir el rango de búsqueda a la mitad en cada iteración, se logra una eficiencia considerable en cuanto al número de intentos necesarios.

### Detalles de la implementación

* Lista de posibles números: Se genera una lista de posibles números desde 1 hasta n.
* Selección del número intermedio: En cada paso, se selecciona el número intermedio de la lista para realizar la adivinanza.
* Uso de la API guess(): Basado en el resultado de la llamada a guess(), se ajusta el rango de posibles números:

  * Si la API devuelve 0, se ha adivinado el número y el programa retorna el valor.
  * Si la API devuelve 1, el número seleccionado es menor, por lo que se ajusta el rango a la mitad superior de los números posibles.
  * Si la API devuelve -1, el número seleccionado es mayor, por lo que se ajusta el rango a la mitad inferior de los números posibles.

* Búsqueda binaria: Este proceso se repite hasta que se adivine el número correcto.

## Uso

Para utilizar esta implementación en un entorno de desarrollo, se puede seguir el siguiente ejemplo:

* Define un valor de n (el límite superior del rango de números) y un número a adivinar.
* Crea una instancia de la clase Solution y llama al método guessNumber(n).
* La función retornará el número correcto basándose en las pistas proporcionadas por la API guess().

```python
if __name__ == "__main__":
    # Suponiendo que la función guess() está correctamente implementada y configurada
    n = 10
    sol = Solution()
    print(sol.guessNumber(n))  # Output: El número correcto basado en las pistas
```

## Conclusión

El ejercicio "Guess Number Higher or Lower" es un buen ejemplo de cómo utilizar la técnica de búsqueda binaria para resolver problemas de adivinanza de manera eficiente. La implementación reduce el espacio de búsqueda en cada iteración, logrando un algoritmo con complejidad O(log n). Esto asegura un tiempo de ejecución óptimo incluso para rangos grandes, cumpliendo con las restricciones del problema.
