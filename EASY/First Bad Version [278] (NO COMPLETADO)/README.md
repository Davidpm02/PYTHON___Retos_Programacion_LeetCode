# First Bad Version

## Descripción

El ejercicio "First Bad Version" es un reto en el que se debe encontrar la primera versión defectuosa de un producto a partir de un conjunto de versiones secuenciales. El problema se basa en que, una vez que se detecta una versión defectuosa, todas las versiones posteriores también lo serán. Para resolver este problema, se dispone de una API `isBadVersion(version)` que devuelve si una versión específica es defectuosa o no.

Este ejercicio no está completamente terminado. La solución implementada está en proceso de desarrollo y optimización.

## Implementación

La solución propuesta utiliza una clase `Solution` que contiene el método `firstBadVersion`, cuyo objetivo es encontrar la primera versión defectuosa minimizando el número de llamadas a la API `isBadVersion`.

La idea principal es realizar una búsqueda eficiente aprovechando las propiedades de la secuencia, similar a una búsqueda binaria. Si se encuentra una versión defectuosa, se continúa buscando hacia versiones anteriores, descartando las posteriores, hasta encontrar la primera versión mala.

### Detalles de la implementación

- **Estrategia inicial**: Si el número de versiones `n` es menor que 1000, se hace una búsqueda lineal para cada versión llamando a la API `isBadVersion`.
- **Optimización**: Para casos más grandes, se realiza una búsqueda progresiva dividiendo el conjunto de versiones en mitades, verificando el punto medio. Dependiendo del resultado de `isBadVersion`, se ajustan los límites del conjunto para encontrar la primera versión defectuosa.
- **Control de límites**: El algoritmo busca optimizar el número de llamadas a la API, ajustando los índices de búsqueda para descartar grandes porciones del conjunto de versiones.

## Uso

Para utilizar este código, primero debes definir la cantidad de versiones disponibles (n) y asegurarte de que la API isBadVersion(version) esté correctamente implementada. Luego, puedes crear una instancia de la clase Solution y llamar al método firstBadVersion para obtener el número de la primera versión defectuosa.

```python
if __name__ == "__main__":
    n = 5  # Número de versiones
    # bad = 4
    sol = Solution()
    first_bad = sol.firstBadVersion(n)
    print(f"La primera versión defectuosa es: {first_bad}")
```

## Conclusión

El ejercicio "First Bad Version" es un reto interesante que implica una búsqueda eficiente dentro de un conjunto de versiones secuenciales. Aunque la implementación actual aún está en desarrollo y no completamente optimizada, ya se han establecido los fundamentos para reducir el número de llamadas a la API.

El uso de técnicas similares a la búsqueda binaria permitirá mejorar la eficiencia en la detección de la primera versión defectuosa, especialmente en casos con grandes cantidades de versiones.
