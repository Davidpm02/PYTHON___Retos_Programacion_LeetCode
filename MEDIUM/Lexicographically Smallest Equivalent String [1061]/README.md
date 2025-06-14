# Lexicographically Smallest Equivalent String

## Descripción

El ejercicio "Lexicographically Smallest Equivalent String" consiste en transformar una cadena `baseStr` utilizando información de equivalencia entre caracteres dada por dos cadenas `s1` y `s2` del mismo tamaño. Dos caracteres se consideran equivalentes si aparecen en la misma posición en `s1` y `s2`. Esta equivalencia cumple las propiedades de reflexividad, simetría y transitividad. El objetivo es devolver la cadena equivalente a `baseStr` que sea lexicográficamente la más pequeña posible, aplicando las equivalencias establecidas.

## Implementación

La solución se basa en la estructura de conjuntos disjuntos (Union-Find) para gestionar las relaciones de equivalencia entre caracteres. Se modela cada carácter como un nodo en un grafo, y se unen aquellos que son equivalentes, asegurando que en cada conjunto el representante sea el carácter lexicográficamente menor.

### Detalles de la implementación

- **Inicialización:** Se crea un arreglo `parent` donde cada índice representa un carácter (`'a'` a `'z'`) y apunta inicialmente a sí mismo.
- **Find con path compression:** Para encontrar el representante (raíz) de un conjunto y optimizar consultas posteriores.
- **Union:** Para unir dos conjuntos equivalentes, asegurando que el representante sea siempre el carácter más pequeño lexicográficamente.
- **Construcción del resultado:** Cada carácter de `baseStr` se reemplaza por el representante de su conjunto, generando así la cadena lexicográficamente mínima equivalente.

## Uso

Para utilizar el código, se definen las cadenas `s1`, `s2` y `baseStr`. Luego se crea una instancia de la clase `Solution` y se llama al método `smallestEquivalentString` con dichos argumentos, obteniendo la cadena equivalente lexicográficamente menor.

```python
if __name__ == "__main__":
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"

    sol = Solution()
    result = sol.smallestEquivalentString(s1, s2, baseStr)
    print(result)  # Output esperado: "makkek"
```

## Conclusión

El ejercicio "Lexicographically Smallest Equivalent String" ofrece una solución eficiente para encontrar la representación lexicográficamente mínima de una cadena dada una relación de equivalencia entre caracteres. La implementación usando Union-Find es óptima para gestionar conjuntos disjuntos, con una complejidad casi lineal respecto al tamaño de las cadenas. Esta solución no solo resuelve el problema específico, sino que también refuerza el uso práctico de estructuras de datos avanzadas para gestionar equivalencias y relaciones en grafos.
