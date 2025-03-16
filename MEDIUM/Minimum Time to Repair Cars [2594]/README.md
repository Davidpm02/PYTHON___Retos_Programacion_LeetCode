# Minimum Time to Repair Cars

## Descripcion

El ejercicio "Minimum Time to Repair Cars" consiste en determinar el tiempo mínimo necesario para reparar un número dado de coches, utilizando un conjunto de mecánicos con distintos rangos de eficiencia. Cada mecánico tiene un "rango" que determina el tiempo necesario para reparar un coche, según la fórmula:

\[ \text{Tiempo} = r \times n^2 \]

donde \( r \) es el rango del mecánico y \( n \) es el número de coches que repara.

El objetivo es encontrar el tiempo mínimo en el que todos los coches puedan ser reparados simultáneamente por los mecánicos disponibles.

## Implementacion

La solución se implementa en Python utilizando una clase `Solution` que contiene el método `repairCars`. Este método emplea una búsqueda binaria sobre el tiempo para determinar la cantidad mínima de minutos necesarios para completar la reparación de todos los coches.

### Detalles de la implementación

- **Función auxiliar `canRepairInTime(time)`:** Evalúa si es posible reparar todos los coches dentro de un tiempo dado.
- **Búsqueda binaria:** Se realiza sobre el rango de tiempos posibles, ajustando el límite superior e inferior hasta encontrar el tiempo óptimo.
- **Cálculo de coches reparados:** Se utiliza la ecuación cuadrática \( x^2 \leq \frac{time}{r} \) para determinar cuántos coches puede reparar cada mecánico en un tiempo dado.

## Uso

Para utilizar este código, se debe definir la lista de rangos de los mecánicos y el número total de coches a reparar. Luego, se crea una instancia de la clase `Solution` y se llama al método `repairCars`.

```python
if __name__ == "__main__":
    ranks = [4, 2, 3, 1]
    cars = 10

    sol = Solution()
    min_time = sol.repairCars(ranks, cars)
    print(min_time)  # Output esperado: 16
```

## Conclusion

El ejercicio "Minimum Time to Repair Cars" aborda un problema de optimización en el que se busca minimizar el tiempo total de reparación de coches mediante la distribución eficiente del trabajo entre mecánicos con distintos niveles de habilidad. La solución implementada hace uso de una estrategia de búsqueda binaria, permitiendo encontrar la solución óptima de manera eficiente incluso para grandes cantidades de coches y mecánicos. Esta técnica resulta particularmente útil en problemas donde se debe encontrar un límite mínimo o máximo dentro de un conjunto ordenado de soluciones posibles.
