# Maximum Candies Allocated to K Children

## Descripción

El ejercicio "Maximum Candies Allocated to K Children" consiste en determinar el número máximo de caramelos que pueden recibir equitativamente `k` niños, a partir de un conjunto de montones de caramelos. Cada montón se puede dividir en submontones más pequeños, pero no se pueden combinar montones distintos.

El objetivo es encontrar la cantidad máxima de caramelos que puede recibir cada niño, asegurando que todos los niños reciban la misma cantidad y sin exceder la cantidad total de caramelos disponibles.

## Implementación

La solución se implementa en Python mediante una clase `Solution`, que contiene el método `maximumCandies`. Este método emplea una estrategia de búsqueda binaria para encontrar el tamaño óptimo de cada porción de caramelos que puede asignarse a `k` niños.

### Detalles de la implementación

- **Verificación inicial:** Si la cantidad total de caramelos es menor que `k`, no es posible repartir al menos un caramelo por niño, por lo que la función retorna `0` inmediatamente.
- **Búsqueda binaria:** Se define un rango de búsqueda entre `1` (mínima cantidad posible de caramelos por niño) y el tamaño del montón más grande.
- **División y conteo:** Para cada valor `mid` dentro del rango de búsqueda, se calcula cuántos montones de tamaño `mid` pueden formarse a partir de los montones originales.
- **Ajuste de búsqueda:** Si el número de montones formados es al menos `k`, significa que es posible asignar caramelos con ese tamaño, por lo que se intenta aumentar el valor de `mid`. En caso contrario, se reduce el rango de búsqueda.

## Uso

Para utilizar este código, se debe proporcionar una lista de enteros `candies`, que representa los montones de caramelos, y un entero `k`, que indica el número de niños. Luego, se instancia la clase `Solution` y se llama al método `maximumCandies`.

```python
if __name__ == "__main__":
    candies = [5, 8, 6]
    k = 3
    
    sol = Solution()
    max_candies = sol.maximumCandies(candies, k)
    print(max_candies)  # Salida esperada: 5
```

## Conclusión

El ejercicio "Maximum Candies Allocated to K Children" presenta una aplicación eficiente del enfoque de búsqueda binaria para optimizar la distribución de recursos. La solución implementada garantiza una asignación equitativa de caramelos a `k` niños mientras maximiza la cantidad recibida por cada uno.

Este problema es un buen ejemplo de cómo las técnicas de búsqueda pueden aplicarse a la optimización de recursos en estructuras discretas y cómo la estrategia de dividir y evaluar permite encontrar soluciones óptimas en tiempos eficientes.
