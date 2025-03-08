# Count Total Number of Colored Cells

## Descripción

El ejercicio **"Count Total Number of Colored Cells"** consiste en determinar cuántas celdas están coloreadas después de `n` minutos en una matriz bidimensional infinita. El proceso de coloreado sigue las siguientes reglas:

1. En el primer minuto, se colorea una celda arbitraria.
2. Cada minuto siguiente, se colorea cualquier celda sin color que toque una celda ya coloreada.

El objetivo es calcular el número total de celdas coloreadas después de `n` minutos.

## Implementación

La solución se implementa en Python dentro de la clase `Solution`, que contiene el método `coloredCells`. Este método evalúa cuántas celdas han sido coloreadas al final del tiempo dado.

### Detalles de la Implementación

- **Casos base:** Para `n = 1`, solo se colorea una celda. Para `n = 2` y `n = 3`, los valores son calculados directamente.
- **Fórmula general:** Para `n > 3`, la cantidad de celdas coloreadas sigue la expresión:
  
  \[
  \text{celdas coloreadas} = n^2 + (n - 1)^2
  \]
  
  Esto se basa en la observación de que la figura resultante tiene una estructura de diamante que crece de manera cuadrática con `n`.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `coloredCells` pasando el valor de `n` como argumento:

```python
if __name__ == "__main__":
    n = 4  # Definir el valor de n
    sol = Solution()
    result = sol.coloredCells(n)
    print(result)  # Devuelve el número total de celdas coloreadas
```

## Conclusión

El ejercicio **"Count Total Number of Colored Cells"** permite explorar patrones de crecimiento en estructuras geométricas y aplicar fórmulas matemáticas para optimizar el cálculo del resultado. La solución presentada tiene una complejidad de \(O(1)\) para la evaluación de `n > 3`, lo que la hace altamente eficiente incluso para valores grandes de `n`.
