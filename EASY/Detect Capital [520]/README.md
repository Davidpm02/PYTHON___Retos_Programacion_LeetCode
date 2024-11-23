# Detect Capital

## Descripción

El ejercicio "Detect Capital" consiste en verificar si el uso de mayúsculas en una palabra es correcto según las siguientes reglas:

1. Todas las letras de la palabra son mayúsculas, como en `"USA"`.
2. Todas las letras de la palabra son minúsculas, como en `"leetcode"`.
3. Solo la primera letra de la palabra es mayúscula, como en `"Google"`.

Si alguna de estas condiciones se cumple, se debe retornar `True`. En caso contrario, se retorna `False`.

## Implementación

La solución se implementa en Python mediante la clase `Solution`, que contiene el método `detectCapitalUse`. Este método comprueba las tres condiciones descritas utilizando métodos nativos de Python como `upper()`, `lower()` y `title()`.

### Detalles de la implementación

- **Condición de mayúsculas:** Se utiliza `word.upper()` para comprobar si todas las letras son mayúsculas.
- **Condición de minúsculas:** Se utiliza `word.lower()` para verificar si todas las letras son minúsculas.
- **Condición de capitalización correcta:** Se utiliza `word.title()` para comprobar si la primera letra es mayúscula y las demás son minúsculas.
- **Devolución del resultado:** Si alguna de las condiciones anteriores se cumple, el método retorna `True`. En caso contrario, retorna `False`.

## Uso

Para utilizar este código, define una palabra en inglés como cadena de texto y crea una instancia de la clase Solution. Luego, llama al método detectCapitalUse con la palabra como argumento para verificar si cumple con las reglas de uso de mayúsculas.

```python
if __name__ == "__main__":
    word = "Google"
    
    sol = Solution()
    result = sol.detectCapitalUse(word)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Detect Capital" es una práctica esencial para trabajar con cadenas de texto y validaciones en Python. Utiliza métodos integrados para simplificar la verificación de reglas de uso de mayúsculas en palabras. Este enfoque es eficiente y permite reforzar conceptos básicos sobre manipulación de cadenas, haciendo el código claro y directo para leer y mantener. Es una tarea común en programación que encuentra aplicaciones en sistemas de procesamiento de texto y validaciones de entrada.
