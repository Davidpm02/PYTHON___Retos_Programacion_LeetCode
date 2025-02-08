# Check if One String Swap Can Make Strings Equal

## Descripción

El ejercicio "Check if One String Swap Can Make Strings Equal" consiste en determinar si es posible hacer que dos cadenas de texto sean iguales mediante un único intercambio de caracteres dentro de una de las cadenas. Este tipo de operación es útil en la validación de datos y en algoritmos de manipulación de cadenas en procesamiento de texto.

## Implementación

La implementación se desarrolla en Python utilizando una clase `Solution` que contiene el método `areAlmostEqual`. Este método verifica si se pueden igualar las dos cadenas con un solo intercambio de caracteres.

## Detalles de la implementación

- **Verificación de frecuencias:** Se utiliza `Counter` para asegurar que ambas cadenas tienen los mismos caracteres en la misma cantidad.
- **Comparación de caracteres diferentes:** Se recorre cada carácter de ambas cadenas y se cuentan cuántas posiciones contienen caracteres distintos.
- **Condición de igualdad:** Se consideran iguales si no hay diferencias o si existen exactamente dos caracteres distintos, ya que estos podrían intercambiarse para hacer coincidir ambas cadenas.

## Uso

Para utilizar este código, se deben definir las cadenas de texto `s1` y `s2`, y luego crear una instancia de la clase `Solution`. Se llama al método `areAlmostEqual` con estas cadenas y se obtiene el resultado booleano correspondiente.

```python
if __name__ == "__main__":
    s1 = "bank"
    s2 = "kanb"
    
    sol = Solution()
    result = sol.areAlmostEqual(s1, s2)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Check if One String Swap Can Make Strings Equal" permite explorar la manipulación de cadenas y la validación de igualdad con una restricción específica. La solución implementada es eficiente y directa, asegurando que la comparación se realice en un tiempo óptimo. Este tipo de problema es relevante en aplicaciones que requieren validación de datos o procesamiento de texto con restricciones mínimas de modificación.
