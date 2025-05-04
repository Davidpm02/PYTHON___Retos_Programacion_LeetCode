import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "dominoes, expected_output",
        [
            ([[1, 2], [2, 1], [3, 4], [5, 6]], 1),        # Una sola pareja equivalente: [1,2] ~ [2,1]
            ([[1, 2], [1, 2], [1, 2]], 3),                # Tres fichas iguales -> 3 parejas: C(3,2) = 3
            ([[1, 1], [1, 1], [1, 1], [1, 1]], 6),         # Cuatro fichas iguales -> 6 parejas: C(4,2)
            ([[1, 2], [3, 4], [5, 6], [7, 8]], 0),         # Ninguna pareja equivalente
            ([[2, 1], [1, 2], [2, 1], [2, 1]], 6),         # Todas equivalentes entre sí: 4 fichas -> 6 parejas
            ([[1, 2]], 0),                                 # Solo una ficha, ninguna pareja posible
            ([], 0),                                       # Lista vacía, sin fichas
            ([[1, 2], [2, 3], [3, 1], [2, 1], [3, 2], [1, 3]], 3),  # Cada pareja aparece una vez: 3 parejas totales
            ([[4, 5], [5, 4], [4, 5], [5, 4], [4, 5]], 10),         # 5 fichas equivalentes -> C(5,2) = 10
            ([[1, 1], [2, 2], [1, 1], [2, 2]], 2),                  # Dos parejas independientes
        ]
    )
    def test_num_equiv_domino_pairs(self, dominoes, expected_output):
        """
        Prueba parametrizada para validar diferentes casos del método numEquivDominoPairs.

        Args:
            dominoes (List[List[int]]): Lista de fichas de dominó representadas como pares de enteros.
            expected_output (int): Número esperado de parejas equivalentes.
        """
        assert self.solution.numEquivDominoPairs(dominoes) == expected_output
