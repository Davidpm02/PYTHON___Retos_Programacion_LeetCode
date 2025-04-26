import pytest
from challenge import Solution  


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected_output",
        [
            ([1, 3, 1, 2, 2], 4),                  # Ejemplo clásico donde hay 4 subarrays completos
            ([5, 5, 5, 5], 10),                    # Todos los subarrays son completos porque solo hay un valor distinto
            ([1, 2, 3, 4], 10),                    # Cada subarray que contiene los 4 elementos es completo
            ([1], 1),                              # Un único elemento forma un único subarray completo
            ([1, 2, 1, 2, 1, 2], 15),               # Repeticiones de dos elementos, muchos subarrays completos
            ([4, 5, 6], 6),                        # Subarrays que incluyen todos los elementos distintos (3 distintos)
            ([1, 2, 3, 1, 2], 7),                  # Subarrays con combinaciones repetidas
            ([1, 1, 2, 2, 3, 3], 9),               # Duplicados que no afectan el conteo de subarrays completos
            ([7, 8, 9, 10, 7], 9),                 # Cierre de vuelta a un elemento anterior
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 45),     # Todos los subarrays de tamaño suficiente forman un subarray completo
        ]
    )
    def test_count_complete_subarrays(self, nums, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función countCompleteSubarrays.

        Args:
            nums (List[int]): Lista de números de entrada.
            expected_output (int): Número esperado de subarrays completos.
        """
        assert self.solution.countCompleteSubarrays(nums) == expected_output
