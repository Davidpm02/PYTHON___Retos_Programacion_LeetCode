import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Inicializo una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 2, 3], 0),                       # Todos los elementos son únicos desde el inicio
            ([1, 1, 1, 2, 3, 4], 1),              # El primer trío tiene duplicados; tras una operación, son únicos
            ([1, 1, 1, 1, 1, 1], 2),              # Se necesitan dos operaciones para vaciar y evitar duplicados
            ([1, 2, 2, 3, 4], 1),                 # Una operación basta para quitar los duplicados iniciales
            ([1, 2, 3, 4, 5, 6], 0),              # Todos los elementos son únicos desde el principio
            ([1, 2, 2], 1),                       # Un solo grupo con duplicados que debe eliminarse por completo
            ([1, 1], 1),                          # Menos de 3 elementos y son duplicados
            ([1], 0),                             # Solo un elemento, ya es único
            ([], 0),                              # Array vacío desde el inicio
            ([5, 5, 5, 5, 5, 6, 7, 8], 2),        # Se requieren dos operaciones para dejar sólo valores únicos
            ([1, 2, 2, 3, 3, 4, 4, 5], 2),        # Duplicados persistentes que requieren varias eliminaciones
        ]
    )
    def test_minimum_operations(self, nums, expected_output):
        """
        Prueba parametrizada para validar distintos casos de la función minimumOperations.

        Args:
            nums (List[int]): Lista de enteros a transformar con operaciones.
            expected_output (int): Número mínimo de operaciones necesarias.
        """
        assert self.solution.minimumOperations(nums.copy()) == expected_output
