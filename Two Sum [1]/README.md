# README.md para el ejercicio "Two Sum"

## Descripción

Este repositorio contiene la implementación de un popular problema de algoritmo conocido como "Two Sum". El objetivo de este ejercicio es encontrar dos números dentro de un arreglo dado (nums) que sumen un objetivo específico (target) y retornar los índices de estos dos números. Es importante notar que cada elemento del arreglo puede ser utilizado una sola vez en la suma.

La solución es implementada en Python, utilizando una clase Solution que contiene el método twoSum. Este método es responsable de realizar la lógica necesaria para encontrar los índices de los dos números que suman el objetivo dado.

## Implementación

El código está estructurado de la siguiente manera:

* Se importa el tipo List desde el módulo typing para anotar los tipos de los parámetros y del valor retornado por el método twoSum.
* Se define la clase Solution que encapsula la lógica del algoritmo.
* Dentro de la clase Solution, se define el método twoSum, que toma como parámetros un arreglo de números nums y un número objetivo target. Este método retorna una lista de dos índices correspondientes a los números en nums que suman target.
* La implementación interna del método twoSum utiliza dos bucles anidados para explorar todas las combinaciones posibles de dos números en el arreglo, buscando aquellos que cumplan con la condición de suma especificada.

La implementación hace uso de comentarios en primera persona para explicar el propósito y la lógica de las secciones clave del código, siguiendo las buenas prácticas de documentación.

## Uso

Para utilizar este código, puedes seguir los siguientes pasos:

* Asegúrate de tener Python instalado en tu sistema.
* Guarda el código en un archivo, por ejemplo, two_sum.py.
* Ejecuta el script desde la terminal o un IDE, lo cual instanciará un objeto de la clase Solution y llamará al método twoSum con un conjunto de parámetros de prueba (nums = [3,3] y target = 6).
* El método imprimirá los índices de los dos números en nums que suman target.

## Conclusión

Este ejercicio proporciona una solución al problema "Two Sum" utilizando un enfoque de fuerza bruta, donde se exploran todas las combinaciones posibles para encontrar la pareja de números que sumen el valor objetivo. Aunque efectiva para arreglos pequeños, esta implementación puede ser ineficiente para arreglos grandes debido a su complejidad temporal cuadrática. Este ejercicio sirve como una excelente oportunidad para entender conceptos fundamentales de algoritmos y estructuras de datos, así como para mejorar la habilidad de resolver problemas utilizando la programación.
