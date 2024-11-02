# Hamming Distance

## Descripción

El ejercicio "Hamming Distance" tiene como objetivo calcular la distancia de Hamming entre dos enteros. La **distancia de Hamming** se define como el número de posiciones en las que los bits correspondientes de dos números enteros son diferentes. Esta métrica es útil en el procesamiento de datos y redes, donde se evalúan las diferencias a nivel de bits entre distintas representaciones binarias.

## Implementación

La solución se implementa en Python en una clase `Solution` con el método `hammingDistance`. Este método calcula la distancia de Hamming entre los enteros `x` e `y` mediante la siguiente lógica:

### Detalles de la implementación

1. **Conversión a binario**: Los enteros se convierten a su representación binaria utilizando `format(x, 'b')` y `format(y, 'b')`, generando cadenas binarias sin el prefijo `0b`.

2. **Igualación de longitud de bits**: Si las cadenas binarias resultantes tienen longitudes diferentes, se rellenan con ceros (`0`) a la izquierda para igualar su longitud. Esto asegura una comparación bit a bit alineada.

3. **Comparación bit a bit**: Los bits de ambas representaciones se comparan posición por posición, y se incrementa el contador `hamming_distance` cada vez que se detecta una diferencia.

4. **Resultado**: Al finalizar la comparación, el método devuelve la distancia de Hamming calculada.

## Uso

Para utilizar este código, simplemente debes definir dos números enteros x y y, crear una instancia de la clase Solution, y llamar al método hammingDistance con los enteros como parámetros. El resultado será la distancia de Hamming entre los dos números.

```python
if __name__ == "__main__":
    x = 1
    y = 4

    sol = Solution()
    distance = sol.hammingDistance(x, y)
    print(distance)  # Output: 2
```

## Conclusión

El ejercicio "Hamming Distance" proporciona una manera eficiente de medir las diferencias entre dos números a nivel de bits. La solución implementada utiliza operaciones básicas en Python para calcular la distancia de Hamming, siendo útil en aplicaciones donde es esencial comparar datos binarios. Esta solución también refuerza el uso de métodos de manipulación de bits y conversión de bases numéricas, conceptos importantes en programación y análisis de datos. Esta implementación es clara, simple y puede ser adaptada para múltiples contextos en ingeniería y ciencias de la computación.
