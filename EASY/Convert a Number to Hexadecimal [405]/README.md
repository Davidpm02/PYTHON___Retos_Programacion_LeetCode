# Convert a Number to Hexadecimal

## Descripción

El ejercicio "Convert a Number to Hexadecimal" consiste en convertir un número entero de 32 bits a su representación en formato hexadecimal. Este tipo de conversión es esencial en el ámbito de la informática, particularmente para la manipulación de datos a nivel bajo, donde las representaciones en diferentes bases numéricas juegan un papel clave. Los números negativos deben representarse usando el formato de complemento a dos, mientras que los números positivos deben representarse normalmente en hexadecimal.

## Implementación

La implementación de este ejercicio se lleva a cabo en Python, utilizando una clase Solution que contiene el método toHex. Este método convierte un número entero dado en su representación hexadecimal utilizando un proceso de división iterativa entre 16 (la base del sistema hexadecimal) para extraer los dígitos hexadecimales.

### Detalles de la implementación

* Array de decimales y hexadecimales: Se utilizan arreglos que permiten mapear los restos de la división por 16 a sus correspondientes caracteres hexadecimales (0-9, A-F).
* Cálculo de complemento a dos para números negativos: Si el número es negativo, se le suma 232232 para simular el comportamiento de un número en complemento a dos, transformándolo en un valor positivo que luego puede ser convertido a hexadecimal.
* Conversión mediante división repetida: Se utiliza un bucle while para dividir el número entre 16, almacenando los restos en una lista. Posteriormente, estos restos se mapean a sus valores hexadecimales y se ordenan en la representación final.

## Uso

El código puede ser utilizado creando una instancia de la clase Solution y llamando al método toHex con el número entero que se desea convertir a hexadecimal. A continuación, se muestra un ejemplo de uso del código:

```python
if __name__ == "__main__":
    num = 26  # Número que queremos convertir a hexadecimal

    sol = Solution()
    hex_repr = sol.toHex(num)
    print(hex_repr)  # Output: "1a"
```

## Conclusión

El ejercicio "Convert a Number to Hexadecimal" proporciona una manera eficiente de convertir un número entero en su representación hexadecimal, teniendo en cuenta tanto números positivos como negativos. La implementación manual de la conversión permite entender en detalle cómo se lleva a cabo este proceso, reforzando el conocimiento sobre el sistema de numeración hexadecimal y el uso del complemento a dos para representar números negativos en sistemas binarios.
