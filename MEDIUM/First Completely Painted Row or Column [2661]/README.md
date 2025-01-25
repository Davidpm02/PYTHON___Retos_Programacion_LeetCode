# First Completely Painted Row or Column

## Descripción

El ejercicio "First Completely Painted Row or Column" consiste en determinar el índice más pequeño en el que, tras pintar elementos en una matriz `mat` utilizando los valores de un arreglo `arr`, se completa por primera vez una fila o una columna de la matriz. Este problema ilustra operaciones con matrices y seguimiento del estado en filas y columnas, lo que es crucial para diversas aplicaciones en programación y matemáticas computacionales.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `firstCompleteIndex`. Este método sigue los siguientes pasos:

1. **Mapeo de posiciones:** Crea un diccionario que relaciona cada valor de la matriz con sus coordenadas correspondientes (fila y columna).
2. **Contador de celdas pintadas:** Define dos listas para rastrear cuántas celdas han sido pintadas por fila y por columna.
3. **Procesamiento de los valores en `arr`:** Itera sobre los valores de `arr`, pintando las celdas en la matriz y actualizando los contadores.
4. **Verificación de filas o columnas completas:** En cada paso, verifica si se completa una fila o columna para devolver el índice correspondiente.

## Uso

Para utilizar el código, es necesario definir el arreglo `arr` y la matriz `mat`. A continuación, se crea una instancia de la clase `Solution` y se llama al método `firstCompleteIndex`. El resultado devuelto es el índice más pequeño que cumple con la condición establecida.

```python
if __name__ == "__main__":
    arr = [1, 3, 4, 2]
    mat = [[1, 4], [2, 3]]

    sol = Solution()
    result = sol.firstCompleteIndex(arr, mat)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "First Completely Painted Row or Column" plantea un problema interesante de mapeo y seguimiento de estado en estructuras matriciales, promoviendo el uso de estrategias eficientes para operaciones en tiempo lineal. La solución es adecuada para casos con matrices y arreglos de gran tamaño, dado su uso optimizado de espacio y cálculo basado en estructuras de datos simples como listas y diccionarios.
