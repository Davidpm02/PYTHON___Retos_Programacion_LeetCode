import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, expected_output",
        [
            (13, [1,10,11,12,13,2,3,4,5,6,7,8,9]),  # Caso pequeño, salida conocida
            (1, [1]),                               # Caso mínimo
            (10, [1,10,2,3,4,5,6,7,8,9]),          # Límite justo en 10
            (20, [1,10,11,12,13,14,15,16,17,18,19,2,20,3,4,5,6,7,8,9]),  # Caso intermedio
            (9, [1,2,3,4,5,6,7,8,9]),               # Sólo números del 1 al 9
            (0, []),                                # Caso borde sin números
            (100, [1,10,100,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,40,41,42,43,44,45,46,47,48,49,5,50,51,52,53,54,55,56,57,58,59,6,60,61,62,63,64,65,66,67,68,69,7,70,71,72,73,74,75,76,77,78,79,8,80,81,82,83,84,85,86,87,88,89,9,90,91,92,93,94,95,96,97,98,99]) # Caso más grande
        ]
    )
    def test_lexical_order(self, n, expected_output):
        """
        Prueba parametrizada para validar distintos casos de la función lexicalOrder.

        Args:
            n (int): Número hasta el cual se genera la lista.
            expected_output (List[int]): Lista esperada en orden lexicográfico.
        """
        assert self.solution.lexicalOrder(n) == expected_output
