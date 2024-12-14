# Biggest Single Number

## Descripción

El ejercicio "Biggest Single Number" consiste en encontrar el mayor número que aparece exactamente una vez dentro de una tabla denominada MyNumbers. Este tipo de problema es común en análisis de datos, donde identificar elementos únicos tiene aplicaciones prácticas, como la deduplicación de registros o el filtrado de información.

### Tabla MyNumbers

La tabla contiene una columna num que incluye una lista de números enteros, los cuales pueden contener duplicados. El objetivo es identificar cuál es el mayor número que aparece una única vez. Si no hay números únicos, el resultado será null.

**Ejemplo 1:**

```bash
+-----+
| num |
+-----+
|  8  |
|  8  |
|  3  |
|  3  |
|  1  |
|  4  |
|  5  |
|  6  |
+-----+
```

**Salida:**

```bash
+-----+
| num |
+-----+
|  6  |
+-----+
```

Los números únicos son 1, 4, 5 y 6. El mayor número único es 6.

## Implementación

El problema se resuelve utilizando Python y la biblioteca pandas para la manipulación de datos, junto con la clase Counter del módulo collections para contar las ocurrencias de cada número.

### Detalles de la implementación

1. Cálculo de frecuencias: Usamos Counter para contar cuántas veces aparece cada número en la tabla.

2. Filtrado de números únicos: Identificamos los números que aparecen exactamente una vez.

3. Obtención del máximo: Si existen números únicos, seleccionamos el mayor. En caso contrario, retornamos None.

4. Retorno del resultado: El resultado se retorna en formato de un DataFrame de pandas con una columna num.

## Uso

Este código puede utilizarse con cualquier tabla cargada en un DataFrame de pandas. A continuación, se muestra un ejemplo práctico:

```python
if __name__ == "__main__":
    data = {"num": [8, 8, 3, 3, 1, 4, 5, 6]}
    my_numbers = pd.DataFrame(data)

    result = biggest_single_number(my_numbers)
    print(result)
    # Salida esperada:
    #    num
    # 0    6
```

## Conclusión

El ejercicio "Biggest Single Number" es un ejemplo útil de cómo procesar y analizar datos tabulares con herramientas como pandas. La solución propuesta ilustra técnicas prácticas para el conteo y filtrado de datos, mostrando cómo integrar la lógica de negocio con operaciones eficientes sobre estructuras de datos. Este problema fomenta habilidades esenciales para el trabajo con datos, incluidas la identificación de patrones y el uso de bibliotecas estándar en Python para tareas de análisis. La implementación es flexible y se puede reutilizar en diversos escenarios del mundo real.
