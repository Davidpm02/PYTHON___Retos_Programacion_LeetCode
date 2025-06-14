# Maximum Difference Between Even and Odd Frequency I

## Descripción

El ejercicio **"Maximum Difference Between Even and Odd Frequency I"** consiste en analizar una cadena de texto compuesta exclusivamente por letras minúsculas del alfabeto inglés, con el objetivo de calcular la **máxima diferencia entre la frecuencia de dos caracteres**, `freq(a1) - freq(a2)`, cumpliendo las siguientes condiciones:

- `a1` debe tener una frecuencia **impar** en la cadena.
- `a2` debe tener una frecuencia **par** en la cadena.

El objetivo es retornar dicha diferencia máxima entre todos los pares posibles de caracteres que cumplan con la condición anterior. Este tipo de problema es útil para comprender cómo analizar distribuciones de caracteres, aplicar filtrado por propiedades aritméticas (paridad), y realizar comparaciones selectivas sobre datos agregados.

## Implementación

La implementación está realizada en Python utilizando la clase `Solution`, la cual define un único método llamado `maxDifference`. Este método recibe una cadena de texto y retorna la diferencia máxima entre las frecuencias de un carácter impar y un carácter par.

### Detalles de la implementación

- **Conteo de caracteres:** Se emplea `collections.Counter` para contar las ocurrencias de cada carácter en la cadena.
- **Filtrado por paridad:** Se filtran las frecuencias impares y pares en listas separadas.
- **Ordenación:** Ambas listas se ordenan para facilitar la obtención del mayor valor impar y el menor valor par.
- **Cálculo de la diferencia:** Se calcula la diferencia máxima como `max(freq_impar) - min(freq_par)`.

Este enfoque garantiza una solución simple, clara y eficiente, dada la longitud máxima permitida de la cadena (`s.length <= 100`).

## Uso

Para utilizar este código, basta con definir una cadena de texto `s` y crear una instancia de la clase `Solution`. Luego se llama al método `maxDifference` con dicha cadena como argumento, obteniendo así el resultado deseado.

```python
if __name__ == "__main__":
    s = "aaaaabbc"

    sol = Solution()
    result = sol.maxDifference(s)
    print(result)  # Output: 3
```

## Conclusión

El ejercicio "Maximum Difference Between Even and Odd Frequency I" es una excelente práctica para trabajar con frecuencias de caracteres y aplicar condiciones basadas en propiedades numéricas como la paridad. La solución propuesta aprovecha las capacidades de la biblioteca estándar de Python, permitiendo una implementación eficiente y concisa. Este problema no solo refuerza el manejo de estructuras de datos como diccionarios y listas, sino que también ayuda a comprender cómo aplicar filtros lógicos en el análisis de datos textuales.
