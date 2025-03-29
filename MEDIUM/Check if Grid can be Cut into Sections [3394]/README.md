# Check if Grid can be Cut into Sections

## Descripcion

El ejercicio "Check if Grid can be Cut into Sections" consiste en determinar si es posible realizar dos cortes horizontales o dos cortes verticales en una cuadrícula de tamaño `n x n` de tal manera que:

- Cada una de las tres secciones resultantes contenga al menos un rectángulo.
- Cada rectángulo pertenezca exactamente a una única sección.

Se proporciona una lista de rectángulos representados por sus coordenadas dentro de la cuadrícula. No hay solapamientos entre rectángulos.

## Implementacion

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `checkValidCuts`. Este método evalúa si es posible realizar cortes válidos en la cuadrícula.

### Detalles de la implementación

- **Partición en el eje vertical y horizontal:** Se intentan cortes en ambas direcciones.
- **Ordenación de intervalos:** Se ordenan los rectángulos según sus coordenadas.
- **Cálculo de cortes válidos:** Se verifica la posibilidad de dividir los rectángulos en tres secciones separadas.

## Uso

Para utilizar este código, se debe definir el tamaño de la cuadrícula `n` y una lista de rectángulos con sus coordenadas. Luego, se crea una instancia de la clase `Solution` y se llama al método `checkValidCuts` con estos valores:

```python
if __name__ == "__main__":
    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    
    sol = Solution()
    result = sol.checkValidCuts(n, rectangles)
    print(result)  # Output: True
```

## Conclusion

El ejercicio "Check if Grid can be Cut into Sections" permite evaluar la segmentación de una cuadrícula en función de los rectángulos presentes. La solución implementada sigue un enfoque estructurado mediante la ordenación de intervalos y la verificación de cortes posibles, asegurando una partición válida. Esta tarea es relevante en problemas de segmentación espacial y optimización en estructuras de datos geométricas.
