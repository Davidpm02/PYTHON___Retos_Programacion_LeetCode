# Power of Four

## Descripción

El ejercicio "Power of Four" consiste en determinar si un número entero es una potencia de cuatro. Un número es considerado una potencia de cuatro si existe un entero x tal que n == 4^x. Esto implica que el número puede ser dividido por 4 repetidamente hasta llegar al valor 1 sin obtener restos en ninguna de las divisiones. La resolución de este problema es esencial en diversas áreas de la computación, particularmente cuando se manejan potencias de bases específicas, como es el caso de la base 4 en este ejercicio.

## Implementación

La implementación del ejercicio se realiza en Python mediante la clase Solution, que contiene el método isPowerOfFour. Este método se encarga de comprobar si un número dado n es una potencia de cuatro utilizando una serie de divisiones sucesivas. Si el número puede dividirse por 4 hasta llegar a 1, entonces es una potencia de cuatro.

### Detalles de la implementación

* División repetida: El método divide sucesivamente el número n entre 4, comprobando si el cociente sigue siendo un número válido que puede dividirse de nuevo por 4.
* Condiciones de retorno: Si n es igual a 1 o 4, el método devuelve True directamente, ya que estos son potencias de 4. Si en algún momento n es menor que 4 y no es 1, se retorna False, indicando que no es una potencia de cuatro.
* Control de errores: Se utiliza una excepción AssertionError para manejar el caso en el que n no pueda dividirse más sin dejar restos.

## Uso

Para utilizar este código, se debe crear una instancia de la clase Solution y llamar al método isPowerOfFour con el entero que se desea validar. El método devolverá True si el número es una potencia de cuatro, y False en caso contrario.

```python
if __name__ == "__main__":
    # Ejemplo 1
    n = 16
    sol = Solution()
    result = sol.isPowerOfFour(n)
    print(result)  # Output: True

    # Ejemplo 2
    n = 5
    result = sol.isPowerOfFour(n)
    print(result)  # Output: False

    # Ejemplo 3
    n = 1
    result = sol.isPowerOfFour(n)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Power of Four" es una buena forma de practicar la lógica de validación de potencias de un número. La implementación mediante divisiones sucesivas asegura una solución eficiente sin necesidad de bucles o recursión, lo que se ajusta al desafío planteado en el ejercicio. La solución es simple, directa y se apoya en las operaciones básicas de división para resolver el problema, lo que resulta ideal para casos donde se trabaja con bases numéricas específicas.
