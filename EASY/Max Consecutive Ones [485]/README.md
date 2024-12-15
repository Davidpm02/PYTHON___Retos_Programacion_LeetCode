# Max Consecutive Ones

## Descripción

El ejercicio "Max Consecutive Ones" consiste en encontrar el número máximo de unos consecutivos en un arreglo binario (una lista de 0s y 1s). La tarea es identificar el tramo más largo de unos consecutivos dentro de este arreglo y devolver su longitud. Este problema es útil en el análisis de secuencias en diversas aplicaciones, como el procesamiento de señales o en la búsqueda de patrones repetitivos en grandes conjuntos de datos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `findMaxConsecutiveOnes`. Este método recorre el arreglo dado y cuenta la cantidad de unos consecutivos. Cuando se encuentra un 0, se compara el número de unos consecutivos encontrados hasta el momento con el valor máximo registrado y se resetea el contador. Al final del recorrido, se devuelve el número máximo de unos consecutivos.

## Detalles de la implementación

- **Recorrido del arreglo:** El método recorre cada elemento del arreglo `nums`. Si encuentra un 0, termina el contador de unos consecutivos y lo compara con el máximo actual. Si encuentra un 1, incrementa el contador de unos consecutivos.
- **Almacenaje de valores consecutivos:** Cada vez que se encuentra un 0 o al final del arreglo, el contador de unos consecutivos se guarda en una lista.
- **Cálculo del máximo:** El valor máximo de esta lista de secuencias de unos consecutivos es retornado como el resultado.

## Uso

Para utilizar este código, simplemente se debe proporcionar una lista binaria de números como entrada. Luego se crea una instancia de la clase `Solution` y se llama al método `findMaxConsecutiveOnes`, pasando la lista como argumento. El resultado será la cantidad máxima de unos consecutivos en la lista.

```python
if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    
    sol = Solution()
    max_ones = sol.findMaxConsecutiveOnes(nums)
    print(max_ones)  # Output: 3
```

## Conclusión

El ejercicio "Max Consecutive Ones" proporciona una solución simple pero eficaz para encontrar la longitud de la secuencia más larga de unos consecutivos en un arreglo binario. Este enfoque resuelve el problema de manera eficiente y es útil en varios escenarios donde las secuencias de bits consecutivos son de interés. La implementación proporciona un algoritmo fácil de entender y aplicar, y refuerza conceptos clave en el manejo de secuencias y estructuras de datos en Python.
