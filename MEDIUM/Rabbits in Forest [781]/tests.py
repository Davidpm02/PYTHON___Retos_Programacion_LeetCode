import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "answers, expected_output",
        [
            ([1, 1, 2], 5),              # Hay 2 conejos que ven 1 igual a ellos (2+1=3), y uno que ve 2 iguales (3 conejos).
            ([10, 10, 10], 11),          # Tres conejos que ven 10 iguales, pero con un solo grupo basta (11 conejos en total).
            ([0, 0, 1, 1, 1], 6),        # Dos conejos solos (0+1=1 conejo cada uno) y tres que ven 1 igual (2 conejos por grupo).
            ([0], 1),                    # Un conejo que dice no ver ninguno más: solo él mismo.
            ([1], 2),                    # Un conejo que ve 1 igual: se necesitan 2 conejos en total.
            ([2, 2, 2], 3),              # Tres conejos que ven 2 iguales: todos pertenecen a un único grupo de 3.
            ([], 0),                     # Sin respuestas, no hay conejos.
            ([3, 3, 3, 3, 3, 3, 3], 8),  # Siete conejos que ven 3 iguales: necesito dos grupos (cada grupo de 4).
            ([1, 0, 1, 0, 0], 6),        # Mezcla de conejos solos y que ven uno igual.
            ([5, 5, 5, 5, 5, 5, 5, 5], 12), # Ocho conejos que ven 5 iguales: se necesitan dos grupos de 6.
        ]
    )
    def test_num_rabbits(self, answers, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función numRabbits.

        Args:
            answers (List[int]): Lista de respuestas de los conejos.
            expected_output (int): Número mínimo esperado de conejos en el bosque.
        """
        assert self.solution.numRabbits(answers) == expected_output
