import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo según corresponda

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "list1, list2, expected_output",
        [
            (["Shogun", "Tapioca Express", "Burger King", "KFC"], 
             ["KFC", "Shogun", "Burger King"], 
             ["Shogun"]),  # Un solo restaurante común, con la menor suma de índices
             
            (["Shogun", "Tapioca Express", "Burger King", "KFC"], 
             ["KFC", "Tapioca Express", "Burger King"], 
             ["Tapioca Express"]),  # Otro restaurante común, con menor suma de índices

            (["A", "B", "C", "D"], 
             ["B", "C", "A", "D"], 
             ["B", "C", "A", "D"]),  # Todos los restaurantes son comunes con índices sumando lo mismo

            (["Sushi", "Burgers", "Pizza"], 
             ["Fries", "Pasta", "Pizza"], 
             ["Pizza"]),  # Solo uno común, "Pizza"

            (["Apple", "Banana", "Grapes"], 
             ["Peach", "Plum"], 
             []),  # Ningún restaurante común
             
            (["C", "A", "B"], 
             ["C", "A", "B"], 
             ["C", "A", "B"]),  # Todos los restaurantes son comunes y suman los mismos índices

            (["Dog", "Cat", "Elephant"], 
             ["Lion", "Cat", "Tiger", "Elephant"], 
             ["Cat", "Elephant"]),  # Dos restaurantes comunes con la misma suma de índices
        ]
    )
    def test_find_restaurant(self, list1, list2, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findRestaurant.

        Args:
            list1 (List[str]): Primera lista de restaurantes.
            list2 (List[str]): Segunda lista de restaurantes.
            expected_output (List[str]): Lista de restaurantes comunes con la menor suma de índices.
        """
        assert self.solution.findRestaurant(list1, list2) == expected_output
