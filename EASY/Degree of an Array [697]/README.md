# Degree of an Array

## Descripción

El ejercicio "Degree of an Array" consiste en encontrar la longitud mínima de un subarreglo contiguo que tenga el mismo grado que el arreglo original. El grado de un arreglo se define como la máxima frecuencia de aparición de cualquiera de sus elementos. Este tipo de problema es útil en el análisis de datos y algoritmos de optimización, ya que permite identificar patrones significativos en secuencias numéricas.

## Implementación

La implementación del ejercicio se realiza utilizando una clase Solution en Python. Esta clase incluye el método findShortestSubArray, que resuelve el problema aplicando las siguientes etapas clave:

1. Contar la frecuencia de elementos: Utilizo el objeto Counter de la librería collections para calcular la frecuencia de cada elemento.

2. Identificar los elementos con el grado máximo: Se filtran los elementos que alcanzan el grado máximo y se almacenan junto con sus índices en un diccionario.

3. Calcular la longitud de los subarreglos: Con base en los índices obtenidos, se calcula la diferencia entre el último y el primer índice de cada elemento con el grado máximo.

4. Devolver la longitud mínima: Se selecciona la longitud más corta y se devuelve.

## Uso

Para utilizar este código, basta con definir un arreglo de entrada nums y crear una instancia de la clase Solution. Luego, se invoca el método findShortestSubArray, que devuelve la longitud mínima del subarreglo con el mismo grado.

```python
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1]

    sol = Solution()
    result = sol.findShortestSubArray(nums)
    print(result)  # Salida: 2

    nums2 = [1, 2, 2, 3, 1, 4, 2]
    result = sol.findShortestSubArray(nums2)
    print(result)  # Salida: 6
```

## Conclusión

El ejercicio "Degree of an Array" introduce una manera eficiente de identificar subarreglos contiguos que mantengan propiedades específicas de la secuencia de entrada. La implementación utiliza estructuras de datos y herramientas integradas en Python, lo que permite una solución robusta y sencilla para procesar arreglos grandes de manera rápida. Este enfoque es aplicable en numerosos contextos donde se analiza el contenido y las características de secuencias numéricas.
