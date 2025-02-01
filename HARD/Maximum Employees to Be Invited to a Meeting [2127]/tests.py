import pytest
from challenge import Solution  # Asegúrate de que el archivo del reto se llame 'challenge.py'

class TestSolution:
    def setup_method(self):
        """
        Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba.
        """
        self.solution = Solution()

    @pytest.mark.parametrize(
        "favorite, expected_output",
        [
            ([2, 2, 1, 2], 3),  # Caso con ciclo de tamaño 2 y cadena extra
            ([1, 2, 0], 3),  # Ciclo de tamaño 3
            ([3, 3, 3, 3], 2),  # Solo conexiones bidireccionales
            ([1, 0, 3, 2], 4),  # Todos están en un ciclo de tamaño 4
            ([0, 1, 2, 3], 1),  # Ciclos individuales
        ]
    )
    def test_maximum_invitations(self, favorite, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función maximumInvitations.

        Args:
            favorite (List[int]): Lista de empleados con su favorito asignado.
            expected_output (int): Número máximo de empleados que pueden asistir.
        """
        assert self.solution.maximumInvitations(favorite) == expected_output
