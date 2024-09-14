# Happy Number

## Descripción

El ejercicio "Happy Number" tiene como objetivo determinar si un número dado es un número feliz. Un número se define como feliz si, al reemplazarlo repetidamente por la suma de los cuadrados de sus dígitos, eventualmente se llega al número 1. Si el proceso cae en un ciclo que no incluye el 1, el número no es feliz. El desafío es diseñar un algoritmo que determine si un número es feliz o no.

Un número feliz es significativo en la teoría de números y en ciertos problemas matemáticos, ya que describe un comportamiento cíclico interesante y permite el análisis de secuencias generadas por sumas de cuadrados de dígitos.

## Implementación

El algoritmo está implementado en Python en una clase llamada `Solution`, la cual contiene el método `isHappy`. Este método recibe un número entero `n` y evalúa si es un número feliz.

### Detalles de la implementación

1. **Suma de cuadrados de los dígitos**: Se obtiene cada dígito del número y se calcula el cuadrado de cada uno de ellos.
2. **Ciclo de procesamiento**: Se repite el proceso de reemplazar el número por la suma de los cuadrados de sus dígitos hasta que el número sea igual a 1 o caiga en un ciclo.
3. **Detección de ciclos**: Se lleva un registro de todas las combinaciones vistas de números para detectar si el proceso entra en un ciclo infinito. Si se encuentra un ciclo, el número no es feliz.
4. **Determinación del resultado**: Si en algún punto el resultado es 1, el número es feliz. De lo contrario, no lo es.

### Uso

Para utilizar este código, simplemente se debe crear una instancia de la clase Solution y llamar al método isHappy con el número que se desea verificar. El método devolverá True si el número es feliz, y False si no lo es.

### Ejemplo de uso

```python
if __name__ == "__main__":
    sol = Solution()
    
    # Ejemplo 1
    n = 19
    print(sol.isHappy(n))  # Output: True

    # Ejemplo 2
    n = 2
    print(sol.isHappy(n))  # Output: False

```

En el ejemplo anterior, el número 19 es feliz, mientras que el número 2 no lo es.

## Conclusión

El ejercicio "Happy Number" es un buen ejemplo de cómo utilizar estructuras de control, listas y algoritmos de detección de ciclos en Python para resolver problemas numéricos. Este tipo de algoritmos tiene aplicaciones en la teoría de números y en problemas relacionados con secuencias y patrones. La solución presentada es eficiente y clara, detectando rápidamente si un número es feliz o si entra en un ciclo sin alcanzar el valor 1.
