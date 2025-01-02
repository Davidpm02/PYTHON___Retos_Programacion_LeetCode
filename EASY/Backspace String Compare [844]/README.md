# Backspace String Compare

## Descripción

El ejercicio "Backspace String Compare" determina si dos cadenas de texto son iguales cuando se procesan a través de un editor de texto simulado. En este editor, el carácter `#` actúa como un retroceso (backspace), eliminando el carácter anterior en la cadena si existe. Esta tarea es útil en la simulación de entradas en tiempo real y sistemas de procesamiento de texto.

### Definición del problema

- Las cadenas `s` y `t` contienen únicamente letras minúsculas del alfabeto inglés y el carácter `#`.
- El carácter `#` elimina el carácter inmediatamente anterior en la cadena. Si no hay caracteres previos, no tiene efecto.

El método devuelve `True` si ambas cadenas resultantes son idénticas después del procesamiento, de lo contrario, retorna `False`.

## Implementación

La solución implementa una clase `Solution` con el método `backspaceCompare`. Este método procesa las cadenas para aplicar el efecto del carácter `#` y luego compara los resultados.

### Detalles de la implementación

1. **Conversión a listas:**
   - Las cadenas se convierten en listas de caracteres para facilitar la manipulación durante el procesamiento.

2. **Procesamiento del carácter `#`:**
   - Se recorren las listas caracter por caracter:
     - Si se encuentra un `#`, se elimina el carácter anterior (si existe) y el `#` actual.
     - Si el `#` está al inicio de la lista, se elimina directamente.
   - Se utiliza un bucle hasta que se procesen todos los caracteres.

3. **Comparación final:**
   - Las cadenas resultantes, reconstruidas a partir de las listas procesadas, se comparan para determinar si son iguales.

## Conclusión

El ejercicio "Backspace String Compare" proporciona una solución eficiente para procesar y comparar cadenas aplicando una lógica de edición. La implementación refuerza conceptos de manipulación de listas y simulación de sistemas, destacando la importancia de manejar operaciones condicionadas sobre estructuras dinámicas de datos. Este enfoque es útil para resolver problemas similares en procesamiento de texto y análisis de entradas en tiempo real.
