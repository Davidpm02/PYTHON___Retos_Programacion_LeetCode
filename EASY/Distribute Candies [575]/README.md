# Distribute Candies

## Descripción

El ejercicio "Distribute Candies" plantea el desafío de ayudar a Alice, quien tiene una cantidad de caramelos representada como un array de enteros. Cada valor en el array indica el tipo de caramelo. El médico de Alice le ha recomendado comer solo la mitad del total de los caramelos para mantener su salud. Alice quiere maximizar el número de tipos diferentes de caramelos que puede comer mientras sigue esta recomendación.

El problema consiste en determinar el número máximo de tipos de caramelos que Alice puede comer bajo estas condiciones.

## Implementación

La solución está implementada en Python dentro de una clase llamada `Solution`, que contiene el método `distributeCandies`. Este método utiliza las siguientes ideas clave:

- **Uso de conjuntos:** Se utiliza un conjunto para identificar los tipos únicos de caramelos.
- **Comparación de límites:** El resultado final será el menor valor entre:
  - La cantidad de tipos únicos de caramelos.
  - La mitad del total de caramelos que Alice puede consumir.

### Detalles de la implementación

1. **Identificación de tipos únicos:** Se usa `set(candyType)` para determinar cuántos tipos únicos de caramelos están disponibles.
2. **Cálculo de la mitad de los caramelos:** `len(candyType) // 2` representa el máximo número de caramelos que Alice puede comer.
3. **Resultado:** Se devuelve el menor valor entre los tipos únicos y la cantidad máxima permitida.

## Uso

Para usar este código, se debe crear una instancia de la clase Solution y llamar al método distributeCandies pasando como argumento la lista de caramelos candyType.

```python
if __name__ == "__main__":
    candyType = [1, 1, 2, 2, 3, 3]

    sol = Solution()
    max_candy_types = sol.distributeCandies(candyType)
    print(max_candy_types)  # Output: 3
```

## Conclusión

El ejercicio "Distribute Candies" aborda un problema de optimización utilizando conceptos básicos de conjuntos y aritmética. La implementación proporciona una solución eficiente con una complejidad de tiempo de O(n)O(n), donde nn es la longitud del array. Este enfoque no solo cumple con los requisitos del problema, sino que también refuerza la comprensión de cómo manejar estructuras de datos como listas y conjuntos en Python. Es un excelente ejemplo de cómo aplicar programación básica para resolver problemas cotidianos.
