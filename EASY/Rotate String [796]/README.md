# Rotate String

## Descripción

El ejercicio "Rotate String" tiene como objetivo determinar si una cadena `s` puede transformarse en otra cadena `goal` mediante un número finito de rotaciones. Una rotación consiste en mover el carácter más a la izquierda de la cadena `s` a su posición más a la derecha. 

Este problema explora conceptos de manipulación de cadenas y algoritmos de rotación, útiles para resolver problemas relacionados con patrones y estructuras cíclicas.

## Implementación

La solución se implementa en Python utilizando una clase `Solution` que incluye el método `rotateString`. Este método realiza las rotaciones de la cadena `s` iterativamente y verifica si en algún momento coincide con la cadena `goal`.

### Detalles de la implementación

1. **Copia del estado inicial:**  
   - Se guarda una copia del estado original de `s` para detectar ciclos completos, lo que ayuda a evitar un bucle infinito.

2. **Proceso de rotación:**
   - Para cada iteración, el carácter más a la izquierda de la cadena `s` se mueve a la posición más a la derecha.
   - Esto se logra separando la cadena en dos segmentos: el primer carácter y el resto, y luego concatenándolos en el orden rotado.

3. **Verificación de coincidencia:**
   - Después de cada rotación, se compara la cadena resultante con la cadena `goal`.
   - Si `goal` coincide con alguna rotación, el método devuelve `True`.

4. **Fin de las rotaciones:**
   - Si, después de completar todas las posibles rotaciones, no se encuentra coincidencia, el método devuelve `False`.

## Uso

Para utilizar este código, simplemente crea una instancia de la clase `Solution` y llama al método `rotateString`, proporcionando las cadenas `s` y `goal` como argumentos.

```python
if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"

    sol = Solution()
    result = sol.rotateString(s, goal)
    print(result)  # Output: True
```

## Conclusión

El ejercicio "Rotate String" es una herramienta excelente para aprender sobre la manipulación de cadenas y estructuras iterativas. La solución propuesta aborda el problema de manera eficiente mediante rotaciones sucesivas, verificando coincidencias de manera directa. Este ejercicio refuerza habilidades en algoritmos de rotación, análisis de ciclos y comprensión de patrones, fundamentales para tareas avanzadas de programación.
