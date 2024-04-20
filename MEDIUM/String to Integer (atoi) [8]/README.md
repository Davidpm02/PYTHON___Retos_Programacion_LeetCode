
# String to Integer (atoi)

## Descripción

El ejercicio "String to Integer (atoi)" consiste en implementar una función que convierte una cadena de caracteres en un entero con signo de 32 bits. Este proceso imita la función atoi encontrada en lenguajes como C/C++. La función debe manejar espacios en blanco iniciales, signos opcionales de positivo o negativo, y convertir los dígitos secuenciales en un número entero hasta que se encuentre un carácter que no sea un dígito.

## Implementación

La clase Solution contiene un método myAtoi que toma como argumento una cadena de texto s. El método procesa la cadena según las siguientes reglas:

* Ignora cualquier espacio en blanco inicial.
* Detecta y maneja el signo positivo (+) o negativo (-) que puede preceder a los números.
* Lee los caracteres continuos que son dígitos y los convierte en un entero.
* Si se lee un número que está fuera del rango de los enteros de 32 bits con signo, el número se ajusta para que permanezca dentro del rango permitido.
* Internamente, se utilizan variables para manejar el número convertido (parsed_integer), el signo del número (sign), y la cadena de dígitos convertidos (num). La conversión se maneja con cuidado para evitar errores de overflow y para garantizar que solo los caracteres válidos sean considerados.

## Uso

Para utilizar la función myAtoi, instancia la clase Solution y llama al método myAtoi con la cadena que deseas convertir. Por ejemplo:

```python
if __name__ == "__main__":
    s = "   -1234 hello"
    solution = Solution()
    result = solution.myAtoi(s)
    print(result)  # Output esperado: -1234
```

Este código instanciará la clase y llamará a la función con la cadena proporcionada, imprimiendo el resultado convertido.

## Conclusión

El ejercicio "String to Integer (atoi)" es útil para entender cómo manejar conversiones de tipos y validaciones en Python, simulando comportamientos típicos de funciones de bajo nivel en otros lenguajes de programación. Es fundamental para asegurar la robustez en la entrada y manejo de errores en aplicaciones que requieren procesamiento y conversión de datos ingresados por el usuario.
