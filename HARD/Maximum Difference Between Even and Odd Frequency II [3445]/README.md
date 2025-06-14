# Maximum Difference Between Even and Odd Frequency II

## Descripción

El ejercicio **"Maximum Difference Between Even and Odd Frequency II"** consiste en encontrar la **diferencia máxima entre las frecuencias** de dos caracteres en cualquier **subcadena del string `s` de tamaño al menos `k`**, bajo las siguientes condiciones:

- La frecuencia del primer carácter (`a`) debe ser **impar**.
- La frecuencia del segundo carácter (`b`) debe ser **par**.

Este tipo de problema requiere una comprensión sólida del manejo eficiente de **frecuencias de caracteres en rangos** (substrings) y del uso de **estructuras de datos avanzadas**, lo que lo convierte en un excelente ejercicio para mejorar la habilidad en programación algorítmica, especialmente en la optimización de soluciones sobre cadenas de texto.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con el método `maxDifference`. Este método busca, entre todas las posibles subcadenas de `s` que tengan al menos longitud `k`, la combinación `(a, b)` tal que se maximice `freq[a] - freq[b]`, cumpliendo las condiciones de paridad impuestas.

### Detalles de la implementación

- **Conteo de prefijos:** Se construyen arreglos de conteo acumulado para cada carácter posible ('0' a '4'), lo que permite calcular la frecuencia de cualquier carácter en un rango en tiempo constante.
- **Substrings válidos:** Se consideran todas las combinaciones de caracteres posibles como candidatos `(a, b)` y se analiza la diferencia de sus frecuencias en cada subcadena.
- **Condiciones de paridad:** Para asegurar que `freq[a]` sea impar y `freq[b]` sea par, se mantiene un registro de la paridad de las frecuencias prefijadas y se utiliza como criterio de filtrado.
- **Uso de Segment Trees:** Se utilizan árboles de segmentos (uno por cada combinación de paridades posibles) para mantener los valores mínimos de diferencia parcial entre frecuencias y poder consultar en tiempo logarítmico el valor mínimo anterior a la posición actual.
- **Optimización:** La implementación está altamente optimizada para manejar strings de hasta `3 * 10^4` caracteres, gracias a la eficiencia del cálculo de prefijos y las consultas sobre árboles de segmento.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution`, y llamar al método `maxDifference` pasando el string `s` y el entero `k` como argumentos.

```python
if __name__ == "__main__":
    s = "1122211"
    k = 3

    sol = Solution()
    resultado = sol.maxDifference(s, k)
    print(resultado)  # Output: 1
```

## Conclusión

El ejercicio "Maximum Difference Between Even and Odd Frequency II" ofrece una combinación desafiante de análisis de cadenas, condiciones de paridad y optimización de consultas. La solución propuesta aprovecha técnicas avanzadas como prefijos acumulados, segment trees y una lógica cuidadosa de combinatoria de caracteres, lo que permite alcanzar una solución eficiente incluso en el caso de entradas de gran tamaño. Este problema refuerza conceptos clave en algoritmos sobre strings, manipulación de frecuencias y estructuras de datos avanzadas aplicadas al análisis de subcadenas.
