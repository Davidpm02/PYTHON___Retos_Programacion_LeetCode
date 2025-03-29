# Apply Operations to Maximize Score

## Descripción

El ejercicio **"Apply Operations to Maximize Score"** consiste en maximizar una puntuación inicial de 1 aplicando una operación en un array de enteros llamado `nums`. La operación consiste en elegir subarreglos de `nums` y multiplicar la puntuación por el valor máximo de un elemento en el subarreglo con el mayor número de factores primos distintos. Esta operación se puede realizar un máximo de `k` veces. El reto es encontrar la puntuación máxima posible tras realizar las operaciones y devolverla módulo \(10^9 + 7\).

### Definición de la operación

1. Se elige un subarreglo no vacío de `nums[l, ..., r]`.
2. Se escoge el elemento `x` con el mayor puntaje primo de dicho subarreglo.
3. Se multiplica la puntuación por `x`.

El puntaje primo de un número es la cantidad de factores primos distintos que tiene. Por ejemplo, el puntaje primo de 300 es 3, ya que 300 = 2*2* 3*5*5.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `maximumScore`. Este método se encarga de calcular la máxima puntuación posible tras aplicar hasta `k` operaciones en el array `nums`.

### Detalles de la implementación

- **Precalcular el menor factor primo (SPF)**: Usamos el método de la Criba de Eratóstenes para precalcular el menor factor primo para cada número hasta el valor máximo en `nums`.
- **Cálculo del puntaje primo**: Para cada número en `nums`, calculamos el puntaje primo, que corresponde a la cantidad de factores primos distintos.
- **Uso de pilas para subarreglos**: Para cada número en `nums`, calculamos cuántos subarreglos lo tienen como el elemento máximo mediante dos pasadas con pilas (una para el lado izquierdo y otra para el derecho).
- **Ordenación de contribuciones**: Los números se ordenan en función de su valor, priorizando los de mayor valor para maximizar la puntuación.
- **Cálculo final**: Se multiplican los valores de los subarreglos seleccionados por el número de veces que deben ser utilizados, asegurando que no exceda el límite de `k` operaciones.

## Uso

Para utilizar este código, simplemente se debe crear una instancia de la clase `Solution` y llamar al método `maximumScore` pasando el array `nums` y el número `k` como parámetros. El resultado será la puntuación máxima posible tras aplicar las operaciones.

```python
if __name__ == "__main__":
    nums = [8, 3, 9, 3, 8]
    k = 2

    sol = Solution()
    result = sol.maximumScore(nums, k)
    print(result)  # Output: 81
```

## Conclusión

El ejercicio "Apply Operations to Maximize Score" proporciona una excelente manera de practicar optimización en problemas combinatorios utilizando técnicas como la criba de Eratóstenes y el uso de pilas para encontrar subarreglos eficientes. Este enfoque no solo es útil en problemas de programación, sino que también mejora la comprensión de las operaciones sobre arrays y el manejo de factores primos. El resultado obtenido es una puntuación máxima bajo restricciones, y el algoritmo optimizado asegura que incluso para tamaños grandes de entrada, la solución sea eficiente.
