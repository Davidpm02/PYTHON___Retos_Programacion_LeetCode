import pytest
from challenge import Solution

# Para simular el comportamiento de la función isBadVersion, supondremos que 
# isBadVersion es una función que simula una versión defectuosa.
# En este caso, debes definir cómo quieres que funcione, 
# como ejemplo aquí asumimos que las versiones malas comienzan a partir de 4.

def isBadVersion(version: int) -> bool:
    # En este ejemplo, supongamos que la versión 4 y todas las siguientes son malas.
    return version >= 4


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (5, 4),  # La primera versión mala es la versión 4 (suponiendo que es 4 y superior)
            (10, 4),  # La primera versión mala es la versión 4
            (20, 4),  # La primera versión mala es la versión 4
            (100, 4),  # La primera versión mala es la versión 4
            (50, 4),   # La primera versión mala es la versión 4
            (3, 3),    # Si n = 3, la última versión es mala, así que retornamos 3
            (1, 1),    # Caso con una sola versión, que es mala
        ]
    )
    def test_first_bad_version(self, n, expected_output):
        """
        Prueba parametrizada para validar la función firstBadVersion.

        Args:
            n (int): El total de versiones.
            expected_output (int): La primera versión mala.
        """
        self.solution.isBadVersion = isBadVersion  # Asignamos la función mock
        assert self.solution.firstBadVersion(n) == expected_output
