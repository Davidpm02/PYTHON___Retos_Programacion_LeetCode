# Find Numbers with Even Number of Digits

## Descripción

El ejercicio **"Find Numbers with Even Number of Digits"** tiene como objetivo contar cuántos números dentro de un array de enteros contienen una cantidad par de dígitos. Este problema está orientado a trabajar con la manipulación de números y cadenas, y es útil para familiarizarse con la conversión de tipos y operaciones básicas sobre datos numéricos en programación.

Se trata de un ejercicio sencillo pero efectivo para reforzar habilidades relacionadas con la iteración, validación de condiciones y comprensión del sistema decimal.

## Implementación

La solución se implementa en Python a través de una clase `Solution`, que contiene el método `findNumbers`. Este método se encarga de recorrer todos los elementos del array `nums`, convertir cada número a una cadena para poder contar sus dígitos, y finalmente determinar si dicha cantidad es par.

## Detalles de la implementación

- **Inicialización del contador:** Se crea una variable `even_number_counter` para llevar el seguimiento de cuántos números cumplen la condición.
- **Conversión a string:** Cada número entero se convierte a cadena mediante `str(num)` para poder calcular fácilmente la longitud (número de dígitos).
- **Validación de paridad:** Se utiliza el operador módulo `%` para verificar si el número de dígitos es par.
- **Acumulación de resultado:** Cada vez que un número cumple la condición, se incrementa el contador.

Este enfoque es simple, directo y muy legible, aprovechando las capacidades básicas de Python para tratar con tipos de datos y operadores.

## Uso

Para utilizar este código, se debe definir una lista de enteros llamada `nums`. Luego, se crea una instancia de la clase `Solution` y se invoca el método `findNumbers`, el cual devolverá un número entero representando cuántos elementos del array tienen una cantidad par de dígitos.

```python
if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]

    sol = Solution()
    result = sol.findNumbers(nums)
    print(result)  # Output: 2
```

## Conclusión

El ejercicio "Find Numbers with Even Number of Digits" representa una forma clara y concisa de practicar el análisis de características numéricas dentro de listas. El enfoque basado en la conversión a cadena permite resolver el problema de forma sencilla sin recurrir a operaciones matemáticas complejas. Este tipo de problema es habitual en entrevistas técnicas y es una excelente forma de consolidar fundamentos de programación como el control de flujo, la manipulación de tipos y la evaluación de condiciones.
