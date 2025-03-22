import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """Inicializa una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "recipes, ingredients, supplies, expected_output",
        [
            # Caso básico: se pueden preparar todas las recetas
            (
                ["bread", "sandwich"],
                [["flour", "water"], ["bread", "ham"]],
                ["flour", "water", "ham"],
                ["bread", "sandwich"]
            ),
            # Caso donde no se pueden preparar recetas porque faltan ingredientes
            (
                ["cake"],
                [["flour", "sugar", "eggs"]],
                ["flour", "sugar"],
                []
            ),
            # Caso con ciclo: una receta depende de sí misma indirectamente
            (
                ["A", "B"],
                [["B"], ["A"]],
                ["C"],
                []
            ),
            # Caso donde algunas recetas son posibles pero otras no
            (
                ["pasta", "sauce", "lasagna"],
                [["flour", "water"], ["tomato", "salt"], ["pasta", "sauce", "cheese"]],
                ["flour", "water", "tomato", "salt"],
                ["pasta", "sauce"]
            ),
            # Caso con un solo ingrediente disponible, sin relación con recetas
            (
                ["pizza"],
                [["cheese", "dough"]],
                ["flour"],
                []
            ),
            # Caso donde los suministros ya contienen las recetas
            (
                ["salad"],
                [["lettuce", "tomato"]],
                ["lettuce", "tomato", "salad"],
                ["salad"]
            )
        ]
    )
    def test_find_all_recipes(self, recipes, ingredients, supplies, expected_output):
        """
        Prueba parametrizada para validar la función findAllRecipes con múltiples escenarios.

        Args:
            recipes (List[str]): Lista de nombres de recetas.
            ingredients (List[List[str]]): Ingredientes requeridos por cada receta.
            supplies (List[str]): Lista de ingredientes disponibles.
            expected_output (List[str]): Recetas que deberían poder cocinarse.
        """
        assert sorted(self.solution.findAllRecipes(recipes, ingredients, supplies)) == sorted(expected_output)
