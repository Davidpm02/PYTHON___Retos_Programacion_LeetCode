# Construct Smallest Number From DI String

## Descripción

El ejercicio "Construct Smallest Number From DI String" consiste en generar la cadena numérica lexicográficamente más pequeña posible a partir de un patrón dado que contiene los caracteres 'I' (aumenta) y 'D' (disminuye). El número generado debe cumplir ciertas condiciones de orden y no puede reutilizar dígitos.

Este problema es relevante en el ámbito de la generación de permutaciones restringidas y tiene aplicaciones en algoritmos de construcción de secuencias y combinatoria.

## Implementación

La solución se implementa en Python utilizando una pila para manejar la secuencia de dígitos según las restricciones del patrón. Se emplea una clase `Solution` que contiene el método `smallestNumber`, el cual construye la cadena numérica resultante siguiendo las reglas establecidas.

### Detalles de la implementación

- **Uso de una pila**: Se utiliza una pila (`stack`) para manejar secuencias de 'D', permitiendo invertir rápidamente los valores.
- **Iteración sobre el patrón**: Se recorre el patrón y se agregan dígitos en orden, liberando la pila cuando se encuentra un 'I' o se llega al final.
- **Conversión a cadena**: Los valores almacenados en la pila se concatenan para obtener el número final.
- **Eficiencia**: El uso de estructuras de datos adecuadas permite construir la solución de manera óptima para el rango de valores permitido.

## Uso

Para utilizar este código, simplemente se debe definir un patrón `pattern` y llamar al método `smallestNumber` de la clase `Solution`. A continuación, se muestra un ejemplo de uso:

```python
if __name__ == "__main__":
    pattern = "IIIDIDDD"
    
    sol = Solution()
    result = sol.smallestNumber(pattern)
    print(result)  # Output esperado: "123549876"
```

## Conclusión

El ejercicio "Construct Smallest Number From DI String" presenta un enfoque interesante para la construcción de secuencias numéricas bajo restricciones. El uso de una pila para manejar las secuencias decrecientes proporciona una solución eficiente y fácil de entender. Este problema refuerza conceptos clave en la manipulación de estructuras de datos y algoritmos de ordenación parcial.
