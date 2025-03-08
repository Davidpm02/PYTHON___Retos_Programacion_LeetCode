# Closest Prime Numbers in Range

## Descripción

El ejercicio "Closest Prime Numbers in Range" consiste en encontrar el par de números primos dentro de un rango dado que tengan la menor diferencia entre sí. Se proporciona un rango definido por dos enteros positivos `left` y `right`, y el objetivo es identificar los dos números primos consecutivos más cercanos dentro de dicho rango.

Si hay múltiples pares que cumplen con esta condición, se debe devolver el par con el número más pequeño como primer elemento. Si no existen suficientes números primos en el rango, se retorna `[-1, -1]`.

Este problema es relevante en matemáticas y teoría de números, ya que implica el uso de algoritmos eficientes para la identificación de números primos dentro de un rango determinado.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que contiene el método `closestPrimes`. Este método emplea la **Criba de Eratóstenes** para generar los números primos en el rango dado y luego encuentra el par de primos consecutivos más cercanos.

### Detalles de la implementación

1. **Generación de números primos:** Se utiliza la Criba de Eratóstenes para identificar los números primos hasta `right` de manera eficiente.
2. **Filtrado del rango:** Se extraen los números primos dentro del intervalo `[left, right]`.
3. **Búsqueda del par más cercano:** Se recorren los primos identificados y se selecciona el par con la menor diferencia entre sí.

## Uso

Para ejecutar el código, se debe instanciar la clase `Solution` y llamar al método `closestPrimes`, proporcionando los valores de `left` y `right`.

```python
if __name__ == "__main__":
    left = 10
    right = 19

    sol = Solution()
    result = sol.closestPrimes(left, right)
    print(result)  # Output: [11, 13]
```

## Conclusión

El ejercicio "Closest Prime Numbers in Range" es un problema que combina la teoría de números con la optimización algorítmica. La solución implementada aprovecha la Criba de Eratóstenes para obtener los números primos de manera eficiente, lo que permite realizar la búsqueda del par óptimo en tiempo reducido. Esta técnica es fundamental en aplicaciones donde se requiere identificar números primos en rangos amplios, como en criptografía y en la generación de claves seguras.
