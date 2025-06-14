import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo la instancia de Solution antes de cada test."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "n, k, expected_output",
        [
            (13, 2, 10),       # Caso básico, ejemplo clásico de rango pequeño
            (13, 1, 1),        # k=1 debe devolver el número 1, el menor lex orden
            (13, 13, 2),       # k igual al total del rango (13) debe devolver 2
            (100, 10, 17),     # Ejemplo más grande
            (1000, 100, 117),  # Caso intermedio, más amplio
            (1, 1, 1),         # Caso mínimo trivial
            (10, 10, 9),       # Último número lex orden
            (50, 15, 23),      # Caso random
            (5000, 1000, 1175) # Caso grande
        ]
    )
    def test_find_kth_number(self, n, k, expected_output):
        """
        Valido que findKthNumber devuelva el enésimo número en orden lexicográfico
        dentro del rango [1, n].

        Args:
            n (int): Rango superior (inclusive).
            k (int): Posición lexicográfica buscada.
            expected_output (int): Resultado esperado.
        """
        # Compruebo que el resultado coincide con la salida esperada
        assert self.solution.findKthNumber(n, k) == expected_output
