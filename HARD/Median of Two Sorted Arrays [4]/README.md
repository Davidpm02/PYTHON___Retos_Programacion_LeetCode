# README.md para "Median of Two Sorted Arrays"

## Descripción

Este ejercicio aborda el problema de encontrar la mediana de dos matrices ordenadas de tamaños m y n. El objetivo es fusionar estas matrices y calcular su mediana de una manera eficiente, con una complejidad de tiempo objetivo de O(log(m+n)). Este problema no solo es fundamental para entender algoritmos de búsqueda y ordenación, sino que también es relevante para aplicaciones prácticas en estadísticas y ciencia de datos, donde el cálculo de medianas es una operación común.

## Implementación

La solución se implementa en la clase Solution, que contiene el método findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float. Este método toma dos listas de números enteros como entrada y retorna la mediana de los valores combinados de ambas listas.

El proceso de implementación es el siguiente:

* Se fusionan las dos listas de entrada en una nueva lista.
* La lista resultante se ordena.
* Se calcula la mediana de la lista ordenada, considerando los casos de listas con un número par e impar de elementos.

## Uso

Para usar esta solución:

* Guarda el código en un archivo, por ejemplo, **median_sorted_arrays.py**.
* Asegúrate de que Python está instalado en tu sistema.
* Modifica las variables array1 y array2 al final del script para reflejar los conjuntos de datos que deseas analizar.
* Ejecuta el script. La ejecución del método findMedianSortedArrays con las listas proporcionadas imprimirá la mediana de los valores combinados.

## Conclusión

Este ejercicio demuestra un enfoque efectivo para calcular la mediana de dos matrices ordenadas. A través de la combinación, ordenación y cálculo de medianas, los desarrolladores pueden abordar problemas similares en aplicaciones reales que requieren análisis estadístico preciso y eficiente. Este problema subraya la importancia de comprender algoritmos fundamentales y su aplicación práctica en la ciencia de datos y áreas relacionadas.
