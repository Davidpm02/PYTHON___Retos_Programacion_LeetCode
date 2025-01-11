# Counting Words with a Given Prefix

## Descripción

El ejercicio "Counting Words with a Given Prefix" consiste en determinar cuántas cadenas en una lista tienen un prefijo específico dado. Un prefijo se define como un subconjunto contiguo de caracteres que se encuentran al inicio de una cadena. Este problema es útil en aplicaciones que requieren análisis de texto o filtrado de datos basados en patrones iniciales.

## Implementación

La solución se desarrolla en Python mediante una clase `Solution` que incluye el método principal `prefixCount`. Este método recorre la lista de palabras y utiliza una función auxiliar para verificar si cada palabra comienza con el prefijo especificado.

### Detalles de la implementación

- **Función auxiliar `isPrefix`:**
  - Determina si una palabra comienza con el prefijo especificado.
  - Utiliza el método `startswith` de Python, que realiza la comprobación de manera eficiente.
  - Retorna `True` si la palabra tiene el prefijo y `False` en caso contrario.

- **Método principal `prefixCount`:**
  - Recorre todas las palabras de la lista utilizando la función auxiliar.
  - Cuenta el número de palabras que cumplen la condición de tener el prefijo especificado.
  - Retorna la suma de las coincidencias como resultado.

## Uso

Para utilizar este código, es necesario crear una instancia de la clase `Solution` y llamar al método `prefixCount`, pasando como argumentos una lista de palabras y el prefijo que se desea verificar.

```python
if __name__ == "__main__":
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"

    sol = Solution()
    count = sol.prefixCount(words, pref)
    print(count)  # Output: 2
```

## Conclusión

El ejercicio "Counting Words with a Given Prefix" destaca cómo trabajar con cadenas y comprobar patrones específicos en texto de manera eficiente. La implementación, simple pero efectiva, aprovecha las capacidades incorporadas de Python para manejar cadenas y proporciona un método claro para resolver el problema. Este enfoque no solo es funcional para el problema planteado, sino que también refuerza conceptos clave como el uso de funciones auxiliares y el mapeo de operaciones en estructuras de datos.
