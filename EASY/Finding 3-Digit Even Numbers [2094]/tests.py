import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "digits, expected_output",
        [
            ([2, 1, 3, 0], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),  # Múltiples combinaciones posibles
            ([2, 2, 8, 8, 2], [228, 282, 288, 822, 828, 882]),                   # Dígitos repetidos
            ([0, 0, 0], []),                                                    # No se pueden formar números de 3 dígitos válidos
            ([1, 2, 3, 4, 5], [120, 124, 130, 132, 134, 140, 142, 150, 152, 154,
                               210, 214, 230, 234, 240, 250, 312, 314, 320, 324,
                               340, 350, 410, 412, 430, 432, 450, 452, 510, 512,
                               514, 520, 530, 532, 540, 542]),                  # Mayor rango de posibilidades
            ([1, 3, 5, 7, 9], []),                                              # Ningún dígito par, por tanto ningún número par
            ([0, 1, 2], [102, 120]),                                            # Solo dos números válidos posibles
            ([0, 1, 2, 3], [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]),  # Repetición de caso base
            ([4, 6, 5, 7], [456, 465, 546, 564, 654, 674, 754, 764]),            # Todos pares válidos en distintas combinaciones
        ]
    )
    def test_find_even_numbers(self, digits, expected_output):
        """
        Test parametrizado para verificar múltiples casos del método findEvenNumbers.

        Args:
            digits (List[int]): Lista de dígitos disponibles.
            expected_output (List[int]): Lista ordenada de números pares de 3 dígitos posibles.
        """
        assert self.solution.findEvenNumbers(digits) == expected_output
