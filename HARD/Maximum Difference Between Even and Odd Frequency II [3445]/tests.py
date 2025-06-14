import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "s, k, expected_output",
        [
            ("01234", 3, 1),         # '012' → a=0 (1), b=1 (1) → no válido; '0123' → a=0 (1), b=1 (1) → ...
            ("00011", 2, 1),         # substr '0001': freq[0]=3, freq[1]=1 → impar-par → válido
            ("0123401234", 5, 2),    # repite patrones, posible mayor diferencia en substrings grandes
            ("1111", 2, -1),         # solo dígito 1, no hay freq[b] par != freq[a]
            ("2222", 1, -1),         # todo igual, no hay pares de dígitos distintos
            ("012012012", 3, 1),     # varios substrings válidos, max diff = 1
            ("01", 2, 1),            # justo el tamaño mínimo, freq[0]=1 impar, freq[1]=1 impar → no válido
            ("0120123", 4, 2),       # máximo aparece cuando a y b se separan en frecuencia
            ("321012", 6, 2),        # todo el string → freq[3]=1 impar, freq[2]=2 par → diff = -1
            ("404040404", 3, 1),     # freq[4] y freq[0] alternando entre par/impar
            ("00000", 5, -1),        # no se puede cumplir la condición de a ≠ b
        ]
    )
    def test_max_difference(self, s, k, expected_output):
        """
        Prueba parametrizada para validar diferentes escenarios del método maxDifference.

        Args:
            s (str): Cadena con dígitos entre '0' y '4'.
            k (int): Tamaño mínimo del substring a considerar.
            expected_output (int): Máxima diferencia freq[a] - freq[b] bajo las restricciones dadas.
        """
        assert self.solution.maxDifference(s, k) == expected_output
