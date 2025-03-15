# House Robber IV

## Descripción

El ejercicio "House Robber IV" trata sobre un ladrón que quiere robar dinero de varias casas dispuestas en una calle. Cada casa tiene cierta cantidad de dinero y el ladrón no puede robar casas adyacentes. El objetivo es determinar la mínima capacidad del ladrón para robar al menos `k` casas de entre todas las combinaciones posibles.

Se nos proporciona un arreglo de enteros `nums`, donde cada elemento representa la cantidad de dinero guardado en una casa, y un entero `k` que indica la cantidad mínima de casas que el ladrón debe robar. El reto consiste en calcular la mínima capacidad del ladrón que permita robar al menos `k` casas sin robar casas adyacentes.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `minCapability`. Este método usa una búsqueda binaria para encontrar la mínima capacidad que permita robar al menos `k` casas, siguiendo estos pasos:

- **Función `can_steal(capability)`:** Esta función verifica si es posible robar al menos `k` casas con una capacidad dada. Recorre las casas y, si la cantidad de dinero en una casa es menor o igual a la capacidad actual, el ladrón puede robarla y salta a la siguiente casa no adyacente.
- **Búsqueda binaria:** El algoritmo emplea una búsqueda binaria para encontrar la capacidad mínima que satisface la condición de robar al menos `k` casas.

## Uso

Para utilizar este código, simplemente se debe definir el arreglo `nums` que representa la cantidad de dinero en cada casa y el valor `k` que indica el número mínimo de casas que se deben robar. Luego, se crea una instancia de la clase `Solution` y se llama al método `minCapability` para obtener el resultado.

```python
if __name__ == "__main__":
    nums = [2, 3, 5, 9]
    k = 2

    sol = Solution()
    result = sol.minCapability(nums, k)
    print(result)  # Output: 5
```

## Conclusión

El ejercicio "House Robber IV" ofrece una forma interesante de aplicar la búsqueda binaria para resolver problemas de optimización. A través de la combinación de una búsqueda binaria y un enfoque greedy para robar casas, se puede encontrar de manera eficiente la capacidad mínima necesaria para robar al menos k casas sin violar la regla de no robar casas adyacentes. Este tipo de problemas son comunes en escenarios de programación competitiva y entrevistas técnicas, y este enfoque optimizado permite manejar grandes entradas de datos dentro de los límites del problema.
