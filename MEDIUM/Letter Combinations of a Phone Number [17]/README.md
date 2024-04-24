# Letter Combinations of a Phone Number

Este archivo README documenta el ejercicio "Letter Combinations of a Phone Number". A continuación se describe el contenido del ejercicio, cómo está implementado, cómo usarlo y las conclusiones que se pueden extraer.

## Descripción

El objetivo de este ejercicio es implementar una solución al problema de encontrar todas las posibles combinaciones de letras que se pueden formar a partir de una cadena de dígitos del 2 al 9, tal como lo representan los botones de un teléfono tradicional. Este tipo de problema es común en entrevistas de programación y puede ser útil para entender conceptos como backtracking y recursión.

El problema se define de la siguiente manera:

* Dada una cadena de dígitos del 2 al 9, se deben retornar todas las combinaciones posibles de letras que esos números podrían representar.
* Las combinaciones pueden ser devueltas en cualquier orden.
* No se considera el dígito 1 ya que no representa ninguna letra.

Ejemplos de entradas y salidas:

* Entrada: "23", Salida: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
* Entrada: "", Salida: []
* Entrada: "2", Salida: ["a", "b", "c"]

## Implementación

El código está implementado en Python y utiliza un enfoque de backtracking para generar las combinaciones. Se define una clase Solution que contiene el método letterCombinations. Este método acepta un string digits y retorna una lista de combinaciones de letras posibles.

## Detalles técnicos

* La función recurvise_search es una función auxiliar interna que utiliza la recursión para construir las combinaciones. Utiliza backtracking para explorar todas las posibles combinaciones y luego vuelve atrás para explorar otras posibilidades.
* Un diccionario chars_for_number_dict mapea cada dígito a sus correspondientes letras, facilitando la búsqueda de combinaciones.
* Se verifica si la cadena de entrada está vacía al inicio, retornando una lista vacía si es así.

## Uso

Para utilizar este código, se debe instanciar un objeto de la clase Solution y llamar al método letterCombinations pasando la cadena de dígitos como argumento. A continuación, se muestra un ejemplo de cómo ejecutar el código desde un script Python:

```python
if __name__ == "__main__":
    digits = "243"
    solution = Solution()
    combinations = solution.letterCombinations(digits)
    print(combinations)
```

Este ejemplo imprimirá todas las combinaciones de letras para los dígitos "243".

## Conclusión

Este ejercicio proporciona una excelente oportunidad para practicar técnicas de programación como la recursión y el backtracking. Es útil para entender cómo se pueden explorar todas las posibles combinaciones de un conjunto de opciones de manera eficiente. Además, este problema es relevante para entender cómo se pueden manejar representaciones de estructuras de datos como diccionarios y listas en Python.
