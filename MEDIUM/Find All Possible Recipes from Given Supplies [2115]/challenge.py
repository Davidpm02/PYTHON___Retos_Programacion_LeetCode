"""
DESCRIPTION:

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

 

Constraints:

    n == recipes.length == ingredients.length
    1 <= n <= 100
    1 <= ingredients[i].length, supplies.length <= 100
    1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
    recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
    All the values of recipes and supplies combined are unique.
    Each ingredients[i] does not contain any duplicate values.

"""

from typing import List
from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        """
        Se encarga de verificar la viabilidad de cocinar un conjunto
        de recetas dadas, en base a una serie de listados de
        ingredientes necesarios y aquellos de los que disponemos para
        cocinar.

        params:
            recipes (List[str])
            ingredients (List[List[str]])
            supplies (List[str])
        
        returns:
            List[str]
        """

        # 1. Inicialización de estructuras de datos
        graph = {}  # Relación ingrediente -> lista de recetas que dependen de él
        in_degree = {}  # Contador de ingredientes necesarios para cada receta

        # Inicializar in_degree con cada receta teniendo el conteo de ingredientes necesario
        for recipe, ingredient_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ingredient_list)  # Número de ingredientes que necesita
            for ingredient in ingredient_list:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipe)  # El ingrediente es necesario para esta receta

        # 2. Cola con elementos que ya pueden producirse
        queue = deque(supplies)  # Partimos con los ingredientes iniciales como "producibles"
        producible = set(supplies)  # Conjunto para rápido acceso

        # 3. Procesamiento de la cola (BFS)
        result = []
        while queue:
            ingredient = queue.popleft()

            # Si este ingrediente desbloquea recetas, procesarlas
            if ingredient in graph:
                for recipe in graph[ingredient]:
                    in_degree[recipe] -= 1  # Reducimos la cantidad de ingredientes pendientes
                    if in_degree[recipe] == 0:  # Si ya no requiere más ingredientes, es creable
                        queue.append(recipe)
                        producible.add(recipe)
                        result.append(recipe)

        return result
