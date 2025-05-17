# Sort Colors

## Descripción

El ejercicio **"Sort Colors"** consiste en ordenar un array que contiene objetos coloreados con tres posibles valores: rojo, blanco y azul, representados respectivamente por los enteros 0, 1 y 2. El objetivo es reorganizar el array **in-place** para que todos los objetos del mismo color queden juntos y en el orden rojo, blanco y azul.

Este problema es clásico en algoritmos de clasificación y es útil para entender técnicas de ordenamiento sin depender de funciones de ordenación genéricas, trabajando directamente sobre los elementos con restricciones de espacio y eficiencia.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, con un método `sortColors` que recibe un array `nums` y modifica su orden en tiempo real.

### Detalles de la implementación

- **Algoritmo utilizado:** Bubble Sort, un algoritmo simple de comparación que funciona intercambiando pares de elementos adyacentes cuando están fuera de orden.
- **Ordenamiento in-place:** El método no utiliza memoria adicional significativa, ya que modifica el array original directamente.
- **Complejidad:** Aunque Bubble Sort no es el más eficiente para grandes volúmenes de datos (O(n²)), para el tamaño limitado de este problema (hasta 300 elementos) es adecuado y sencillo de entender.
- **Restricciones:** El método no retorna ningún valor, ya que la modificación ocurre sobre la estructura de datos pasada como argumento.

## Uso

Para utilizar esta solución, basta con definir el array que contiene los colores representados por 0, 1 y 2, crear una instancia de la clase `Solution` y llamar al método `sortColors` con dicho array.

```python
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]

    sol = Solution()
    sol.sortColors(nums)
    print(nums)  # Salida esperada: [0, 0, 1, 1, 2, 2]
```

## Conclusión

El ejercicio "Sort Colors" es un problema clásico de ordenación con una aplicación clara en la clasificación segmentada. La solución implementada con Bubble Sort es directa y adecuada para problemas de pequeña escala, sirviendo como una base didáctica para entender algoritmos de ordenación básicos y manipulación de arrays in-place. Este enfoque es fundamental para reforzar conceptos de algoritmos, eficiencia y optimización espacial en problemas de clasificación específica.
