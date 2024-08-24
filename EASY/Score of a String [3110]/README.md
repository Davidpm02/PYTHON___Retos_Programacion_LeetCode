# Score of a String

## Descripción

El ejercicio "Score of a String" consiste en calcular la puntuación (score) de una cadena de texto `s`. La puntuación de la cadena se define como la suma de las diferencias absolutas entre los valores ASCII de caracteres adyacentes en la cadena. Este tipo de operación es útil en el análisis de cadenas y procesamiento de texto, donde la relación entre caracteres puede tener un significado particular.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `scoreOfString`. Este método toma una cadena de caracteres en minúscula y devuelve un entero que representa la puntuación de la cadena según la fórmula mencionada.

### Detalles de la Implementación

- **Inicialización del resultado:**
  - Se inicializa una variable `result` en 0, que almacenará la puntuación acumulada.
- **Cálculo de diferencias absolutas:**
  - Se itera sobre la cadena de texto `s`, calculando la diferencia absoluta entre los valores ASCII de cada par de caracteres adyacentes.
  - Se utiliza la función `ord()` para obtener el valor ASCII de cada carácter.
- **Acumulación del resultado:**
  - En cada iteración, se actualiza la variable `result` sumando la diferencia absoluta calculada.

Este enfoque asegura que la puntuación se calcule de manera eficiente, incluso para cadenas de longitud máxima según las restricciones del problema.

## Uso

Para utilizar este código, simplemente define una cadena `s`, crea una instancia de la clase `Solution`, y llama al método `scoreOfString`. El resultado será un entero que representa la puntuación de la cadena.

```python
if __name__ == "__main__":
    s = "hello"
    
    sol = Solution()
    score = sol.scoreOfString(s)
    print(score)  # Output: 13
```

## Conclusión

El ejercicio "Score of a String" ofrece una forma práctica de calcular una métrica simple basada en los valores ASCII de una cadena de texto. La solución implementada es directa y eficiente, utilizando operaciones básicas para obtener el resultado deseado. Este tipo de problemas es útil en escenarios donde se necesita evaluar la similitud o diferencias entre caracteres en una cadena, y refuerza el uso de funciones básicas de Python para el procesamiento de texto.
