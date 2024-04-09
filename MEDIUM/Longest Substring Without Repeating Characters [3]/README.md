# README.md para "Longest Substring Without Repeating Characters"

## Descripción

Este ejercicio se centra en encontrar la longitud de la subcadena más larga sin caracteres repetidos dentro de una cadena dada s. Es un problema clásico que se encuentra comúnmente en entrevistas técnicas y ejercicios de programación, sirviendo como un buen indicador de la capacidad de un desarrollador para trabajar con estructuras de datos como diccionarios y aplicar técnicas como el deslizamiento de ventanas para resolver problemas complejos de manera eficiente.

## Implementación

La solución se presenta a través de la clase Solution, que contiene dos métodos principales:

* lengthOfLongestSubstring(s: str) -> int: Dada una cadena s, este método retorna la longitud de la subcadena más larga sin caracteres repetidos. Utiliza un diccionario window para rastrear los caracteres y sus índices más recientes. A medida que itera sobre s, ajusta una ventana de caracteres no repetidos y actualiza la longitud máxima encontrada.

* validateString(s): Un método auxiliar que asegura que la longitud de la cadena s cumple con las restricciones especificadas (0 <= s.length <= 5 * 10^4). Aunque es un método simple, ilustra la importancia de validar los datos de entrada antes de proceder con el algoritmo principal.

## Uso

Para utilizar esta solución en tu propio entorno de desarrollo, sigue estos pasos:

* Guarda el código proporcionado en un archivo, por ejemplo, longest_substring.py.
* Asegúrate de tener Python instalado en tu sistema.
* Modifica la variable s en el bloque if __name__ == "__main__": para probar diferentes cadenas de acuerdo con tu caso de uso.
* Ejecuta el script. Esto invocará el método lengthOfLongestSubstring con la cadena proporcionada y imprimirá la longitud de la subcadena más larga sin caracteres repetidos.

## Conclusión

Este ejercicio demuestra una aplicación práctica de técnicas de deslizamiento de ventana y uso de diccionarios para resolver eficientemente el problema de encontrar la subcadena más larga sin repetición de caracteres. Además de su utilidad en entrevistas técnicas, el problema y su solución ofrecen una valiosa lección sobre el manejo de estructuras de datos y la implementación de algoritmos eficientes en Python, habilidades cruciales para cualquier desarrollador de software.
