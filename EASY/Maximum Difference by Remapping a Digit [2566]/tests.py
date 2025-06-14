import pytest
from challenge import Solution  # Asumo que el archivo con la clase se llama challenge.py


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "num, expected_output",
        [
            (11891, 99001),   # Cambiando '1' por '9' da 99899, y luego '1' por '0' da 00800 -> 99899 - 800 = 99099
            (555, 888),       # '5' por '9' da 999, y luego '5' por '0' da 000 -> 999 - 0 = 999
            (9, 9),           # Ya es '9', y al cambiarlo por '0' queda 0 -> 9 - 0 = 9
            (123456, 823456), # '1'→'9' da 923456, luego '1'→'0' da 023456 -> 923456 - 23456 = 900000
            (909, 909),       # No hay dígito a cambiar para máximo o mínimo -> misma diferencia
            (100, 900),       # '1'→'9' da 900, y '1'→'0' da 000 -> 900 - 0 = 900
            (90, 90),         # '9'→nada (ya es máximo), '9'→'0' da 00 -> 90 - 0 = 90
            (10, 90),         # '1'→'9' da 90, luego '1'→'0' da 00 -> 90 - 0 = 90
            (9999, 0),        # Todos los dígitos son '9', no se puede mejorar ni empeorar -> 9999 - 9999 = 0
            (8008, 9009),     # '8'→'9' da 9009, luego '8'→'0' da 0000 -> 9009 - 0 = 9009
        ]
    )
    def test_min_max_difference(self, num, expected_output):
        """
        Test parametrizado para comprobar la diferencia entre el número máximo
        y el mínimo que se puede formar mediante el reemplazo de dígitos.

        Args:
            num (int): El número original que se transformará.
            expected_output (int): Diferencia esperada entre el máximo y mínimo posibles.
        """
        assert self.solution.minMaxDifference(num) == expected_output
