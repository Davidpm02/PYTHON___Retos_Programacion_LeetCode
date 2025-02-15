# Max Sum of a Pair With Equal Sum of Digits

## Descripción

El ejercicio "Max Sum of a Pair With Equal Sum of Digits" consiste en encontrar el par de números dentro de un array cuya suma de dígitos sea igual y cuya suma total sea la mayor posible. Si no existe tal par, se debe devolver -1. Este problema está relacionado con técnicas de agrupación y optimización, aplicadas en algoritmos eficientes de búsqueda y clasificación.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que contiene el método `maximumSum`. Este método itera sobre la lista de números, agrupa los valores según la suma de sus dígitos y luego encuentra el par con la suma máxima.

### Detalles de la implementación

- **Cálculo de la suma de dígitos:** Se obtiene la suma de los dígitos de cada número convirtiéndolo a una cadena y sumando sus valores numéricos.
- **Agrupación por suma de dígitos:** Se usa un diccionario donde la clave es la suma de dígitos y el valor es una lista de números con dicha suma.
- **Búsqueda del par con la suma más alta:** Para cada grupo, se ordenan los valores en orden descendente y se toma la suma de los dos mayores.
- **Optimización:** Se garantiza eficiencia utilizando un solo recorrido para la agrupación y otro para la búsqueda de la máxima suma.

## Uso

Para utilizar este código, se debe definir una lista de números enteros positivos y luego crear una instancia de la clase `Solution`. Se llama al método `maximumSum` con la lista como argumento y se obtiene el resultado.

```python
if __name__ == "__main__":
    nums = [18, 43, 36, 13, 7]
    
    sol = Solution()
    result = sol.maximumSum(nums)
    print(result)  # Output: 54
```

## Conclusión

El ejercicio "Max Sum of a Pair With Equal Sum of Digits" proporciona una forma eficiente de encontrar la mayor suma de dos números dentro de un conjunto, cumpliendo con la condición de tener la misma suma de dígitos. La solución implementada utiliza estructuras de datos adecuadas para garantizar un buen rendimiento, con una lógica clara y modular. Este tipo de problema es útil en aplicaciones de optimización y procesamiento de datos numéricos.
