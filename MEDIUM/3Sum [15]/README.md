# 3Sum

## Descripción

El problema "3Sum" consiste en encontrar todos los tríos de números en un arreglo de enteros tales que la suma de los tres números sea igual a cero. Este ejercicio busca solucionar el problema evitando tríos duplicados y garantizando que cada trío sea único en términos de sus índices y valores.

## Implementación

El código está implementado en Python y utiliza el módulo collections para aprovechar la clase Counter, que ayuda en el conteo de ocurrencias de cada número en el arreglo. La estrategia principal para resolver el problema es:

* Ordenar el arreglo: Esto facilita la comparación y ayuda a implementar la búsqueda con dos punteros de manera eficiente.
* Uso del contador: Se limita la repetición de cualquier número a un máximo de tres veces, lo que es suficiente para cubrir todos los casos posibles sin redundancia.
* Búsqueda con dos punteros: Se emplea un enfoque de dos punteros para identificar los tríos cuya suma es cero. Esto se realiza de manera iterativa ajustando los punteros basados en la suma calculada.

La clase Solution contiene un método threeSum que recibe un arreglo de enteros y retorna una lista de tríos que cumplen con la condición de suma cero.

## Uso

Para utilizar este código, se debe instanciar la clase Solution y llamar al método threeSum con el arreglo de números como argumento. Aquí un ejemplo de cómo usarlo:

```python
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)  # Output esperado: [[-1, -1, 2], [-1, 0, 1]]
```

Este fragmento de código inicializa un arreglo con números, crea una instancia de Solution y llama al método threeSum para obtener y mostrar los tríos que suman cero.

## Conclusión

El ejercicio "3Sum" es un excelente ejemplo de cómo se pueden aplicar técnicas de algoritmos y estructuras de datos como ordenamiento, conteo y búsqueda con dos punteros para resolver problemas complejos de manera eficiente. La solución proporcionada aquí demuestra un enfoque práctico y optimizado para el manejo de arrays y búsqueda de resultados específicos bajo ciertas condiciones.
