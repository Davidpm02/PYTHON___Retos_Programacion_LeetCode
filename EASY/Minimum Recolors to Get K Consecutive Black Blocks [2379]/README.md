# Minimum Recolors to Get K Consecutive Black Blocks

## Descripción

El ejercicio "Minimum Recolors to Get K Consecutive Black Blocks" consiste en determinar el número mínimo de operaciones necesarias para obtener al menos "k" bloques negros consecutivos dentro de una cadena de caracteres compuesta por los caracteres 'W' (blanco) y 'B' (negro). En cada operación, es posible cambiar un bloque blanco ('W') a negro ('B').

El objetivo es encontrar la mínima cantidad de cambios necesarios para que, en algún punto de la cadena, haya una secuencia de "k" bloques negros consecutivos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `minimumRecolors`. Este método examina todas las posibles subcadenas de longitud "k" dentro de "blocks" y determina la cantidad mínima de cambios requeridos para convertir cada subcadena en una secuencia completamente negra.

## Detalles de la implementación

- **Recorrer todas las posibles subcadenas de longitud "k"**: Se analiza cada segmento contiguo de "k" caracteres en la cadena "blocks".
- **Contar los bloques negros ('B') en cada subcadena**: Se obtiene el número de bloques negros ya existentes en la subcadena.
- **Calcular los cambios necesarios**: Si el número de bloques negros es menor que "k", se determina cuántos bloques blancos ('W') deben cambiarse a negros ('B') para lograr la secuencia deseada.
- **Devolver el mínimo de cambios**: Se registra el mínimo número de cambios requeridos entre todas las subcadenas evaluadas.

## Uso

Para utilizar este código, se debe definir la cadena de bloques y el valor de "k", luego crear una instancia de la clase `Solution` y llamar al método `minimumRecolors`.

```python
if __name__ == "__main__":
    blocks = "WBBWWBBWBW"
    k = 7
    
    sol = Solution()
    min_operations = sol.minimumRecolors(blocks, k)
    print(min_operations)  # Output: 3
```

## Conclusión

El ejercicio "Minimum Recolors to Get K Consecutive Black Blocks" es un problema que se puede resolver de manera eficiente evaluando todas las subcadenas de longitud "k" en la cadena de entrada. El método implementado encuentra la solución óptima minimizando el número de cambios requeridos.

Este enfoque aprovecha la técnica de ventanas deslizantes para evaluar eficientemente las subcadenas sin recalcular toda la información en cada iteración, optimizando así el rendimiento del algoritmo. La solución es adecuada para cadenas de longitud moderada (hasta 100 caracteres, según las restricciones del problema).
