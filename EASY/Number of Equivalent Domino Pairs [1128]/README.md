# Number of Equivalent Domino Pairs

## Descripción

El ejercicio "Number of Equivalent Domino Pairs" tiene como objetivo encontrar cuántos pares de fichas de dominó son equivalentes dentro de una lista. Dos fichas se consideran equivalentes si contienen los mismos números, independientemente del orden (es decir, se pueden rotar para ser iguales). Este problema es una buena oportunidad para trabajar con estructuras de datos eficientes y entender el concepto de normalización de datos para facilitar comparaciones.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `numEquivDominoPairs`. Este método recorre todas las fichas, las normaliza ordenando sus valores, y utiliza un diccionario para contar cuántas veces aparece cada combinación. A partir de estas frecuencias, calcula el número total de pares equivalentes.

## Detalles de la implementación

- **Normalización de las fichas:** Cada ficha se transforma en una tupla ordenada `(min(a,b), max(a,b))` para que las fichas [1,2] y [2,1] se consideren iguales.
- **Uso de `defaultdict`:** Se utiliza `collections.defaultdict(int)` para llevar un recuento de la frecuencia de cada ficha normalizada sin necesidad de inicializar las claves manualmente.
- **Cálculo del número de pares:** Por cada ficha encontrada, se suma al resultado el número de veces que ya ha aparecido esa ficha. Esto se debe a que cada nueva aparición forma un nuevo par con todas las apariciones anteriores.

## Uso

Para utilizar este código, simplemente se debe definir una lista de fichas de dominó y crear una instancia de la clase `Solution`. Luego, se llama al método `numEquivDominoPairs` con la lista de fichas para obtener el número total de pares equivalentes.

```python
if __name__ == "__main__":
    dominoes = [[1,2],[2,1],[3,4],[5,6]]

    sol = Solution()
    num_pairs = sol.numEquivDominoPairs(dominoes)
    print(num_pairs)  # Output: 1
```

## Conclusión

El ejercicio "Number of Equivalent Domino Pairs" pone en práctica técnicas útiles como la normalización de datos para evitar comparaciones redundantes y el uso eficiente de estructuras como diccionarios para contar frecuencias. Este enfoque permite resolver el problema con una complejidad lineal, lo cual es esencial dada la posible longitud del array de entrada. Además, ayuda a desarrollar habilidades clave en la manipulación de colecciones y optimización de código en Python.
