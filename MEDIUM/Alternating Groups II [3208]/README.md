# Alternating Groups II

## Descripción

El ejercicio "Alternating Groups II" consiste en encontrar el número de grupos alternantes dentro de un círculo de baldosas rojas y azules. Se proporciona un array de enteros `colors` y un entero `k`. Cada posición del array representa el color de una baldosa:

- `colors[i] == 0` indica que la baldosa es roja.
- `colors[i] == 1` indica que la baldosa es azul.

Un grupo alternante es cualquier conjunto de `k` baldosas contiguas dentro del círculo donde los colores alternan en cada posición, excepto en los extremos. Dado que el arreglo representa un círculo, la primera y la última baldosa se consideran adyacentes.

El objetivo es contar cuántos grupos alternantes existen dentro del círculo.

## Implementación

La solución se implementa en Python utilizando una clase `Solution`, que contiene el método `numberOfAlternatingGroups`. Este método evalúa la cantidad de grupos alternantes en el arreglo `colors` con longitud `k`.

### Detalles de la implementación

- **Cálculo de diferencias:** Se genera una lista auxiliar `diff` que almacena `1` si dos baldosas consecutivas tienen colores distintos y `0` en caso contrario.
- **Extensión del array:** Para manejar la naturaleza circular del problema, se extiende el array `diff` con los primeros `k-2` elementos.
- **Ventana deslizante:** Se utiliza una ventana deslizante de tamaño `k-1` para contar la cantidad de diferencias en segmentos consecutivos del arreglo extendido.
- **Cálculo de grupos alternantes:** Se cuenta cuántas veces la suma dentro de la ventana alcanza el valor `k-1`, indicando que el grupo cumple con la condición de alternancia.

## Uso

Para utilizar este código, se debe definir un array de colores `colors` y un entero `k`, luego instanciar la clase `Solution` y llamar al método `numberOfAlternatingGroups`.

```python
if __name__ == "__main__":
    colors = [0,1,0,1,0]
    k = 3
    
    sol = Solution()
    result = sol.numberOfAlternatingGroups(colors, k)
    print(result)  # Salida esperada: 3
```

## Conclusión

El ejercicio "Alternating Groups II" proporciona una manera eficiente de identificar patrones de alternancia en una secuencia cíclica. La solución implementada aprovecha estructuras auxiliares y una técnica de ventana deslizante para mejorar el rendimiento, asegurando una evaluación óptima incluso para valores grandes de `colors.length`. Este tipo de problema es útil en el procesamiento de secuencias y en la optimización de algoritmos de búsqueda en estructuras circulares.
