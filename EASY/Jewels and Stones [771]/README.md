# Jewels and Stones

## Descripción

El ejercicio "Jewels and Stones" consiste en determinar cuántas piedras en un inventario dado son consideradas joyas. Se nos proporcionan dos cadenas:

- `jewels`: representa los tipos de piedras que son consideradas joyas.
- `stones`: representa el inventario de piedras disponible.

El objetivo es contar cuántas piedras en el inventario corresponden a los tipos de joyas definidos. Es importante considerar que las letras son sensibles a mayúsculas y minúsculas, es decir, `"a"` es diferente de `"A"`.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con un método `numJewelsInStones`. A continuación, se describen los pasos de la implementación:

1. **Listado de joyas:**
   - Se crea una lista con los caracteres de la cadena `jewels`, los cuales representan las joyas de referencia.

2. **Conteo de joyas en piedras:**
   - Se recorre la lista de joyas y, para cada tipo de joya, se cuenta cuántas veces aparece en la cadena `stones` usando el método `count()`.

3. **Suma acumulativa:**
   - Se suma el total de apariciones para obtener la cantidad final de joyas en el inventario de piedras.

## Uso

Para utilizar este código, crea una instancia de la clase Solution y llama al método numJewelsInStones, pasando las cadenas jewels y stones como parámetros. El método devolverá el número total de joyas presentes en el inventario de piedras.

```python
if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"

    sol = Solution()
    result = sol.numJewelsInStones(jewels, stones)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Jewels and Stones" ofrece una solución sencilla para contar elementos que cumplen un criterio específico en un conjunto mayor. La implementación aprovecha las capacidades de Python para manejar cadenas y realizar operaciones repetitivas con claridad y eficiencia. Este problema es un excelente ejemplo de cómo trabajar con listas y métodos integrados para procesar datos de forma eficiente, resaltando conceptos clave como el recorrido de estructuras de datos y la manipulación de cadenas.
