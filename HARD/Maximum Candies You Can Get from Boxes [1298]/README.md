# Maximum Candies You Can Get from Boxes

## Descripción

El ejercicio "Maximum Candies You Can Get from Boxes" consiste en maximizar la cantidad de dulces que se pueden obtener de un conjunto de cajas con ciertas características. Cada caja puede estar abierta o cerrada, contiene una cantidad determinada de dulces, puede contener llaves para otras cajas y además puede contener otras cajas en su interior. Se dispone de un conjunto inicial de cajas, y se debe recolectar la máxima cantidad de dulces posible siguiendo las reglas de apertura y acceso a cajas y llaves.

Este problema es un claro ejemplo de búsqueda y exploración en grafos o estructuras similares, donde las cajas son nodos conectados por relaciones de llaves y contenido. El objetivo es modelar el proceso de apertura y acceso para maximizar la extracción de recursos (dulces).

## Implementación

La solución se implementa en Python utilizando una clase `Solution` con el método `maxCandies`. Este método simula la apertura y exploración de cajas siguiendo las reglas del problema:

- Se comienza con las cajas iniciales.
- Se utiliza una cola para procesar las cajas que están abiertas y aún no se han visitado.
- Se mantiene un conjunto de llaves obtenidas para abrir nuevas cajas.
- Se registra el total de dulces recolectados conforme se procesan las cajas.
- Se actualizan los estados de las cajas conforme se obtienen llaves o se encuentran cajas dentro de otras.
- El proceso continúa hasta no quedar más cajas abiertas por procesar.

### Detalles de la implementación

- **Conjuntos y estructuras:** Se usan conjuntos para manejar llaves disponibles, cajas encontradas y cajas procesadas, garantizando operaciones eficientes de búsqueda y actualización.
- **Cola para BFS:** Se emplea una cola para procesar las cajas abiertas de manera iterativa, simulando una búsqueda en anchura.
- **Actualización de estados:** Cada vez que se obtiene una llave o una caja nueva, se verifica si es posible abrir o procesar dicha caja y se agrega a la cola si corresponde.
- **Prevención de procesamientos repetidos:** Se controla que cada caja se procese una única vez para evitar sumas duplicadas de dulces.

## Uso

Para utilizar este código, se deben definir las listas que representan el estado, la cantidad de dulces, las llaves, las cajas contenidas y las cajas iniciales. Luego, se instancia la clase `Solution` y se llama al método `maxCandies` con estos parámetros, obteniendo como resultado el número máximo de dulces que se pueden recolectar.

```python
if __name__ == "__main__":
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]

    sol = Solution()
    total_candies = sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(total_candies)  # Output esperado: 16
```

## Conclusión

El ejercicio "Maximum Candies You Can Get from Boxes" presenta un interesante problema de búsqueda y manejo de estados, donde se debe optimizar la extracción de recursos (dulces) mediante la apertura estratégica de cajas utilizando llaves y cajas contenidas. La solución implementada es eficiente y clara, utilizando estructuras de datos adecuadas para manejar la exploración y actualización dinámica de estados. Este ejercicio refuerza conceptos importantes de programación como búsqueda en grafos, manejo de conjuntos y simulación de procesos dinámicos, muy relevantes en problemas de Machine Learning para la exploración de espacios de estados o configuración.
