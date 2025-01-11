# Assign Cookies

## Descripción

El ejercicio "Assign Cookies" consiste en determinar el número máximo de niños que pueden estar contentos al asignarles galletas, según su "factor de codicia" (greed factor). Cada niño tiene un valor mínimo de tamaño de galleta que lo hace feliz, y cada galleta tiene un tamaño. El objetivo es maximizar el número de niños satisfechos asignando las galletas de la forma más eficiente posible.

Este problema es útil para entender algoritmos de asignación, estrategias de optimización y manipulación de listas, aplicando principios como el ordenamiento y la comparación iterativa.

## Implementación

La solución utiliza una clase `Solution` que contiene el método `findContentChildren`. Este método evalúa las listas de factores de codicia y tamaños de galletas y determina cuántos niños pueden ser contentados con las galletas disponibles.

### Detalles de la implementación

- **Ordenamiento de datos:** Se ordenan tanto los factores de codicia de los niños como los tamaños de las galletas. Esto permite realizar asignaciones de manera óptima, asegurándose de asignar la galleta más pequeña posible que satisfaga a cada niño.
- **Asignación eficiente:** A medida que se itera por los tamaños de las galletas, se compara con los factores de codicia. Si una galleta cumple el requisito de un niño, este queda satisfecho y se elimina de la lista de pendientes.
- **Resultados:** Se mantiene un contador que indica cuántos niños han quedado satisfechos al finalizar el proceso.

## Uso

Para utilizar este código, se deben proporcionar las listas `g` (factores de codicia de los niños) y `s` (tamaños de las galletas) como parámetros del método `findContentChildren` de una instancia de la clase `Solution`.

```python
if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]

    sol = Solution()
    result = sol.findContentChildren(g, s)
    print(result)  # Output: 1
```

## Conclusión

El ejercicio "Assign Cookies" presenta una forma eficiente de resolver un problema clásico de asignación utilizando estrategias de ordenamiento y comparación. Este enfoque no solo resuelve el problema de manera efectiva, sino que también ofrece una visión clara de cómo optimizar recursos en situaciones reales. Es un excelente ejemplo de aplicación práctica de algoritmos simples para maximizar el rendimiento en asignaciones limitadas.
