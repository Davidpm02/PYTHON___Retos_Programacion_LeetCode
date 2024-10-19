# Fizz Buzz

## Descripción

El ejercicio "Fizz Buzz" consiste en generar un array de cadenas de texto basadas en las reglas clásicas del juego FizzBuzz. Este ejercicio es común en entrevistas de programación debido a su simplicidad para demostrar el manejo de bucles, condiciones, y la manipulación de cadenas.
Reglas:

1. Si un número es divisible por 3 y 5, se añade la cadena "FizzBuzz".
2. Si un número es divisible solo por 3, se añade la cadena "Fizz".
3. Si un número es divisible solo por 5, se añade la cadena "Buzz".
4. En cualquier otro caso, se añade el número como una cadena de texto.

Este ejercicio ayuda a practicar el uso de condicionales y el manejo básico de arrays en Python.

## Implementación

La implementación se realiza utilizando una clase Solution que contiene el método fizzBuzz. Este método genera un array de cadenas de texto con las reglas mencionadas, iterando desde 1 hasta el número n proporcionado como entrada.

### Detalles de la implementación

* Iteración: Se itera a través de los números del 1 al n.
* Condiciones: Dentro del bucle, se evalúan las condiciones de divisibilidad para decidir qué cadena agregar al array.
  * Si el número es divisible por 3 y 5, se añade "FizzBuzz".
  * Si solo es divisible por 3, se añade "Fizz".
  * Si solo es divisible por 5, se añade "Buzz".
  * En caso contrario, se añade el número convertido a cadena.

## Uso

Para utilizar el código, se debe definir el número n que indica cuántos elementos tendrá el array resultante. Luego, se instancia la clase Solution y se llama al método fizzBuzz pasando n como argumento.

```python
if __name__ == "__main__":
    n = 15
    sol = Solution()
    result = sol.fizzBuzz(n)
    print(result)
    # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```

Este ejemplo genera un array para n = 15, siguiendo las reglas del juego FizzBuzz.

## Conclusión

El ejercicio "Fizz Buzz" es una solución clásica que demuestra cómo iterar y aplicar condiciones en un bucle para generar resultados basados en reglas específicas. A pesar de su simplicidad, es un buen ejercicio para evaluar el conocimiento básico de programación, como el uso de condicionales, bucles y arrays. Además, la implementación es eficiente y fácil de entender, lo que lo convierte en un excelente ejemplo para fortalecer conceptos fundamentales.
