# Clear Digits

## Descripción

El ejercicio "Clear Digits" consiste en procesar una cadena de texto y eliminar todos los dígitos junto con el caracter más cercano situado a su izquierda. Este proceso se realiza de manera iterativa hasta que no queden dígitos en la cadena.

Este tipo de manipulación de cadenas es útil en diversas aplicaciones, como el procesamiento de datos de texto, la limpieza de entradas de usuario y la normalización de datos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `clearDigits`. Este método lleva a cabo la eliminación de dígitos y caracteres asociados de manera eficiente.

### Detalles de la implementación

- **Identificación de dígitos**: Se marca la posición de todos los dígitos en la cadena de entrada.
- **Eliminación iterativa**: Se elimina el primer dígito encontrado junto con el primer caracter no numérico a su izquierda.
- **Generación del resultado**: Se reconstruye la cadena sin los caracteres eliminados y se devuelve como resultado final.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `clearDigits` pasando la cadena de entrada. El método devolverá la cadena resultante después de haber eliminado todos los dígitos y los caracteres correspondientes.

```python
if __name__ == "__main__":
    s = "cb34"
    sol = Solution()
    result = sol.clearDigits(s)
    print(result)  # Output: ""
```

## Conclusión

El ejercicio "Clear Digits" proporciona una solución efectiva para eliminar dígitos y sus caracteres asociados de una cadena de texto. Su implementación garantiza un procesamiento correcto y eficiente, aprovechando estructuras de datos apropiadas para recorrer la cadena y modificarla según los requisitos establecidos.

Este tipo de problema es común en tareas de limpieza y preprocesamiento de datos en entornos de manipulación de texto, procesamiento de lenguajes naturales y sistemas de validación de entradas de usuario.
