import pytest
from challenge import Solution  # Ajusta el nombre del archivo o el módulo según corresponda


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1,1,0,1,1,1], 3),      # Tres 1 consecutivos al final: [1, 1, 1]
            ([1,0,1,1,0,1], 2),      # Dos 1 consecutivos en el medio: [1, 1]
            ([0,0,0,0,0], 0),        # No hay 1s en la lista, la longitud máxima es 0.
            ([1, 1, 1, 1, 1], 5),    # Todos los elementos son 1, el máximo es 5.
            ([0, 1, 0, 1, 1, 1, 0], 3), # Tres 1 consecutivos: [1, 1, 1]
            ([1, 0, 0, 1, 0, 1], 1), # Solo hay cadenas de 1 individual.
            ([1], 1),                # Caso con un solo 1 en la lista.
            ([0, 1], 1),             # Un 1 después de un 0.
            ([0, 1, 0, 1, 0, 1], 1), # Cadenas intercaladas de 1s.
            ([1, 1, 0, 0, 1, 1], 2), # Secuencia corta de 1s consecutivos: [1, 1]
            ([1, 0, 1, 0, 1, 0, 1], 1), # Solo secuencias de 1, intercalados con 0.
        ]
    )
    def test_find_max_consecutive_ones(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función findMaxConsecutiveOnes.

        Args:
            nums (List[int]): La lista de números que se probará.
            expected_output (int): El resultado esperado, que es la longitud máxima de unos consecutivos.
        """
        assert self.solution.findMaxConsecutiveOnes(nums) == expected_output
