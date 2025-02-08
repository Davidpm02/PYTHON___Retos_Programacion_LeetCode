# Design a Number Container System

## Descripción

El ejercicio "Design a Number Container System" consiste en diseñar un sistema que maneje contenedores de números, permitiendo insertar o reemplazar un número en un índice específico, así como encontrar el índice más pequeño que contiene un número dado. Este tipo de ejercicio es útil para trabajar con estructuras de datos como diccionarios y montículos (heaps), y es común en la optimización de operaciones en bases de datos o sistemas que requieren búsquedas rápidas.

## Implementación

La implementación se realiza mediante la clase `NumberContainers`, que mantiene dos estructuras de datos:

- **`index_to_number`:** Un diccionario que mapea cada índice a un número específico.
- **`num_to_heap`:** Un diccionario que mapea cada número a un "heap" (montículo) de índices donde se encuentra dicho número.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `NumberContainers` y luego llamar a los métodos `change` y `find` según sea necesario.

```python
if __name__ == "__main__":
    nc = NumberContainers()
    
    print(nc.find(10))  # Output: -1
    
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    
    print(nc.find(10))  # Output: 1
    
    nc.change(1, 20)
    print(nc.find(10))  # Output: 2
```

## Conclusión

El ejercicio "Design a Number Container System" proporciona una solución eficiente para almacenar y consultar números en un sistema de contenedores. Utilizando estructuras de datos como diccionarios y heaps, se logra optimizar las operaciones de inserción, reemplazo y búsqueda de índices. Este enfoque es escalable y puede manejar una gran cantidad de operaciones debido a la eficiencia de las operaciones de heap y diccionario. La implementación es adecuada para problemas que requieren optimización en la búsqueda de índices asociados con valores específicos.
