# Shifting Letters II

## Descripción

El ejercicio "Shifting Letters II" consiste en aplicar una serie de desplazamientos a los caracteres de una cadena de letras minúsculas. Para cada desplazamiento, se define un rango de índices dentro de la cadena y la dirección del desplazamiento (adelante o atrás). El carácter de la cadena se cambia siguiendo el alfabeto, es decir, se mueve hacia el siguiente o el anterior carácter, con el alfabeto considerando un ciclo (de 'a' a 'z' o viceversa). Después de aplicar todos los desplazamientos, se debe devolver la cadena resultante.

## Implementación

La implementación del ejercicio se realiza en Python utilizando la clase `Solution` y su método `shiftingLetters`. Este método recibe como parámetros la cadena `s` y una lista `shifts`, que contiene los desplazamientos a realizar. El enfoque utilizado emplea un enfoque de diferencia acumulada para aplicar eficientemente los desplazamientos.

### Detalles de la implementación

1. **Rango de desplazamientos:** El parámetro `shifts` contiene un conjunto de desplazamientos donde cada uno se define por tres valores: `start`, `end` e `direction`. 
   - `start` es el índice de inicio del desplazamiento.
   - `end` es el índice final del desplazamiento (inclusive).
   - `direction` indica si el desplazamiento es hacia adelante (1) o hacia atrás (0).

2. **Delta para cambios acumulativos:** Utilizamos un arreglo `delta` para registrar los cambios que se deben aplicar en la cadena en las posiciones indicadas por los desplazamientos. 
   - Un incremento en `delta[start]` indica que todos los caracteres desde `start` deben moverse en la dirección especificada.
   - El valor de `delta[end + 1]` se ajusta para revertir el cambio después del índice `end`.

3. **Suma acumulada de desplazamientos:** Una vez que todos los desplazamientos se registran en el arreglo `delta`, se aplica una suma acumulativa a `delta` para obtener los desplazamientos finales de cada índice en la cadena.

4. **Aplicación de los desplazamientos:** Finalmente, se iteran los caracteres de la cadena `s`, aplicando los desplazamientos calculados y generando la nueva cadena.

### Complejidad

- El enfoque tiene una complejidad temporal de \(O(n + m)\), donde \(n\) es la longitud de la cadena `s` y \(m\) es el número de desplazamientos en `shifts`. Este enfoque es eficiente y adecuado incluso para cadenas largas y múltiples desplazamientos.

## Uso

Para utilizar este código, simplemente proporciona la cadena `s` y el arreglo `shifts` de desplazamientos. Luego, se puede llamar al método `shiftingLetters` de la clase `Solution` para obtener la cadena con los desplazamientos aplicados.

```python
if __name__ == "__main__":
    s = "abc"
    shifts = [[0,1,0],[1,2,1],[0,2,1]]

    sol = Solution()
    result = sol.shiftingLetters(s, shifts)
    print(result)  # Output: "ace"
```

## Conclusión

El ejercicio "Shifting Letters II" aborda el problema de realizar múltiples desplazamientos en una cadena de forma eficiente, utilizando un enfoque de diferencia acumulada para registrar y aplicar los cambios. Este enfoque reduce el costo de aplicar los desplazamientos de forma iterativa a cada carácter, optimizando el rendimiento para grandes entradas. Además, enseña conceptos útiles de manipulación de cadenas y técnicas para trabajar con rangos de modificaciones en un arreglo. Este método es eficiente y apropiado para resolver problemas similares con características de procesamiento masivo de datos.
