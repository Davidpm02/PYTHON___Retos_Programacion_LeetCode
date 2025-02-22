# Find Unique Binary String

## Descripción

El ejercicio "Find Unique Binary String" consiste en encontrar una cadena binaria de longitud `n` que no esté presente en una lista dada de `n` cadenas binarias de la misma longitud. Si existen múltiples soluciones, se puede devolver cualquiera de ellas.

Este problema es útil en situaciones donde se requiere generar identificadores únicos que no colisionen con un conjunto preexistente de valores.

## Implementación

La solución se implementa en Python dentro de la clase `Solution`, que contiene el método `findDifferentBinaryString`. Este método evalúa las combinaciones posibles de cadenas binarias para encontrar una que no esté en la lista de entrada `nums`.

### Detalles de la Implementación

- **Verificación de caso base:** Si `nums` contiene solo una cadena de un solo bit, se devuelve el complemento de dicha cadena.
- **Búsqueda de la cadena faltante:**
  - Se verifica si la cadena compuesta solo por ceros (`"000...0"`) ya está en `nums`. Si no está, se devuelve directamente.
  - Se genera un conjunto de cadenas binarias candidatas, iterando y combinando bits hasta encontrar una que no esté en `nums`.
  - Se usa una estrategia incremental para modificar bits de derecha a izquierda y encontrar una solución válida.

## Uso

Para utilizar este código, se debe definir la lista de cadenas binarias y luego llamar al método `findDifferentBinaryString` de la clase `Solution`.

```python
if __name__ == "__main__":
    nums = ["111", "011", "001"]
    
    sol = Solution()
    unique_binary = sol.findDifferentBinaryString(nums)
    print(unique_binary)  # Output: Puede ser "101", "000", "010", "100", "110", etc.
```

## Conclusión

El ejercicio "Find Unique Binary String" permite encontrar una cadena binaria única que no esté contenida en un conjunto dado. La solución aprovecha la generación incremental de cadenas y verificaciones eficientes para determinar una opción válida. Este tipo de problema es común en aplicaciones que requieren evitar colisiones en identificadores y generar combinaciones únicas de datos.
