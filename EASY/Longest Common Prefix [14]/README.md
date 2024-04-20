# Longest Common Prefix

## Descripción

Este ejercicio implementa una solución al problema de encontrar el prefijo común más largo entre un arreglo de cadenas. El objetivo principal es identificar un prefijo que todas las cadenas del arreglo compartan. Si no existe tal prefijo, la función devuelve una cadena vacía "".

El problema se presenta con ciertas restricciones y casos de ejemplo para ilustrar el funcionamiento esperado de la función:

- Las cadenas solo contienen letras minúsculas del alfabeto inglés.
- El número de cadenas en el arreglo puede variar entre 1 y 200.
- La longitud de cada cadena puede variar entre 0 y 200.

## Implementación

La solución está encapsulada en la clase `Solution`, la cual contiene el método `longestCommonPrefix`. Este método acepta un arreglo de cadenas (`strs`) y retorna el prefijo común más largo encontrado.

El método se implementa de la siguiente manera:

1. Comprueba si alguna cadena en el arreglo está vacía y, de ser así, retorna una cadena vacía de inmediato.
2. Utiliza una lista para acumular los caracteres comunes al inicio de cada cadena.
3. Itera sobre los caracteres de las cadenas, comparándolos y acumulando el prefijo común mientras sea posible.
4. Finaliza la iteración y construcción del prefijo cuando encuentra una discrepancia entre los caracteres o se alcanza el final de alguna cadena.

El código está diseñado para manejar eficientemente los casos en los que el arreglo de entrada es grande o contiene cadenas de longitud variable.

## Uso

Para utilizar este código en tu proyecto, necesitas:

1. Crear una instancia de la clase `Solution`.
2. Llamar al método `longestCommonPrefix` con el arreglo de cadenas como argumento.

Ejemplo de uso:

```python
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)  # Output esperado: "fl"
```

## Conclusión

El ejercicio "Longest Common Prefix" provee una interesante oportunidad para entender y aplicar conceptos básicos de cadenas en Python, incluyendo manipulación de listas y control de flujos. La solución propuesta es eficiente para los límites dados por las restricciones y es aplicable en diversos contextos donde se requiera procesar colectivamente conjuntos de cadenas.
