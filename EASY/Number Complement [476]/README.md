# Number Complement

## Descripción

El ejercicio "Number Complement" se enfoca en hallar el complemento de un número entero en su representación binaria. El complemento de un número se obtiene invirtiendo todos los bits de su representación binaria: los bits '1' se transforman en '0' y los bits '0' en '1'. Por ejemplo, el entero 5 tiene la representación binaria `101`, y su complemento sería `010`, que corresponde al entero 2.

Esta operación es fundamental en teoría de la información y sistemas digitales, ya que los complementos son ampliamente utilizados en la aritmética binaria y la codificación de datos.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `findComplement`. Este método toma un número entero como argumento y devuelve su complemento. La solución incluye los siguientes pasos principales:

- **Conversión a binario:** Se convierte el número dado a su representación binaria en formato de cadena.
- **Inversión de bits:** Se recorre cada bit de la representación binaria; los bits '1' se cambian por '0' y viceversa.
- **Conversión a entero:** La cadena de bits invertida se convierte de nuevo a un entero, que representa el complemento.

### Detalles de la implementación

- **Representación binaria:** La función `format()` se utiliza para convertir el número a binario, sin agregar ceros iniciales.
- **Inversión de bits:** Se emplea una lista por comprensión para recorrer cada bit de la cadena y alternarlo.
- **Resultado:** La cadena binaria resultante se convierte a entero con `int(..., 2)` para retornar el complemento.

## Uso

Para utilizar esta implementación, basta con definir un número entero y crear una instancia de la clase Solution. Luego, llamamos al método findComplement pasando el número deseado, obteniendo así el complemento del entero en formato decimal.

```python
if __name__ == "__main__":
    num = 5

    sol = Solution()
    complement = sol.findComplement(num)
    print(complement)  # Output: 2
```

En este ejemplo, el entero 5 tiene una representación binaria de 101, y su complemento es 010, que corresponde al entero 2.

## Conclusión

El ejercicio "Number Complement" proporciona una forma eficiente de calcular el complemento de un número en su representación binaria, una operación frecuente en el procesamiento binario y en sistemas digitales. Este enfoque permite manipular fácilmente las representaciones binarias y emplea operaciones eficientes en Python para procesar y convertir entre representaciones binarias y decimales. Además, refuerza conceptos importantes sobre aritmética de bits y manipulación de datos binarios.
