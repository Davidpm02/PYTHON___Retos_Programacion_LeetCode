# Minimum Equal Sum of Two Arrays After Replacing Zeros

## Descripción

El ejercicio "Minimum Equal Sum of Two Arrays After Replacing Zeros" plantea el siguiente reto: dadas dos listas de enteros positivos (que pueden contener ceros), se deben reemplazar todos los ceros por enteros estrictamente positivos de forma que la suma total de ambas listas sea igual. El objetivo es encontrar la suma mínima posible que cumpla esta condición. En caso de que no sea posible lograr dicha igualdad, se debe retornar -1.

Este problema aborda conceptos clave como el análisis de casos condicionales, la optimización de operaciones aritméticas bajo restricciones específicas y la gestión eficiente del conteo y la suma de elementos en estructuras de datos.

## Implementación

La implementación se realiza en Python a través de una clase `Solution` que contiene el método `minSum`. Este método identifica la mínima suma posible para igualar el total de ambas listas después de sustituir los ceros por enteros positivos.

Se consideran distintos escenarios según la cantidad de ceros presentes en cada lista, y se aplica una lógica condicional para determinar si es posible igualar las sumas con los valores mínimos requeridos.

## Detalles de la implementación

- **Cálculo de suma y conteo de ceros:** Se utiliza `sum()` para calcular la suma de elementos y `count(0)` para identificar cuántos ceros hay en cada lista.
- **Caso base:** Si ambas listas no contienen ceros, simplemente se compara la igualdad entre las sumas originales.
- **Casos parciales:** Si solo una de las dos listas contiene ceros, se verifica si es posible alcanzar la suma de la otra lista utilizando valores mínimos posibles (al menos 1 por cada cero).
- **Caso general:** Si ambas listas contienen ceros, se calcula el mínimo valor objetivo que iguala ambas sumas, asegurando que cada cero se reemplace con al menos un valor 1. Este valor se obtiene como el máximo entre `suma + número de ceros` de cada lista.

## Uso

Para utilizar este código, se deben definir las listas `nums1` y `nums2`, y luego crear una instancia de la clase `Solution`. Se llama al método `minSum` con estas listas para obtener el resultado:

```python
if __name__ == "__main__":
    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]

    sol = Solution()
    result = sol.minSum(nums1, nums2)
    print(result)  # Output: 12
```

## Conclusión

El ejercicio "Minimum Equal Sum of Two Arrays After Replacing Zeros" representa una excelente práctica para aplicar lógica condicional y aritmética con restricciones, además de fomentar una mentalidad analítica orientada a optimización. La solución propuesta evita enfoques de fuerza bruta al evaluar de forma eficiente los límites mínimos requeridos para cumplir la condición, logrando así una implementación escalable que se adapta a entradas de gran tamaño. Esta técnica es útil tanto para entrevistas técnicas como para reforzar fundamentos esenciales de resolución de problemas en estructuras de datos.
