# Maximum Employees to Be Invited to a Meeting

## Descripción

El ejercicio "Maximum Employees to Be Invited to a Meeting" plantea el desafío de maximizar el número de empleados que pueden asistir a una reunión, considerando que cada empleado solo asistirá si su "empleado favorito" también está presente. Además, la disposición en la mesa de reuniones es circular, lo que significa que cada empleado puede tener un máximo de dos vecinos inmediatos.

Dado un array `favorite`, donde `favorite[i]` representa el empleado favorito del `i-ésimo` empleado, el objetivo es encontrar el máximo número de empleados que pueden ser invitados cumpliendo con las restricciones establecidas.

## Implementación

La solución se implementa en Python a través de la clase `Solution`, que contiene el método `maximumInvitations`. Este método analiza la estructura del grafo implícito definido por `favorite` y determina la mayor cantidad de empleados que pueden asistir al evento.

### Detalles de la implementación

- **Detección de ciclos:** Se busca identificar ciclos en la estructura de preferencias de los empleados, ya que los ciclos representan grupos cerrados que pueden asistir en su totalidad.
- **Cálculo de la cadena más larga:** En caso de que algunos empleados no formen parte de un ciclo directo, se determinan las cadenas de empleados que pueden ser anexadas a ciclos de tamaño 2.
- **Uso de estructuras eficientes:** Se emplean listas de adyacencia, recorridos en profundidad y colas (`deque`) para optimizar la exploración del grafo de relaciones de empleados.

## Uso

Para utilizar este código, basta con definir el array `favorite` y llamar al método `maximumInvitations` de la clase `Solution`.

```python
if __name__ == "__main__":
    favorite = [2, 2, 1, 2]
    
    sol = Solution()
    max_employees = sol.maximumInvitations(favorite)
    print(max_employees)  # Output: 3
```

## Conclusión

El ejercicio "Maximum Employees to Be Invited to a Meeting" presenta un desafío de optimización basado en la teoría de grafos. La solución implementada aprovecha la detección de ciclos y la evaluación de cadenas de empleados para encontrar la mejor configuración posible. Este problema ilustra la importancia de estructuras de datos eficientes y algoritmos de recorrido de grafos en escenarios de optimización y modelado de relaciones entre elementos.
