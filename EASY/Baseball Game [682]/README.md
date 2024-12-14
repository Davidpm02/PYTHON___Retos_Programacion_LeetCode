# Baseball Game

## Descripción

El ejercicio "Baseball Game" consiste en simular y calcular el puntaje total de un juego de béisbol siguiendo una serie de reglas establecidas. Para ello, se proporciona una lista de operaciones donde cada elemento indica una acción que afecta al registro de puntuaciones del juego. Este desafío combina conceptos de manejo de estructuras de datos, control de flujo y manipulación de listas.

Las operaciones permitidas son las siguientes:

1. Un entero : Registrar una nueva puntuación .

2. Registrar una nueva puntuación que sea la suma de las dos puntuaciones anteriores.

3. Registrar una nueva puntuación que sea el doble de la puntuación anterior.

4. Invalidar la puntuación anterior, eliminándola del registro.

Al final del juego, se retorna la suma total de las puntuaciones registradas.

## Implementación

La solución se desarrolla utilizando la clase Solution, la cual incluye el método calPoints que implementa la lógica para procesar las operaciones y calcular la suma total de puntuaciones.

## Uso

El método calPoints puede utilizarse definiendo una lista de operaciones y pasándola como argumento al método. A continuación se muestra un ejemplo completo de uso:

```python
if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]

    sol = Solution()
    total_score = sol.calPoints(ops)
    print(total_score)  # Output: 30
```

## Conclusión

El ejercicio "Baseball Game" es una herramienta útil para practicar la implementación de algoritmos que manipulan estructuras de datos en tiempo real. La solución presentada utiliza listas para mantener un registro dinámico de puntuaciones, mostrando cómo aplicar operaciones condicionales para modificar los datos. Este tipo de problema no solo es relevante para desarrollar habilidades de programación, sino también para comprender mejor el manejo de secuencias y sus transformaciones en Python.
