import pytest
from challenge import Solution  # Asegúrate de que el nombre del archivo sea 'challenge.py' o el que corresponda

class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([2, 2, 4, 4], [4, 8, 0, 0]),  # Ejemplo básico de combinación de números iguales
            ([0, 2, 2, 4, 0], [4, 4, 0, 0, 0]),  # Números con ceros, y combinación de iguales
            ([2, 0, 0, 4, 4], [2, 4, 8, 0, 0]),  # Combinación con ceros en el medio
            ([2, 2, 2, 2], [4, 4, 0, 0]),  # Todos los números iguales y su combinación
            ([1, 0, 0, 0, 3], [1, 3, 0, 0, 0]),  # Ejemplo con ceros y números distintos
            ([0, 0, 0, 0], [0, 0, 0, 0]),  # Caso con solo ceros
            ([2, 0, 2, 0], [4, 0, 0, 0]),  # Números alternados con ceros
            ([4, 0, 0, 4], [8, 0, 0, 0]),  # Combinación de números con ceros
            ([0, 0, 0], [0, 0, 0]),  # Solo ceros
        ]
    )
    def test_apply_operations(self, input_nums, expected_output):
        """
        Prueba parametrizada para validar la función applyOperations.

        Args:
            input_nums (List[int]): Lista de enteros sobre los que se aplicarán las operaciones.
            expected_output (List[int]): El resultado esperado después de aplicar las operaciones.
        """
        assert self.solution.applyOperations(input_nums) == expected_output
