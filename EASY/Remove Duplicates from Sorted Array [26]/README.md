# Remove Duplicates from Sorted Array

## Descripción

El ejercicio "Remove Duplicates from Sorted Array" se enfoca en eliminar duplicados de un arreglo de enteros ordenado de manera no decreciente, manteniendo sólo una instancia de cada elemento en su orden original. El objetivo principal es modificar el arreglo nums in situ para que los primeros k elementos contengan los elementos únicos en el mismo orden en que aparecían originalmente. Los elementos restantes del arreglo no son relevantes. Además, se debe retornar k, el número de elementos únicos.

Este problema es común en entrevistas de programación y es útil para entender el manejo de arreglos y algoritmos de filtrado en Python.

## Implementación

La clase Solution contiene un método removeDuplicates, que recibe un arreglo de enteros nums y retorna el número de elementos únicos después de eliminar duplicados. La implementación realiza las siguientes acciones:

* Utiliza la conversión del arreglo a un conjunto para eliminar duplicados y luego lo convierte de nuevo a lista, asegurando que esté ordenado. Esto es posible ya que el arreglo original está en orden no decreciente.
* Asigna el arreglo modificado de vuelta a nums utilizando slicing para modificar el arreglo original in situ.
* Retorna la longitud del arreglo modificado, que corresponde al número de elementos únicos k.

El método aprovecha las capacidades de Python con los conjuntos para eliminar duplicados y el slicing para modificar el arreglo de entrada directamente.

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Elimino duplicados utilizando un conjunto y vuelvo a ordenar
        nums[:] = sorted(set(nums))
        # Retorno la cantidad de elementos únicos
        return len(nums)
```

## Uso

Para utilizar la solución en un entorno de desarrollo o en un script directo de Python, primero se debe crear una instancia de Solution y luego llamar al método removeDuplicates con el arreglo deseado:

```python
nums = [1, 1, 2, 2, 3, 3, 3, 4]
sol = Solution()
k = sol.removeDuplicates(nums)
print("Número de elementos únicos:", k)
print("Arreglo modificado:", nums)
```

Este código imprimirá el número de elementos únicos y mostrará el estado final del arreglo nums.

## Conclusión

La implementación proporcionada es eficiente para el propósito del ejercicio, ofreciendo una solución concisa y efectiva para la eliminación de duplicados en arreglos ordenados. Esta tarea es esencial para cualquier desarrollador de Python, especialmente en el contexto de preparación de datos en Machine Learning, donde es crucial manejar datos sin redundancias. Esta solución no sólo es adecuada para entrevistas sino también para aplicaciones reales donde la eficiencia y claridad del código son prioritarias.
