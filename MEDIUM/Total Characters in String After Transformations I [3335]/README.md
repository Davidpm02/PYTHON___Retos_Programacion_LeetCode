# Total Characters in String After Transformations I

## Descripción

El ejercicio "Total Characters in String After Transformations I" consiste en calcular la longitud final de una cadena después de aplicar una serie de transformaciones definidas sobre sus caracteres. Cada transformación sigue estas reglas:

- Si el carácter es `'z'`, se reemplaza por la cadena `"ab"`.
- Cualquier otro carácter se reemplaza por el siguiente carácter en el alfabeto. Por ejemplo, `'a'` se convierte en `'b'`, `'b'` en `'c'`, y así sucesivamente.

El objetivo es determinar cuántos caracteres tendrá la cadena resultante tras aplicar exactamente `t` transformaciones sobre la cadena original `s`. Dado que el tamaño de la cadena puede crecer exponencialmente, se requiere devolver el resultado módulo \(10^9 + 7\).

Este tipo de problema es interesante desde el punto de vista computacional, ya que pone a prueba la eficiencia algorítmica en el manejo de grandes volúmenes de datos y transformaciones iterativas.

## Implementación

La solución se implementa en Python dentro de una clase `Solution`, que expone el método `lengthAfterTransformations`. Esta función evita transformar explícitamente la cadena en cada iteración, lo que sería computacionalmente inviable para grandes valores de `t`. En su lugar, utiliza una estrategia basada en conteo de frecuencias para representar cuántas veces aparece cada letra, y cómo estas frecuencias se actualizan en cada transformación.

## Detalles de la implementación

- **Inicialización de frecuencias:** Se utiliza un array de tamaño 26 (una posición por cada letra del alfabeto en minúscula) para contar la frecuencia de cada letra en la cadena inicial.
- **Transformaciones iterativas:** 
  - Para cada transformación:
    - Los caracteres de `'a'` a `'y'` se trasladan a su siguiente carácter.
    - El carácter `'z'` se transforma en dos nuevos caracteres: `'a'` y `'b'`.
- **Eficiencia:** Esta técnica evita construir y almacenar cadenas intermedias, lo que permite manejar entradas de tamaño hasta \(10^5\) tanto en longitud de cadena como en número de transformaciones.
- **Cálculo final:** Se suman todas las frecuencias tras las `t` transformaciones, y se devuelve el resultado módulo \(10^9 + 7\).

## Uso

Para utilizar este código, basta con definir la cadena original `s` y el número de transformaciones `t`. Luego se crea una instancia de la clase `Solution` y se llama al método `lengthAfterTransformations`.

```python
if __name__ == "__main__":
    s = "abcyy"
    t = 2

    sol = Solution()
    result = sol.lengthAfterTransformations(s, t)
    print(result)  # Output: 7
```

## Conclusión

El ejercicio "Total Characters in String After Transformations I" proporciona una solución eficiente al problema de crecimiento exponencial de cadenas tras múltiples transformaciones. Emplear un enfoque basado en conteo de frecuencias evita la manipulación directa de la cadena, reduciendo la complejidad computacional de manera significativa. Este ejercicio es ideal para comprender cómo optimizar operaciones iterativas y manejar grandes volúmenes de datos sin comprometer el rendimiento, especialmente dentro del contexto de restricciones algorítmicas comunes en problemas de programación competitiva.
