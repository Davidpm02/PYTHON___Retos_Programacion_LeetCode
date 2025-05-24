# Type of Triangle

## Descripción

El ejercicio "Type of Triangle" consiste en determinar qué tipo de triángulo se puede formar a partir de un array de tres enteros, donde cada valor representa la longitud de un lado del triángulo. Este tipo de problema permite reforzar conceptos fundamentales de geometría y lógica condicional, evaluando la validez de la figura geométrica y clasificándola como:

- **Equilátero**: todos los lados son iguales.
- **Isósceles**: exactamente dos lados son iguales.
- **Escaleno**: todos los lados son diferentes.
- **Ninguno**: los valores no cumplen la desigualdad triangular, por lo que no forman un triángulo válido.

## Implementación

La solución se implementa en Python dentro de una clase llamada `Solution`, que contiene el método `triangleType`. Este método recibe una lista de tres enteros y retorna un string con el tipo de triángulo que se puede formar o `"none"` si no es posible construir uno.

## Detalles de la implementación

- **Validación geométrica**: Se verifica la validez del triángulo usando la desigualdad triangular, que establece que la suma de las longitudes de dos lados cualesquiera debe ser mayor que la longitud del tercer lado.
- **Clasificación del triángulo**: Una vez validado que se puede formar un triángulo, se utiliza un conjunto (`set`) para contar la cantidad de lados únicos. A partir del número de elementos únicos, se infiere el tipo de triángulo:
  - 1 elemento → equilátero.
  - 2 elementos → isósceles.
  - 3 elementos → escaleno.

## Uso

Para utilizar este código, se debe definir una lista de tres enteros que representen las longitudes de los lados del triángulo. Luego, se crea una instancia de la clase `Solution` y se llama al método `triangleType`, pasando como argumento la lista de longitudes. El resultado será una cadena de texto que describe el tipo de triángulo que se puede formar.

```python
if __name__ == "__main__":
    nums = [3, 4, 5]

    sol = Solution()
    triangle = sol.triangleType(nums)
    print(triangle)  # Output: "scalene"
```

## Conclusión

El ejercicio "Type of Triangle" representa una forma práctica de aplicar principios básicos de geometría y estructuras de datos en Python. La solución propuesta permite clasificar correctamente triángulos a partir de sus lados, validando previamente su existencia con la desigualdad triangular. Este tipo de problemas es común en entrevistas técnicas y tareas de programación básica, fomentando el pensamiento lógico y la correcta implementación de condiciones compuestas.
