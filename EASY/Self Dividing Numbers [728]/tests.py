import pytest
from challenge import Solution  # Asegúrate de importar correctamente la clase Solution.


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "left, right, expected_output",
        [
            (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 18]),    # Ejemplo de rango (1, 22)
            (10, 50, [12, 15, 24, 36, 48]),                   # Ejemplo de rango (10, 50)
            (50, 100, [55, 66, 77, 88, 99]),                  # Ejemplo de rango (50, 100)
            (100, 150, [111, 112, 122, 144]),                 # Ejemplo de rango (100, 150)
            (200, 300, [222, 224, 252, 264, 288]),            # Ejemplo de rango (200, 300)
            (150, 200, [168, 192]),                           # Ejemplo de rango (150, 200)
            (500, 600, [512, 528, 544, 555, 576, 588]),       # Ejemplo de rango (500, 600)
            (1, 1, [1]),                                      # Caso con un solo número en el rango (1, 1)
            (5, 5, [5]),                                      # Caso con un solo número en el rango (5, 5)
            (15, 15, [15]),                                    # Caso con un solo número en el rango (15, 15)
        ]
    )
    def test_self_dividing_numbers(self, left, right, expected_output):
        """
        Prueba parametrizada para validar la función selfDividingNumbers.

        Args:
            left (int): El límite inferior del rango.
            right (int): El límite superior del rango.
            expected_output (List[int]): La lista de números divisibles entre sí en el rango especificado.
        """
        result = self.solution.selfDividingNumbers(left, right)
        assert result == expected_output
