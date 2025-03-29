# Count Days Without Meetings

## Descripción

El ejercicio "Count Days Without Meetings" consiste en determinar cuántos días un empleado está disponible para trabajar sin que tenga reuniones programadas. Para ello, se cuenta con un número total de días disponibles y una lista de reuniones, donde cada reunión tiene un día de inicio y un día de fin (ambos inclusive). El objetivo es calcular cuántos días no están ocupados por reuniones.

## Implementación

La implementación se realiza en Python mediante una clase `Solution` que contiene el método `countDays`. Este método analiza los intervalos de reuniones y determina los días libres disponibles.

## Detalles de la implementación

- **Registro de eventos**: Se almacena el inicio y fin de cada reunión en una lista de eventos.
- **Ordenación de eventos**: Se ordenan los eventos para procesar correctamente la cantidad de reuniones activas en cada momento.
- **Conteo de días libres**: Se recorre la lista de eventos y se suman los días en los que no hay reuniones activas.

## Uso

Para utilizar este código, simplemente se deben definir el número total de días disponibles y la lista de reuniones. Luego, se crea una instancia de la clase `Solution` y se llama al método `countDays` con estos parámetros:

```python
if __name__ == "__main__":
    days = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    
    sol = Solution()
    available_days = sol.countDays(days, meetings)
    print(available_days)  # Output esperado: 2
```

## Conclusión

El ejercicio "Count Days Without Meetings" permite calcular de manera eficiente la cantidad de días en los que un empleado está disponible para trabajar sin reuniones programadas. La implementación optimiza el procesamiento de intervalos de tiempo utilizando una estrategia basada en eventos, lo que permite manejar grandes cantidades de reuniones de forma eficiente. Este problema es útil en aplicaciones de planificación y optimización de agendas.
