# Design HashMap

## Descripción

El ejercicio "Design HashMap" plantea la tarea de diseñar un HashMap desde cero sin utilizar bibliotecas predefinidas de tablas hash. Un HashMap es una estructura de datos que permite almacenar pares clave-valor y proporciona acceso rápido a los valores mediante las claves correspondientes.

Este ejercicio requiere implementar la clase `MyHashMap` con las siguientes funcionalidades:

- **`put(key, value)`**: Inserta un par (clave, valor) en el HashMap. Si la clave ya existe, actualiza el valor correspondiente.
- **`get(key)`**: Devuelve el valor asociado a la clave proporcionada o `-1` si no existe una asociación.
- **`remove(key)`**: Elimina la clave y el valor correspondiente del HashMap, si existen.

## Implementación

La implementación utiliza un diccionario nativo de Python (`dict`) para almacenar y manipular los pares clave-valor, adaptándolo para satisfacer los requisitos del problema.

### Detalles de la implementación

- **Estructura interna**: Se utiliza un atributo llamado `dict_` para representar el mapa, con claves como índices y valores asociados.
- **Insertar (`put`)**: Agrega o actualiza un par clave-valor en el diccionario.
- **Obtener (`get`)**: Retorna el valor correspondiente a una clave dada si existe, de lo contrario devuelve `-1`.
- **Eliminar (`remove`)**: Reconstruye el diccionario excluyendo la clave especificada, simulando la operación de eliminación.

## Uso

Para utilizar esta implementación, crea una instancia de la clase MyHashMap e interactúa con sus métodos. Estos permiten agregar, actualizar, consultar y eliminar pares clave-valor según sea necesario.

```python
if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)  # Inserta el par (1, 1)
    myHashMap.put(2, 2)  # Inserta el par (2, 2)
    print(myHashMap.get(1))  # Devuelve 1
    print(myHashMap.get(3))  # Devuelve -1
    myHashMap.put(2, 1)  # Actualiza el valor asociado a la clave 2
    print(myHashMap.get(2))  # Devuelve 1
    myHashMap.remove(2)  # Elimina el par con clave 2
    print(myHashMap.get(2))  # Devuelve -1
```

## Conclusión

El ejercicio "Design HashMap" permite explorar el diseño básico de estructuras de datos de mapeo mediante el uso de operaciones fundamentales. Si bien la implementación presentada se basa en un diccionario de Python para simplificar el manejo, puede extenderse o modificarse para incluir características adicionales como funciones de hashing personalizadas, manejo de colisiones o estructuras internas avanzadas para optimizar el rendimiento. Este enfoque refuerza conceptos clave en la implementación y gestión de estructuras de datos basadas en claves.
