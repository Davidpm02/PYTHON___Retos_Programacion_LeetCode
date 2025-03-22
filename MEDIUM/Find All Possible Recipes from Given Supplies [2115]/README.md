# Find All Possible Recipes from Given Supplies

## Descripción

El ejercicio **"Find All Possible Recipes from Given Supplies"** consiste en determinar qué recetas pueden ser preparadas con una lista inicial de ingredientes disponibles. Para ello, se cuenta con una lista de recetas, donde cada una tiene una serie de ingredientes necesarios, y una lista de ingredientes iniciales que se poseen en cantidad ilimitada.

El objetivo es devolver una lista con todas las recetas que pueden ser creadas utilizando los ingredientes disponibles o aquellas que se pueden generar a partir de otras recetas previamente preparadas.

## Implementación

La implementación se realiza en Python utilizando una clase `Solution` que contiene el método `findAllRecipes`. Este método emplea un enfoque basado en **búsqueda en anchura (BFS)** para determinar qué recetas pueden ser creadas de manera incremental.

## Detalles de la implementación

- **Estructuras de datos:** Se utilizan un diccionario `graph` para representar la relación entre ingredientes y recetas, un diccionario `in_degree` para contar los ingredientes requeridos por cada receta, y una cola (`deque`) para procesar los ingredientes disponibles.
- **Inicialización:** Se establece la cantidad de ingredientes requeridos para cada receta en `in_degree` y se construye el grafo `graph` que mapea ingredientes a las recetas que los necesitan.
- **Búsqueda en anchura (BFS):** Se parte de los ingredientes disponibles y se van reduciendo los requisitos de cada receta en `in_degree`. Cuando una receta tiene todos sus ingredientes disponibles, se agrega a la lista de resultados y se considera como un nuevo "ingrediente" disponible.

## Uso

Para utilizar este código, se deben definir las listas de recetas, sus respectivos ingredientes y los ingredientes disponibles. Luego, se crea una instancia de la clase `Solution` y se llama al método `findAllRecipes` con estos datos.

```python
if __name__ == "__main__":
    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies = ["yeast", "flour", "meat"]

    sol = Solution()
    possible_recipes = sol.findAllRecipes(recipes, ingredients, supplies)
    print(possible_recipes)  # Output: ["bread", "sandwich", "burger"]
```

## Conclusión

El ejercicio **"Find All Possible Recipes from Given Supplies"** ofrece una aplicación práctica de la búsqueda en anchura (BFS) para resolver problemas de dependencias. Este enfoque permite construir recetas de manera eficiente utilizando una estructura de grafo y un procesamiento iterativo con una cola.

Este problema es relevante en escenarios donde se deben resolver dependencias en cadenas de producción, sistemas de compilación o gestión de recursos. La solución implementada es eficiente y se adapta a restricciones de tamaño moderado en la entrada.
