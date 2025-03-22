# Divide Array Into Equal Pairs

## Descripción

El ejercicio "Divide Array Into Equal Pairs" consiste en determinar si es posible dividir un arreglo de números enteros en pares donde cada par contenga elementos iguales. Se nos proporciona un array `nums` de longitud `2 * n`, y debemos verificar si es posible formar `n` pares cumpliendo las siguientes condiciones:

- Cada elemento pertenece exactamente a un solo par.
- Los elementos dentro de cada par son iguales.

Si se pueden formar los pares correctamente, se devuelve `true`, de lo contrario, `false`.

## Implementación

La implementación se realiza en Python mediante la clase `Solution`, que contiene el método `divideArray`. Este método utiliza un diccionario de frecuencias (`Counter`) para contar cuántas veces aparece cada número en `nums` y determinar si cada número tiene una cantidad par de ocurrencias, lo que garantizaría que puede formar pares completos.

## Detalles de la implementación

- **Verificación de la longitud del array:** Se comprueba que `nums` tenga un número par de elementos, pues si no es así, no es posible formar pares.
- **Conteo de elementos:** Se usa `Counter` de la librería `collections` para contar la frecuencia de cada número en `nums`.
- **Validación de pares:** Se recorre el conteo de frecuencias y se verifica que cada número aparezca un número par de veces.
- **Optimización:** La solución tiene una complejidad de `O(n)`, donde `n` es la cantidad de elementos en `nums`, ya que solo requiere recorrer el array una vez para contar los elementos y otra para verificar las frecuencias.

## Uso

Para utilizar este código, simplemente se debe definir el array de entrada `nums` y crear una instancia de la clase `Solution`. Luego, se llama al método `divideArray` con `nums` como argumento para obtener el resultado.

```python
if __name__ == "__main__":
    nums = [3,2,3,2,2,2]
    sol = Solution()
    result = sol.divideArray(nums)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Divide Array Into Equal Pairs" permite reforzar el manejo de estructuras de datos como diccionarios y listas en Python. Utilizar `Counter` facilita la verificación de frecuencias de elementos, asegurando una implementación eficiente. Este problema es relevante en contextos donde es necesario agrupar elementos en pares de manera equitativa, como en la asignación de recursos o en algoritmos de emparejamiento.
