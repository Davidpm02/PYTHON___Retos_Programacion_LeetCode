# Product of the Last K Numbers

## Descripción

El ejercicio "Product of the Last K Numbers" consiste en diseñar un algoritmo que acepte un flujo de números enteros y permita recuperar el producto de los últimos `k` números de dicho flujo en cualquier momento. Para ello, se debe implementar una clase `ProductOfNumbers` que proporcione las siguientes funcionalidades:

- `ProductOfNumbers()`: Inicializa el objeto con un flujo vacío.
- `add(int num)`: Agrega un número entero `num` al flujo.
- `getProduct(int k)`: Retorna el producto de los últimos `k` números añadidos al flujo.

Los casos de prueba garantizan que en cualquier momento el producto de cualquier secuencia continua de números cabe dentro de un entero de 32 bits sin desbordamiento.

## Implementación

La solución utiliza una lista de productos acumulativos para optimizar la recuperación del producto de los últimos `k` números. Este enfoque permite calcular el producto en tiempo constante `O(1)`, lo que mejora la eficiencia en comparación con un enfoque ingenuo basado en iteraciones.

Detalles de la implementación:

- Se mantiene una lista de productos acumulativos, donde cada elemento en la lista representa el producto de todos los números hasta ese punto.
- Si se añade un `0`, la lista se reinicia, ya que cualquier producto que incluya `0` siempre será `0`.
- Para calcular el producto de los últimos `k` números, se divide el último producto acumulado por el producto acumulado de `k` posiciones atrás.
- Si `k` es mayor que la cantidad de elementos desde el último `0`, se retorna `0`.

## Uso

Para utilizar este código, se debe instanciar un objeto de la clase `ProductOfNumbers` y llamar a los métodos `add` y `getProduct` según sea necesario.

```python
if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)        # [3]
    productOfNumbers.add(0)        # [3,0]
    productOfNumbers.add(2)        # [3,0,2]
    productOfNumbers.add(5)        # [3,0,2,5]
    productOfNumbers.add(4)        # [3,0,2,5,4]
    print(productOfNumbers.getProduct(2))  # Output: 20
    print(productOfNumbers.getProduct(3))  # Output: 40
    print(productOfNumbers.getProduct(4))  # Output: 0
    productOfNumbers.add(8)        # [3,0,2,5,4,8]
    print(productOfNumbers.getProduct(2))  # Output: 32
```

## Conclusión

El ejercicio "Product of the Last K Numbers" demuestra una solución eficiente para calcular productos de los últimos `k` elementos en un flujo de datos. La utilización de productos acumulativos reduce el tiempo de consulta a `O(1)`, lo que lo hace altamente escalable para grandes volúmenes de datos. Además, la implementación maneja correctamente los ceros, asegurando que los cálculos sean precisos en todas las condiciones posibles.
