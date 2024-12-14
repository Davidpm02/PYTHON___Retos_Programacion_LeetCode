# Binary Numbers with Alternating Bits

## Descripción

El ejercicio **"Binary Numbers with Alternating Bits"** consiste en verificar si un número entero positivo, representado en formato binario, tiene bits alternantes. Esto implica que cada bit adyacente en la representación binaria debe tener un valor diferente al anterior.

### Ejemplos

1. **Input:** `n = 5`
   - **Output:** `true`
   - **Explicación:** La representación binaria de 5 es `101`, donde los bits son alternantes.

2. **Input:** `n = 7`
   - **Output:** `false`
   - **Explicación:** La representación binaria de 7 es `111`, donde los bits no alternan.

3. **Input:** `n = 11`
   - **Output:** `false`
   - **Explicación:** La representación binaria de 11 es `1011`, donde los bits finales no alternan.

### Restricciones
- `1 <= n <= 2^{31} - 1`

Este problema combina conceptos de manipulación de cadenas y control de flujo para analizar patrones en representaciones binarias, siendo útil en aplicaciones relacionadas con sistemas digitales y algoritmos de bajo nivel.

## Implementación

La solución utiliza una clase `Solution` que implementa el método `hasAlternatingBits`, el cual realiza las siguientes operaciones:

- **Conversión a binario:** El número entero `n` se convierte a su representación binaria utilizando `bin(n)`.
- **Iteración sobre los bits:** Se recorre la cadena binaria y se compara cada bit con el anterior para asegurarse de que no coincidan.
- **Detección de patrones:** Si algún par de bits consecutivos es igual, el método retorna `False`.
- **Resultado final:** Si se recorren todos los bits sin problemas, se retorna `True`.

### Código

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Comprueba si la representación en binario para un
        entero dado está compuesta, en su totalidad, por bits
        alternantes.

        params:
            n (int): Número entero a verificar.
        
        returns:
            bool: True si los bits son alternantes, False en caso contrario.
        """

        for idx, bit in enumerate(str(bin(n))):
            try:
                if idx != 0:  # Saltar el prefijo '0b'
                    assert (bit != str(bin(n))[idx - 1])
            except AssertionError:
                return False
        return True
```

## Uso

Para utilizar esta solución, basta con definir un entero `n`, crear una instancia de la clase `Solution`, y luego llamar al método `hasAlternatingBits`. A continuación, se muestra un ejemplo completo:

```python
if __name__ == "__main__":
    n = 5  # Número a verificar

    sol = Solution()
    result = sol.hasAlternatingBits(n)
    print(result)  # Output: True
```

### Ejemplos adicionales

1. **Input:** `n = 10`
   - Representación binaria: `1010`
   - **Output:** `true`

2. **Input:** `n = 14`
   - Representación binaria: `1110`
   - **Output:** `false`

## Conclusión

El ejercicio **"Binary Numbers with Alternating Bits"** es una práctica ideal para trabajar con conceptos de representación binaria y patrones de bits. Este tipo de problemas es especialmente relevante en áreas como procesamiento digital y diseño de circuitos, donde la verificación de patrones binarios es común. La solución presentada es simple, directa y aprovecha las funcionalidades integradas de Python para manipular cadenas y controlar el flujo del programa.
