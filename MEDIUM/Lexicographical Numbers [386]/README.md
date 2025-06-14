# Lexicographical Numbers

## Descripción

El ejercicio **"Lexicographical Numbers"** consiste en devolver todos los números en el rango `[1, n]` ordenados lexicográficamente, es decir, como si se ordenasen como cadenas de texto. Por ejemplo, para `n = 13`, la salida sería `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`. 

El reto principal es implementar un algoritmo que funcione en tiempo O(n) y utilice un espacio extra constante O(1), optimizando la generación del listado sin necesidad de ordenar explícitamente toda la lista.

## Implementación

La solución está implementada en Python dentro de una clase `Solution`, que contiene el método `lexicalOrder`. Este método emplea un recorrido en profundidad (DFS) para generar los números en orden lexicográfico de forma natural, evitando generar y ordenar una lista completa posteriormente.

### Detalles de la implementación

- **DFS recursivo:** Se define una función auxiliar `dfs(current)` que explora recursivamente los números a partir del valor `current`, agregándolos a la lista resultado siempre que no superen `n`.
- **Construcción del árbol:** Desde cada número `current`, se generan los números hijos concatenando dígitos del 0 al 9 (por ejemplo, desde `1` se generan `10, 11, ..., 19`), asegurando que no se exceda `n`.
- **Inicio del recorrido:** La búsqueda comienza con los números del 1 al 9, dado que no se pueden iniciar números con cero.
- **Corte temprano:** Si al generar un nuevo número este supera `n`, la rama se abandona para evitar búsquedas innecesarias.

Este enfoque garantiza una enumeración ordenada sin usar espacio adicional para ordenar y manteniendo la eficiencia requerida.

## Uso

Para utilizar el código, solo es necesario definir el valor `n`, crear una instancia de la clase `Solution` y llamar al método `lexicalOrder` para obtener la lista de números lexicográficamente ordenados.

```python
if __name__ == "__main__":
    n = 13

    sol = Solution()
    lex_numbers = sol.lexicalOrder(n)
    print(lex_numbers)  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Conclusión

El ejercicio "Lexicographical Numbers" permite entender cómo generar secuencias ordenadas lexicográficamente mediante recorridos DFS eficientes. La implementación evita la necesidad de ordenar listas completas, reduciendo el coste computacional y el uso de memoria, lo cual es crucial para rangos grandes. Este problema refuerza el manejo de técnicas recursivas, optimización en generación de secuencias y comprensión de ordenamientos no triviales en programación.
