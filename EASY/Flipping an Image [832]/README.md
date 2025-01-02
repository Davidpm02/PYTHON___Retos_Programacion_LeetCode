# Flipping an Image

## Descripción

El ejercicio "Flipping an Image" tiene como objetivo transformar una matriz binaria siguiendo dos pasos principales:

1. **Voltear horizontalmente cada fila**: Revertir el orden de los elementos en cada fila de la matriz.
   - Ejemplo: La fila `[1,1,0]` se convierte en `[0,1,1]`.

2. **Invertir cada elemento de la matriz**: Cambiar cada `0` por `1` y cada `1` por `0`.
   - Ejemplo: La fila `[0,1,1]` se convierte en `[1,0,0]`.

La matriz transformada se devuelve como resultado.

Este problema combina conceptos de manipulación de matrices y transformación de datos binarios, haciendo énfasis en el trabajo con estructuras anidadas.

## Implementación

La implementación se realiza utilizando una clase llamada `Solution`, que contiene el método `flipAndInvertImage`. Este método toma como entrada una matriz binaria y produce la matriz transformada aplicando los pasos mencionados.

### Detalles de la implementación

- **Volteo horizontal**: Se utiliza la operación de inversión (`[::-1]`) para revertir cada fila de la matriz.
- **Inversión binaria**: Se aplica la negación lógica (`not`) para cambiar cada bit binario, seguido de una conversión a entero para garantizar la representación correcta.
- **Procesamiento iterativo**: Cada fila de la matriz se procesa de manera independiente.

La implementación garantiza que las transformaciones sean eficientes y se mantenga la simplicidad en el diseño del código.

## Conclusión

El ejercicio "Flipping an Image" combina la manipulación de matrices con operaciones binarias para transformar una estructura bidimensional. Esta solución es eficiente y emplea prácticas recomendadas para iterar y modificar estructuras anidadas en Python. Resolver este problema ayuda a reforzar habilidades importantes para trabajar con datos matriciales y algoritmos de procesamiento lógico.
