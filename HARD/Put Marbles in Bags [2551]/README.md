# Put Marbles in Bags

## Descripción

El ejercicio "Put Marbles in Bags" plantea el desafío de distribuir una secuencia de mármoles, cada uno con un peso determinado, en `k` bolsas, cumpliendo con ciertas reglas de agrupamiento. Cada bolsa debe contener un subgrupo continuo de mármoles, sin dejar ninguna vacía. El coste de una bolsa se calcula como la suma del peso del primer y último mármol en ella. La puntuación total es la suma de los costes de todas las bolsas. El objetivo final es determinar la **diferencia** entre la puntuación máxima y mínima que se puede obtener al distribuir los mármoles en las `k` bolsas.

## Implementación

La implementación está escrita en Python mediante una clase `Solution`, que contiene el método `putMarbles`. Este método analiza todas las posibles divisiones entre pares consecutivos de mármoles y calcula los cortes que maximizarían o minimizarían la puntuación total, eligiendo los `k-1` cortes más altos o más bajos respectivamente.

## Detalles de la implementación

- **Cálculo de pares adyacentes:** Se construye una lista con la suma de pesos de cada par de mármoles adyacentes. Esta lista representa los posibles puntos de corte entre las bolsas.
- **Ordenación de cortes:** Se ordenan los valores obtenidos de los pares adyacentes para facilitar la selección de los cortes más baratos y más costosos.
- **Selección de cortes:**
  - Para minimizar la puntuación total, se toman los `k-1` pares con menor coste.
  - Para maximizarla, se seleccionan los `k-1` pares con mayor coste.
- **Resultado final:** Se devuelve la diferencia entre la puntuación máxima y mínima obtenidas con las respectivas selecciones.

## Uso

Para utilizar este código, se debe proporcionar un arreglo con los pesos de los mármoles y un número entero `k` indicando en cuántas bolsas se deben distribuir. Luego, se instancia la clase `Solution` y se llama al método `putMarbles`, el cual devuelve un entero con la diferencia entre la mejor y la peor puntuación posible.

```python
if __name__ == "__main__":
    weights = [1, 3, 5, 1]
    k = 2

    sol = Solution()
    result = sol.putMarbles(weights, k)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Put Marbles in Bags" es una excelente práctica para trabajar con problemas de optimización y divisiones de secuencias. La solución implementada hace un uso eficiente de estructuras básicas como listas y operaciones de ordenación para resolver el problema en tiempo lineal o logarítmico relativo al número de mármoles. Además, introduce una forma elegante de interpretar particiones y cortes en listas consecutivas, lo que resulta aplicable en numerosos escenarios reales de segmentación de datos y distribución óptima de recursos.
