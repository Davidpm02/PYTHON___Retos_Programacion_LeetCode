# Number of Ways to Split Array

## Descripción

El ejercicio "Number of Ways to Split Array" consiste en encontrar todas las formas válidas de dividir una lista de enteros en dos partes. Se considera una división válida si la suma de los primeros elementos en una parte es mayor o igual a la suma de los elementos restantes en la otra parte. La división se debe realizar de forma que ambas partes no estén vacías, es decir, debe existir al menos un elemento en el lado derecho de la división.

## Implementación

La implementación del ejercicio se realiza en Python utilizando la clase `Solution`. El método `waysToSplitArray` recibe un arreglo de enteros `nums` y devuelve el número de formas válidas de dividirlo. Para cada posible punto de división, se calcula la suma de los dos subconjuntos resultantes y se verifica si la suma de los elementos en la primera parte es mayor o igual a la suma de la segunda.

### Detalles de la implementación

1. **Cálculo de la suma total:** Se calcula la suma de todos los elementos del arreglo `nums`. Este valor es utilizado para calcular las sumas parciales en cada iteración.
  
2. **Suma parcial (izquierda y derecha):** Se mantiene una suma acumulada de la parte izquierda, que va aumentando a medida que avanzamos en el arreglo. La suma de la parte derecha se calcula restando la suma acumulada de la suma total.
  
3. **Validación de la división:** En cada iteración, se compara la suma de la parte izquierda con la suma de la parte derecha. Si la primera es mayor o igual, se cuenta como una división válida.

### Complejidad

- El enfoque tiene una complejidad temporal de \(O(n)\), donde \(n\) es el número de elementos en el arreglo `nums`, lo que lo hace eficiente para listas de longitud considerable.

## Uso

Para utilizar este código, simplemente proporciona una lista de enteros representando los valores en el arreglo `nums` y llama al método `waysToSplitArray` para obtener el número de formas válidas de división.

```python
if __name__ == "__main__":
    nums = [10, 4, -8, 7]

    sol = Solution()
    result = sol.waysToSplitArray(nums)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Number of Ways to Split Array" resalta cómo manejar operaciones sobre subconjuntos de un arreglo, específicamente para resolver un problema de partición con condiciones sobre las sumas parciales. La implementación ofrece un enfoque eficiente para calcular el número de divisiones válidas en un arreglo de enteros, utilizando una complejidad temporal de 𝑂(𝑛). Este tipo de problemas tiene aplicaciones prácticas en algoritmos de optimización y partición de datos. El enfoque aquí presentado es simple pero efectivo, lo que permite resolver el ejercicio en tiempo lineal incluso para entradas grandes.
