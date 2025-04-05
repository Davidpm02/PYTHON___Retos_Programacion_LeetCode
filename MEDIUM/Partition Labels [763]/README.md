# Partition Labels

## Descripción

El ejercicio "Partition Labels" consiste en dividir una cadena de texto en el mayor número posible de subcadenas, de tal forma que cada letra del alfabeto aparezca en **una sola** de dichas subcadenas. La condición principal es que, al concatenar todas las particiones en orden, se obtenga nuevamente la cadena original. Este tipo de problema es útil en escenarios donde se desea segmentar datos preservando ciertas propiedades de unicidad dentro de cada segmento.

## Implementación

La implementación se desarrolla en Python dentro de una clase llamada `Solution`, la cual contiene el método `partitionLabels`. Este método se encarga de identificar la última aparición de cada carácter dentro de la cadena original para así determinar los puntos de corte válidos que permiten generar las subcadenas deseadas.

## Detalles de la implementación

- **Última aparición de caracteres:** Se construye un diccionario que mapea cada letra a su última aparición en la cadena. Esto permite saber hasta qué punto debe extenderse una partición para asegurarse de incluir todas las ocurrencias de cada letra.
- **Detección de particiones:** Se itera por la cadena y se ajusta dinámicamente el límite de la partición actual al máximo índice de cualquier letra encontrada hasta el momento. Cuando el índice actual coincide con este límite, se define una nueva partición.
- **Cálculo del tamaño:** Al cerrar una partición, se añade su tamaño a la lista de resultados, y se actualiza el punto de inicio de la próxima.

## Uso

Para utilizar este código, simplemente se debe definir la cadena de texto sobre la que se desea operar, crear una instancia de la clase `Solution` y llamar al método `partitionLabels`, el cual devolverá una lista de enteros que representan el tamaño de cada partición.

```python
if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"

    sol = Solution()
    result = sol.partitionLabels(s)
    print(result)  # Output: [9, 7, 8]
```

## Conclusión

El ejercicio "Partition Labels" permite aplicar técnicas de análisis de intervalos y manejo de mapas de ocurrencias para segmentar una cadena de texto en partes que cumplan una propiedad de exclusividad de caracteres. Esta solución es eficiente tanto en tiempo como en espacio, ya que recorre la cadena una sola vez y utiliza estructuras simples como diccionarios y listas. Además, constituye un buen ejemplo del uso de algoritmos de barrido y análisis de rangos aplicados a problemas de segmentación de datos.
