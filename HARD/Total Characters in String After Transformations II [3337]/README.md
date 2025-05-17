# Total Characters in String After Transformations II

## Descripción

El ejercicio **"Total Characters in String After Transformations II"** consiste en determinar la longitud final de una cadena de texto después de aplicarle un número `t` de transformaciones consecutivas. Cada transformación reemplaza cada carácter de la cadena por una secuencia de nuevos caracteres basada en una lógica de desplazamiento definido por el arreglo `nums`, de tamaño 26 (uno por cada letra minúscula del alfabeto inglés).

La transformación para cada carácter se realiza sustituyéndolo por los siguientes `nums[i]` caracteres consecutivos del alfabeto, con envolvimiento circular (`wrap-around`) en caso de sobrepasar la letra `'z'`. Esta operación se repite `t` veces. Dado que `t` puede ser muy grande (hasta 10⁹), el problema requiere una solución eficiente basada en técnicas de álgebra lineal, concretamente exponenciación de matrices, para evitar cálculos repetitivos y costosos.

## Implementación

La solución está implementada en Python y encapsulada dentro de la clase `Solution`, que contiene el método `lengthAfterTransformations`. Esta implementación utiliza álgebra matricial para modelar el sistema de transformaciones como un problema de transición de estados. Los pasos fundamentales son:

- **Contar la frecuencia inicial de cada letra** de la cadena.
- **Construir una matriz de transición** `T` de tamaño 26x26, que define cómo cada letra da lugar a otras letras en una sola transformación.
- **Aplicar exponenciación rápida de matrices** sobre `T`, elevándola a la potencia `t` para modelar el efecto acumulado de las `t` transformaciones.
- **Multiplicar el vector de frecuencias original** por la matriz `T^t` para obtener la distribución final de caracteres.
- **Sumar todos los elementos** del vector resultante para obtener la longitud final de la cadena transformada.

La operación se realiza bajo un módulo `10^9 + 7`, ya que la longitud resultante puede ser muy grande.

## Uso

Para utilizar esta implementación, simplemente se debe proporcionar la cadena `s`, el número de transformaciones `t`, y el arreglo `nums` con los desplazamientos por letra. El resultado será la longitud final de la cadena tras aplicar todas las transformaciones.

```python
if __name__ == "__main__":
    s = "abcyy"
    t = 2
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

    sol = Solution()
    final_length = sol.lengthAfterTransformations(s, t, nums)
    print(final_length)  # Output esperado: 7
```

## Conclusión

Este ejercicio pone a prueba la capacidad de modelar un problema de transformación repetitiva sobre cadenas mediante herramientas de álgebra lineal, y concretamente con la técnica de exponenciación de matrices. Esto permite escalar la solución a valores de t muy grandes sin incurrir en una complejidad prohibitiva. Además, la implementación modular y eficiente no solo resuelve el problema, sino que también refuerza conceptos clave como el conteo de frecuencias, la manipulación de matrices y la importancia de trabajar con aritmética modular en problemas de gran escala computacional.
