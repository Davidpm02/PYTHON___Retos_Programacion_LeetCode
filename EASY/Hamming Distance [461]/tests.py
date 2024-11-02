import pytest
from challenge import Solution  # Importa la clase Solution desde el módulo correspondiente

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "x, y, expected_output",
        [
            (1, 4, 2),          # Ejemplo básico de distancia de Hamming con 1 y 4
            (3, 1, 1),          # Distancia de Hamming entre 3 (011) y 1 (001)
            (0, 0, 0),          # Mismo número, distancia debe ser 0
            (255, 0, 8),        # Ejemplo donde todos los bits difieren (11111111 vs 00000000)
            (10, 10, 0),        # Mismo número, distancia debe ser 0
            (15, 8, 2),         # Comparación entre 15 (1111) y 8 (1000), con distancia de Hamming 2
            (31, 14, 2),        # Ejemplo con distancia 2
            (100, 250, 5),      # Ejemplo con números más grandes
            (128, 1, 2),        # Distancia de Hamming entre 128 (10000000) y 1 (00000001)
            (5, 9, 2),          # Distancia de Hamming entre 5 (0101) y 9 (1001)
        ]
    )
    def test_hamming_distance(self, x, y, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función hammingDistance.

        Args:
            x (int): Primer número para el cálculo de distancia de Hamming.
            y (int): Segundo número para el cálculo de distancia de Hamming.
            expected_output (int): Distancia de Hamming esperada entre x e y.
        """
        assert self.solution.hammingDistance(x, y) == expected_output
