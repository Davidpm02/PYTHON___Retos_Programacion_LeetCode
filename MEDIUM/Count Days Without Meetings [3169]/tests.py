import pytest
from challenge import Solution

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "days, meetings, expected_output",
        [
            (10, [[2, 5], [7, 8]], 4),  # Caso con reuniones en diferentes intervalos
            (5, [[1, 2], [2, 3], [3, 4]], 1),  # Reuniones continuas dejando un solo día libre
            (7, [], 7),  # Caso sin reuniones, todos los días están disponibles
            (3, [[1, 3]], 0),  # Reuniones cubriendo todos los días
            (6, [[2, 3], [4, 5]], 2),  # Reuniones separadas con días libres intermedios
            (15, [[1, 2], [5, 10], [12, 14]], 5),  # Múltiples reuniones en distintos periodos
        ]
    )
    def test_countDays(self, days, meetings, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countDays.

        Args:
            days (int): Número total de días.
            meetings (List[List[int]]): Lista de reuniones con intervalos de días ocupados.
            expected_output (int): Resultado esperado de días disponibles.
        """
        assert self.solution.countDays(days, meetings) == expected_output