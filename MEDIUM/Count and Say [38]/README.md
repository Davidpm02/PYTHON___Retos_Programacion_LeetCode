# Count and Say

## Descripción

El ejercicio **"Count and Say"** se basa en generar una secuencia de cadenas de texto conocida como *secuencia count-and-say*. Esta secuencia se construye aplicando de manera recursiva un algoritmo de compresión de tipo *Run-Length Encoding (RLE)*, donde se describe verbalmente el número y tipo de dígitos consecutivos presentes en la cadena anterior.  
Por ejemplo, partiendo de `"1"`, la siguiente cadena será `"11"` (un 1), luego `"21"` (dos 1s), seguido de `"1211"` (un 2 y un 1), y así sucesivamente. La función debe devolver el enésimo término de esta secuencia.

## Implementación

La solución está implementada en Python mediante una clase `Solution` que contiene el método `countAndSay`. Se trata de una implementación iterativa que genera la secuencia desde el primer elemento hasta alcanzar el número `n` solicitado. Para cada iteración se aplica el algoritmo RLE sobre la cadena anterior, generando así la siguiente.

## Detalles de la implementación

- **Caso base:** Si `n` es igual a 1, se retorna directamente `"1"`, ya que es el primer término de la secuencia.
- **Construcción iterativa:** Se utiliza un bucle que recorre desde 2 hasta `n`, actualizando en cada paso la cadena con su correspondiente codificación RLE.
- **Algoritmo RLE:** Para cada grupo de dígitos consecutivos, se cuenta cuántos hay y se concatena ese número seguido del dígito correspondiente.
- **Actualización del resultado:** Al finalizar cada iteración, la nueva cadena generada reemplaza a la anterior para continuar con la construcción del siguiente término.

## Uso

Para utilizar este código, se debe instanciar la clase `Solution` y llamar al método `countAndSay` con el valor de `n` deseado.

```python
if __name__ == "__main__":
    n = 4

    sol = Solution()
    result = sol.countAndSay(n)
    print(result)  # Output esperado: "1211"
```

## Conclusión

El ejercicio "Count and Say" es un buen ejemplo del uso práctico de algoritmos de compresión como el Run-Length Encoding. A través de un enfoque iterativo, se logra construir de forma eficiente cada término de la secuencia sin necesidad de aplicar recursión explícita. Esta implementación no solo refuerza conceptos de compresión de datos, sino también habilidades en el manejo de cadenas, contadores y bucles en Python.
