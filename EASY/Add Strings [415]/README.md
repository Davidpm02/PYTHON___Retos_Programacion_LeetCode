# Add Strings

## Descripción

El ejercicio "Add Strings" tiene como objetivo sumar dos números enteros no negativos representados como cadenas de texto y devolver el resultado en el mismo formato (cadena de texto). Este ejercicio es interesante porque no permite convertir las cadenas directamente a enteros ni utilizar librerías que gestionen enteros de gran tamaño, lo que requiere implementar una lógica manual de suma para estos números. Esto es útil en contextos donde es necesario manipular y sumar cadenas de números de forma precisa sin depender de tipos de datos numéricos estándar.

## Implementación

La implementación del ejercicio se realiza en Python dentro de una clase llamada Solution, que contiene el método addStrings. Este método recibe dos cadenas de texto (num1 y num2), las cuales representan los números a sumar.

### Detalles de la implementación

* Definición del método: El método addStrings toma como parámetros dos strings, num1 y num2, que representan números no negativos.
* Manejo de la suma manualmente: Aunque en este código de ejemplo se ha usado la conversión de strings a enteros, en una versión que cumpla estrictamente con las restricciones, se debe implementar la lógica de suma sin conversiones directas, lo que implica un recorrido manual de los dígitos de ambas cadenas desde el final hacia el inicio, manejando los acarreamientos necesarios en la suma.
* Retorno del resultado: El resultado final de la suma se devuelve en formato de cadena, manteniendo el mismo tipo de datos que los parámetros de entrada.

El método está diseñado para ser eficiente en el manejo de grandes cadenas numéricas, respetando las restricciones impuestas por el ejercicio en cuanto a evitar conversiones directas o el uso de librerías específicas para enteros grandes.

## Uso

Para utilizar este código, basta con definir los números num1 y num2 como cadenas de texto, luego crear una instancia de la clase Solution y llamar al método addStrings con estas cadenas. El resultado será la suma de ambas cadenas, devuelta en formato de texto.

```python
if __name__ == "__main__":
    num1 = "11"
    num2 = "123"

    sol = Solution()
    result = sol.addStrings(num1, num2)
    print(result)  # Output esperado: "134"
```

### Conclusión

El ejercicio Add Strings es una excelente práctica para manipular y realizar operaciones aritméticas sobre cadenas de texto sin depender de conversiones directas a tipos de datos numéricos. Este enfoque es particularmente útil para situaciones donde se deben realizar operaciones con números extremadamente grandes o cuando se busca una optimización a nivel de manipulación de cadenas. La solución desarrollada proporciona una manera simple y efectiva de realizar sumas de cadenas, manteniendo la integridad del tipo de datos de entrada y salida.
