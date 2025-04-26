# Count Largest Group

## Descripción

El ejercicio "Count Largest Group" consiste en agrupar todos los números del rango [1, n] según la suma de sus dígitos y determinar cuántos grupos tienen el tamaño máximo. Esta tarea resulta útil para trabajar conceptos relacionados con el procesamiento de números, agrupaciones dinámicas y conteos basados en criterios personalizados, aspectos esenciales tanto en algoritmos de clasificación como en análisis de datos.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `countLargestGroup`. Este método organiza los números en grupos según la suma de sus dígitos y cuenta cuántos grupos alcanzan la máxima cantidad de elementos.

## Detalles de la implementación

- **Contador de grupos:** Se utiliza un objeto `Counter` para registrar cuántos números pertenecen a cada grupo de suma de dígitos.
- **Recorrido del rango:** Se itera sobre todos los números entre 1 y n, calculando la suma de los dígitos de cada número.
- **Actualización del contador:** Para cada suma de dígitos, se incrementa su contador correspondiente.
- **Determinación del tamaño máximo:** Se obtiene el tamaño del grupo más grande.
- **Conteo de grupos máximos:** Finalmente, se cuenta cuántos grupos alcanzan ese tamaño máximo y se devuelve dicho valor.

## Uso

Para utilizar este código, simplemente se debe definir el valor de n, crear una instancia de la clase `Solution`, y llamar al método `countLargestGroup` pasando el valor de n.

```python
if __name__ == "__main__":
    n = 13

    sol = Solution()
    result = sol.countLargestGroup(n)
    print(result)  # Output: 4
```

## Conclusión

El ejercicio "Count Largest Group" ofrece una manera eficiente de agrupar y analizar números basándose en un criterio dinámico, como es la suma de sus dígitos. Esta técnica de agrupación resulta útil en problemas que requieren categorizaciones rápidas y análisis de frecuencias. La solución implementada aprovecha la estructura de datos Counter para gestionar de manera óptima el conteo de grupos, proporcionando un enfoque claro y directo que refuerza habilidades importantes en el manejo de estructuras de datos y algoritmos de conteo.
