import pytest
from challenge import Solution  # Asegúrate de que 'challenge' sea el nombre correcto de tu archivo

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([1, 3, 5, 7, 9], 2, 5),                # Caso básico: robar 2 casas
            ([1, 2, 3, 4, 5], 3, 3),                # Caso: capacidad mínima para robar 3 casas
            ([1, 2, 3, 4, 5, 6], 4, 4),            # Caso con 4 casas a robar
            ([10, 20, 30, 40, 50], 3, 30),          # Caso con números más grandes
            ([1, 10, 100, 1000], 2, 100),           # Capacidades con gran diferencia entre casas
            ([5, 5, 5, 5, 5], 3, 5),               # Caso donde todas las casas tienen la misma cantidad de dinero
            ([1, 100, 1000, 10000], 2, 1000),       # Caso donde una capacidad alta es necesaria
            ([100, 200, 300, 400, 500], 2, 200),    # Probando con una capacidad media
            ([10, 20, 30, 40, 50], 1, 10),           # Caso con k=1 (robar solo una casa)
            ([1], 1, 1),                            # Caso con un solo elemento
        ]
    )
    def test_minCapability(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método minCapability.

        Args:
            nums (List[int]): Lista de valores de las casas.
            k (int): Número de casas que deben ser robadas.
            expected_output (int): La capacidad mínima esperada para robar al menos k casas.
        """
        assert self.solution.minCapability(nums, k) == expected_output
