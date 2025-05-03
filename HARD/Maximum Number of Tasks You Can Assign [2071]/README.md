# Maximum Number of Tasks You Can Assign

## Descripción

El ejercicio **"Maximum Number of Tasks You Can Assign"** plantea el problema de asignar tareas a trabajadores según sus capacidades físicas. Cada tarea requiere un nivel específico de fuerza, mientras que cada trabajador dispone de una fuerza determinada. Adicionalmente, se cuenta con un número limitado de píldoras mágicas que aumentan temporalmente la fuerza de los trabajadores. El objetivo es determinar el número máximo de tareas que pueden completarse, considerando tanto la fuerza natural de los trabajadores como la opción de usar píldoras para suplir deficiencias.

Este tipo de problema es común en la optimización de recursos y asignación de tareas bajo restricciones, y se relaciona con técnicas clásicas como búsqueda binaria y estrategias greedy para maximizar resultados.

## Implementación

La solución se implementa en Python mediante una clase `Solution` que contiene el método `maxTaskAssign`. Este método toma como parámetros las listas `tasks` y `workers`, junto con los enteros `pills` y `strength`. El enfoque utilizado combina ordenación, estructuras de datos eficientes (`deque`) y una búsqueda binaria para determinar la cantidad máxima de tareas que pueden ser completadas bajo las condiciones dadas.

## Detalles de la implementación

- **Ordenación inicial:** Tanto las tareas como los trabajadores se ordenan para facilitar la asignación eficiente.
- **Búsqueda binaria:** Se utiliza para encontrar el número máximo de tareas asignables (`k`). Para cada valor intermedio, se verifica si es posible asignar `k` tareas a `k` trabajadores mediante la función auxiliar `canAssignTasks`.
- **Asignación con píldoras:** Dentro de `canAssignTasks`, se intenta asignar tareas desde las más difíciles hacia las más fáciles. Se utiliza una cola doble (`deque`) para gestionar dinámicamente los trabajadores disponibles. Si un trabajador no puede cumplir la tarea por sí solo, se evalúa si, con una píldora, podría alcanzarse la fuerza mínima requerida.
- **Eliminación controlada:** Cuando se asigna una tarea con o sin píldora, el trabajador correspondiente se elimina del conjunto disponible para evitar reasignaciones.

## Uso

Para utilizar este código, basta con definir las listas de tareas y trabajadores, así como los parámetros de píldoras y fuerza adicional. Luego, se crea una instancia de la clase `Solution` y se llama al método `maxTaskAssign` con estos valores.

```python
if __name__ == "__main__":
    tasks = [3, 2, 1]
    workers = [0, 3, 3]
    pills = 1
    strength = 1

    sol = Solution()
    max_tasks = sol.maxTaskAssign(tasks, workers, pills, strength)
    print(max_tasks)  # Output esperado: 3
```

## Conclusión

El ejercicio "Maximum Number of Tasks You Can Assign" representa un interesante desafío algorítmico que combina estrategias de búsqueda, uso eficiente de estructuras de datos y lógica de asignación condicionada. La solución implementada es robusta y escalable, siendo capaz de manejar límites altos gracias al uso de búsqueda binaria y ordenación previa. Este tipo de problemas es altamente representativo de escenarios del mundo real donde la asignación de recursos limitados debe hacerse de forma óptima, respetando restricciones específicas.
