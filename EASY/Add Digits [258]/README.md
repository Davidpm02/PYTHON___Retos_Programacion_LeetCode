# Add Digits

## Descripción

El ejercicio "Add Digits" consiste en tomar un número entero y sumar sus dígitos de forma repetida hasta que el resultado sea un solo dígito. Esta tarea es interesante en el contexto de la manipulación de números y es fundamental para comprender cómo se pueden descomponer los números en sus componentes básicos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `addDigits`. Este método se encarga de convertir el número en una cadena, sumar los dígitos y repetir el proceso hasta que solo quede un dígito.

## Detalles de la implementación

- **Iteración sobre los dígitos:** Se convierte el número en una cadena para iterar sobre sus caracteres, transformándolos de nuevo en enteros para su suma.
- **Suma de dígitos:** La suma se realiza en un bucle que continúa mientras el número tenga más de un dígito.
- **Condición de finalización:** Cuando el número se reduce a un solo dígito, se retorna el resultado.

## Uso

Para utilizar este código, se debe definir un número entero num y luego crear una instancia de la clase Solution. Se llama al método addDigits con este número y se obtiene el resultado, que es el dígito final.

```python
if __name__ == "__main__":
    num = 38

    sol = Solution()
    result = sol.addDigits(num)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Add Digits" proporciona una manera eficiente de reducir un número entero a su equivalente de un solo dígito sumando sus dígitos de manera iterativa. Este proceso es útil en varias aplicaciones matemáticas y de programación, y el método implementado es claro y directo, aprovechando las capacidades integradas de Python para manipular cadenas y listas. Este enfoque no solo facilita la práctica de la manipulación de números, sino que también refuerza conceptos clave de programación y algoritmos.
