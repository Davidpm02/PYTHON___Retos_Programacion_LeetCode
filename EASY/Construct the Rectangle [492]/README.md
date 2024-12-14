# Construct the Rectangle

## Descripción

El ejercicio **"Construct the Rectangle"** consiste en diseñar un rectángulo dado su área objetivo, siguiendo tres criterios clave:

1. El área del rectángulo debe ser igual al valor dado.
2. La anchura (`W`) no debe ser mayor que la longitud (`L`), es decir, `L >= W`.
3. La diferencia entre la longitud y la anchura debe ser lo más pequeña posible.

El objetivo es devolver un array `[L, W]` que represente la longitud y la anchura del rectángulo de acuerdo con las restricciones anteriores.

### Ejemplos

- **Ejemplo 1**  
  Entrada: `area = 4`  
  Salida: `[2, 2]`  
  Explicación: Las posibles configuraciones son `[1, 4]`, `[2, 2]`, y `[4, 1]`. Según las restricciones, `[2, 2]` es la configuración óptima.  

- **Ejemplo 2**  
  Entrada: `area = 37`  
  Salida: `[37, 1]`  

- **Ejemplo 3**  
  Entrada: `area = 122122`  
  Salida: `[427, 286]`  

### Restricciones

- \( 1 \leq area \leq 10^7 \)

---

## Implementación

La implementación se realiza en Python mediante la clase `Solution`, que contiene el método `constructRectangle`. Este método sigue un enfoque basado en iteraciones para encontrar la mejor combinación de longitud y anchura.

### Detalles de la implementación

1. **Iteración desde la raíz cuadrada del área:**  
   Dado que buscamos minimizar la diferencia entre la longitud y la anchura, iteramos desde la raíz cuadrada del área hacia abajo. Esto garantiza que los pares evaluados sean lo más cercanos posibles.

2. **Validación de divisibilidad:**  
   Para cada divisor \( i \) del área, verificamos si \( area \mod i = 0 \). Esto garantiza que \( i \) y \( area / i \) sean números enteros.

3. **Configuración del par \( [L, W] \):**  
   Si encontramos un par válido donde \( L \geq W \), devolvemos inmediatamente el resultado.

---

## Uso

Para utilizar el código, crea una instancia de la clase `Solution` y llama al método `constructRectangle` con el área deseada como argumento. La salida será un array `[L, W]`.

### Ejemplo de uso

```python
from math import sqrt
from typing import List

if __name__ == "__main__":
    area = 37

    sol = Solution()
    dimensions = sol.constructRectangle(area)
    print(dimensions)  # Salida: [37, 1]
```

## Conclusión

El ejercicio "Construct the Rectangle" proporciona un problema práctico y eficiente para trabajar con divisores y optimizar configuraciones geométricas en base a restricciones. La solución se basa en recorrer los posibles divisores comenzando desde la raíz cuadrada del área, lo que reduce la complejidad del problema. Este enfoque asegura que las configuraciones retornadas sean tanto correctas como óptimas en términos de longitud y anchura. El algoritmo es eficiente y maneja áreas grandes dentro de los límites definidos.
