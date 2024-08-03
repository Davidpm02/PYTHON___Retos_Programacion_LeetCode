# Plus One

## Descripción

El ejercicio "Plus One" consiste en incrementar en uno un número entero representado como un array de dígitos. Cada elemento del array representa un dígito del número entero en orden de más significativo a menos significativo. El objetivo es retornar un nuevo array que represente el número incrementado en uno.

**Ejemplos:**

1. **Input:** digits = [1,2,3]  
   **Output:** [1,2,4]  
   **Explicación:** El array representa el número entero 123. Incrementar en uno da 123 + 1 = 124. Por lo tanto, el resultado es [1,2,4].

2. **Input:** digits = [4,3,2,1]  
   **Output:** [4,3,2,2]  
   **Explicación:** El array representa el número entero 4321. Incrementar en uno da 4321 + 1 = 4322. Por lo tanto, el resultado es [4,3,2,2].

3. **Input:** digits = [9]  
   **Output:** [1,0]  
   **Explicación:** El array representa el número entero 9. Incrementar en uno da 9 + 1 = 10. Por lo tanto, el resultado es [1,0].

**Restricciones:**

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- El array `digits` no contiene ceros a la izquierda.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `plusOne`. Este método se encarga de procesar el array de dígitos, convertirlo en un entero, incrementar el entero en uno y luego devolver el resultado como un nuevo array de dígitos.

### Detalles de la implementación

- **Conversión a entero:** Se convierte el array de dígitos en una cadena de texto y luego en un entero.
- **Incremento:** Se incrementa el entero en uno.
- **Conversión a array:** Se convierte el nuevo entero en una cadena de texto y luego en un array de dígitos.

## Uso

Para utilizar este código, simplemente se debe definir el array de dígitos digits, y luego crear una instancia de la clase Solution. Se llama al método plusOne con este array y se obtiene el nuevo array de dígitos que representa el número incrementado en uno.

```python
if __name__ == "__main__":
    digits = [4,3,2,1]

    sol = Solution()
    plusOne_array = sol.plusOne(digits)
    print(plusOne_array)  # Output: [4, 3, 2, 2]
```

## Conclusión

El ejercicio "Plus One" proporciona una manera eficiente de incrementar un número entero representado como un array de dígitos. Esta tarea es común en muchas aplicaciones de programación, especialmente en aquellos casos donde se trabaja con grandes números o se requiere manipulación precisa de cada dígito. La implementación presentada es directa y aprovecha las capacidades de manipulación de cadenas y números en Python para lograr el objetivo de manera clara y eficiente.
