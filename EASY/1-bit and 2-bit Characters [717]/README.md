# 1-bit and 2-bit Characters

## Descripción

El ejercicio "1-bit and 2-bit Characters" consiste en determinar si el último carácter de un arreglo binario es un carácter representado por un bit (`0`) o por dos bits (`10` o `11`).

Se da una matriz binaria `bits` que siempre termina en `0`, y el objetivo es devolver `true` si el último carácter debe ser un carácter de un bit. Este problema es relevante en el ámbito de decodificación binaria y compresión de datos.

## Implementación

La solución se desarrolla en Python, utilizando una clase `Solution` que contiene el método `isOneBitCharacter`. Este método verifica la estructura de la cadena binaria iterando a través de ella y decodificando en función de las reglas establecidas para caracteres de un bit y de dos bits.

### Detalles de la implementación

- **Copia del arreglo original:** Se realiza una copia del arreglo para trabajar de forma segura con los elementos mientras se manipula el índice.
- **Decodificación de caracteres:** La lógica distingue entre un bit (`0`) y dos bits (`10` o `11`) avanzando en el arreglo según corresponda.
- **Validación final:** El proceso verifica al término del arreglo si el último bit decodificado pertenece a un carácter de un bit.

## Uso

El código es directamente funcional al instanciar la clase Solution y utilizar el método isOneBitCharacter pasando como parámetro un arreglo binario bits. La función devuelve un valor booleano indicando si el último carácter del arreglo es un carácter de un bit.

```python
if __name__ == "__main__":
    bits = [1, 0, 0]
    solution = Solution()
    print(solution.isOneBitCharacter(bits))  # Devuelve: True
```

## Conclusión

El ejercicio "1-bit and 2-bit Characters" ofrece una forma práctica de analizar y decodificar cadenas binarias bajo restricciones específicas. Esta solución aprovecha estructuras iterativas simples y un enfoque lógico para determinar el tipo del último carácter en el arreglo. Esto refuerza conceptos de iteración, manipulación de índices y operaciones lógicas fundamentales en programación con datos binarios.
