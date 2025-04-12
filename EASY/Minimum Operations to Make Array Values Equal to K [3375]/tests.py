import pytest
from challenge import Solution


class TestSolution:
    def setup_method(self):
        """Método de configuración para inicializar una instancia de la clase Solution antes de cada prueba."""
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected_output",
        [
            ([5, 5, 5, 5], 5, 0),               # Todos los elementos ya son iguales a k, no se necesitan operaciones
            ([6, 6, 6, 6], 5, 1),               # Todos los elementos son mayores que k, 1 operación para reducirlos a 5
            ([5, 6, 7, 8], 5, 3),               # Tres valores mayores que k, se necesitan 3 operaciones
            ([10, 20, 30, 40], 25, 2),          # Se necesitan dos operaciones para reducir los valores mayores que 25
            ([7, 8, 9, 10], 5, 3),              # Tres valores mayores que k, todos deben ser reducidos
            ([1, 2, 3, 4], 5, -1),              # Todos los valores son menores que k, imposible llegar a k
            ([5, 10, 15], 12, 1),               # Solo 15 necesita ser reducido a 12, por lo que se requiere una operación
            ([8, 9, 9, 10], 8, 2),              # Se necesitan dos operaciones para reducir 9 y 10 a 8
            ([5, 5, 5], 10, -1),                # No puedo llegar a 10 porque no hay valores mayores que 10
            ([1, 2, 2, 2], 2, 0),               # Todos los valores ya son iguales a 2, no se necesitan operaciones
            ([3, 4, 5, 6], 3, 3),               # Tres valores mayores que 3, se necesitan 3 operaciones
            ([7, 8, 10, 12], 10, 2),            # Se necesitan dos operaciones para reducir 12 y 10 a 10
            ([3, 3, 3], 3, 0),                 # Todos son 3, no se necesita ninguna operación
            ([5, 6, 7, 8], 6, 2),               # Se necesitan dos operaciones para reducir 7 y 8 a 6
        ]
    )
    def test_min_operations(self, nums, k, expected_output):
        """
        Prueba parametrizada para validar diferentes casos de la función minOperations.

        Args:
            nums (List[int]): Lista de enteros a modificar.
            k (int): Valor al que se deben transformar todos los elementos de nums.
            expected_output (int): El número esperado de operaciones para convertir todos los valores a k.
        """
        assert self.solution.minOperations(nums.copy(), k) == expected_output
