# Check if a Parentheses String Can Be Valid

## Descripción

El ejercicio **"Check if a Parentheses String Can Be Valid"** tiene como objetivo determinar si una cadena de paréntesis puede modificarse para formar una secuencia válida, dadas ciertas restricciones. Una cadena de paréntesis es válida si cumple las siguientes condiciones:

1. La cadena vacía es válida.
2. Una cadena formada como `(A)` es válida si `A` es válida.
3. Una cadena formada como `AB` es válida si `A` y `B` son válidas.

Se proporciona una cadena `s` y una cadena binaria `locked`, donde:

- Si `locked[i]` es '1', no se puede modificar el carácter `s[i]`.
- Si `locked[i]` es '0', se puede modificar el carácter `s[i]` a '(' o ')'.

El desafío consiste en devolver `true` si es posible transformar la cadena `s` en una secuencia válida de paréntesis bajo las restricciones dadas, y `false` en caso contrario.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `canBeValid`. Este método realiza lo siguiente:

1. **Verificación inicial:** Comprueba si la longitud de la cadena `s` es par, ya que una cadena impar no puede ser válida.
2. **Recorrido hacia adelante:** Evalúa de izquierda a derecha si el número de paréntesis abiertos no excede el límite permitido, ni se desequilibra en ningún punto.
3. **Recorrido hacia atrás:** Evalúa de derecha a izquierda asegurando que el número de paréntesis cerrados sigue siendo válido.
4. **Resultado final:** Si ambas comprobaciones son exitosas, la cadena es válida.

La implementación optimiza el proceso evitando modificaciones innecesarias y evaluando únicamente las posiciones requeridas.

## Uso

Para utilizar este código, define las cadenas `s` y `locked` con los valores deseados. Luego, crea una instancia de la clase `Solution` y utiliza el método `canBeValid` para verificar la validez de la cadena:

```python
if __name__ == "__main__":
    s = "))()))"
    locked = "010100"

    sol = Solution()
    is_valid = sol.canBeValid(s, locked)
    print(is_valid)  # Debería imprimir True o False según el caso
```

## Conclusión

El ejercicio "Check if a Parentheses String Can Be Valid" permite explorar algoritmos relacionados con el manejo de estructuras de datos dinámicas y el uso de recorridos duales para validar cadenas. La solución se basa en un análisis eficiente de los caracteres bloqueados y desbloqueados, optimizando los cálculos mediante dos recorridos de tiempo lineal. Este enfoque es útil no solo para problemas específicos de validación de paréntesis, sino también para conceptos más generales relacionados con secuencias restringidas y lógica booleana.
